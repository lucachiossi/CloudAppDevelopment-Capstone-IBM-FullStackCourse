import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth
from django.conf import settings


def get_request(url, **kwargs):
    """
    get_request function will call request.get(url, headers, params=kwargs)
    the function is expected to work with http messages passing data in json format

    url: url passed as parameter
    headers: 'Content-Type' and 'cp_api_key'
    params: pairs passed as parameters (kwargs)

    'Content-Type' value fixed as 'application/json'
    'cp_cl_api_key' needs to be passed in the payload in order to interact with
        a Cloudant service rest api
    'cp_wnlu_api_key' needs to be passed in the payload in order to interact with
        a WatsonNaturalLanguageUnderstandin service 
    """
    print("get_request: received kwargs {}".format(kwargs))
    print("get_request: received url {}".format(url))
    try:
        if 'cp_cl_api_key' in kwargs:
            # Cloudant service rest api request
            cp_cl_api_key = kwargs['cp_cl_api_key']
            # prepare payload
            del kwargs['cp_cl_api_key']
            # prepare header
            headers = {'Content-Type': 'application/json', 'cp_api_key': cp_cl_api_key}
            # call get method 
            response = requests.get(url=url,headers=headers,params=kwargs)
        elif 'cp_wnlu_api_key' in kwargs:
            # WNLU service request
            cp_wnlu_api_key = kwargs['cp_wnlu_api_key']
            # prepare payload
            params = dict()
            params['text'] = kwargs['text']
            params['version'] = kwargs['version']
            params['features'] = kwargs['features']
            params['return_analyzed_text'] = kwargs['return_analyzed_text']
            print("WNLU request params {}".format(params))
            # prepare header
            headers = {'Content-Type': 'application/json'}
            response = requests.get(url=url,headers=headers,params=kwargs,\
                    auth=HTTPBasicAuth('apikey',cp_wnlu_api_key))
        else:
            # no service key has been specified
            print("neither cp_cl_api_key nor cp_wnlu_api_key has been specified")
            return {}
    except:
        # if any error occurs print it
        print("Network exception occurred!!!")
        return {}
    status_code = response.status_code
    print("get_request: received response with status code {}".format(status_code))
    json_data = json.loads(response.text)
    return json_data


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Get dealers from cloud
def parse_dealers(json_data):
    car_dealers_list = []
    for dealership in json_data['docs']:
        dealer_obj = CarDealer(
           dealership['address'],
           dealership['city'],
           dealership['full_name'],
           dealership['id'],
           dealership['lat'],
           dealership['long'],
           dealership['state'],
           dealership['st'],
           dealership['zip']
        )
        car_dealers_list.append(dealer_obj)
    return car_dealers_list


def get_dealers_from_cf(url,cp_cl_api_key):
    json_data = get_request(url=url,cp_cl_api_key=cp_cl_api_key)
    return parse_dealers(json_data)

def get_dealers_by_state(url,cp_cl_api_key,state):
    json_data = get_request(url,cp_cl_api_key=cp_cl_api_key,state=state)
    return parse_dealers(json_data)


# Get dealer reviews from cloud
def parse_dealer_reviews(json_data):
    dealer_reviews = []
    for review in json_data['docs']:
        if review['purchase']:
            review_obj = DealerReview(
                review['id'],
                review['dealership'],
                review['name'],
                review['purchase'],
                review['review'],
                review['purchase_date'],
                review['car_make'],
                review['car_model'],
                review['car_year']
            )
        else:
            review_obj = DealerReview(
                review['id'],
                review['dealership'],
                review['name'],
                review['purchase'],
                review['review']
            )
        print("analyze_review_sentiments...")
        review_obj.sentiment = analyze_review_sentiments(review_obj.review)
        dealer_reviews.append(review_obj)
    return dealer_reviews


def get_dealer_reviews_from_cf(url,cp_cl_api_key,dealer_id):
    json_data = get_request(url,cp_cl_api_key=cp_cl_api_key,dealerId=dealer_id)
    return parse_dealer_reviews(json_data)


# `analyze_review_sentiments` method to call Watson NLU and analyze text
def analyze_review_sentiments(dealer_review):
    json_data = get_request(
        url=settings.WNLU_API_URL + "v1/analyze",
        cp_wnlu_api_key=settings.WNLU_API_KEY,
        version="2021-03-25",
        text=dealer_review,
        features="sentiment",
        return_analyzed_text=True
    )
    return json_data['sentiment']['document']['label']
