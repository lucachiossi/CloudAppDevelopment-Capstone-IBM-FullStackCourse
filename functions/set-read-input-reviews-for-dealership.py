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

def main(dict):
    if 'dealerId' in dict:
        return {
            "query": {
                "selector": {
                    "dealership": {
                        "$eq": int(dict['dealerId'])
                        }
                    },
                "fields": [
                    "id",
                    "name",
                    "dealership",
                    "review",
                    "purchase",
                    "purchase_date",
                    "car_make",
                    "car_model",
                    "car_year"
                    ]
                }
            }
    else:
        return {
            "query": {
                "selector": {
                    "dealership": {
                        "$gt": -1
                        }
                    },
                "fields": [
                    "id",
                    "name",
                    "dealership",
                    "review",
                    "purchase",
                    "purchase_date",
                    "car_make",
                    "car_model",
                    "car_year"
                    ]
                }
            }
