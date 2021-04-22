import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth
from django.conf import settings


def get_request(url, **kwargs):
    """
    get_request function will call request.get(url, headers, params=kwargs)
    the function is expected to work with http messages passing data in json format

    url: url passed as parameter
    headers: 'Content-Type' and 'cp_api_key'
    params: pairs passed as parameters (kwargs)

    'cp_api_key' needs the environment variable $CP_API_KEY defined with valid key to access
        the rest api
    'Content-Type' value fixed as 'application/json'
    """
    cp_api_key = settings.CP_API_KEY
    headers = {'Content-Type': 'application/json', 'cp_api_key': cp_api_key}
    print("get_request: url {}".format(url))
    print("get_request: params {}".format(kwargs))
    try:
        # call get method with loaded payload
        response = requests.get(url=url,headers=headers,params=kwargs)
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


def get_dealers_from_cf(url):
    json_data = get_request(url=url)
    return parse_dealers(json_data)

def get_dealers_by_state(url,state):
    json_data = get_request(url,state=state)
    return parse_dealers(json_data)


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
