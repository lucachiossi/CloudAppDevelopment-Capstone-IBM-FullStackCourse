import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth


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
    cp_api_key = ""
    headers = {'Content-Type': 'application/json', 'cp_api_key': cp_api_key}
    try:
        # call get method with loaded payload
        response = requests.get(url,headers=headers,params=kwargs)
    except:
        # if any error occurs print it
        print("Network exception occurred!!!")
        return {}
    status_code = response.status_code
    print("received response with status code {}".format(status_code))
    json_data = json.loads(response.text)
    return json_data




# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
