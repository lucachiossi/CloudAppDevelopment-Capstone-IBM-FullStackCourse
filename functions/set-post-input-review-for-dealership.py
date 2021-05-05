#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys

def parse_review(review):
    try:
        if review['purchase']:
            return {
                'doc' : {
                    'id' : review['id'],
                    'name': review['name'],
                    'dealership': review['dealership'],
                    'review': review['review'],
                    'purchase': review['purchase'],
                    'purchase_date': review['purchase_date'],
                    'car_make': review['car_make'],
                    'car_model': review['car_model'],
                    'car_year': review['car_year']
                    }
                }
        else:
            return {
                'doc' : {
                    'id' : review['id'],
                    'name': review['name'],
                    'dealership': review['dealership'],
                    'review': review['review'],
                    'purchase': review['purchase']
                    }
                }
    except:
        return {}


    def main(dict):
        if 'review' in dict:
            return parse_review(dict['review'])
        else:
            return {}

