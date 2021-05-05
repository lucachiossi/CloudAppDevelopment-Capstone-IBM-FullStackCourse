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
    if not 'docs' in dict:
        return {
            "status": 500,
            "message": "Something went wrong on the server"
            }
    elif len(dict['docs']) > 0:
        return dict
    else:
        return {
            "status": 404,
            "message": "The database is empty or dealerId does not exist"
            }

