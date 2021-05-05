/**
 *
 * main() will be run when you invoke this action
 *
 * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
 *
 * @return The output of this action, which must be a JSON object.
 *
 */
function main(params) {
  state = params.state
  dealer_id = params.dealer_id
  if ((typeof state === 'string' || state instanceof String) && state !== "") {
    return {
      "query": {
        "selector": {
          "st": {
            "$eq": state
          }
        },
        "fields": [
          "id",
          "city",
          "state",
          "st",
          "address",
          "zip",
          "lat",
          "long",
          "full_name"
        ]
      }
    };
  }
  else if ((typeof dealer_id === 'string' || dealer_id instanceof String) && dealer_id !== "") {
    dealer_id= Number(dealer_id)
    if(dealer_id <= 0 || !Number.isInteger(dealer_id)) {
      dealer_id = -1;
    }
    return {
      "query": {
        "selector": {
          "id": {
            "$eq": dealer_id
          }
        },
        "fields": [
          "id",
          "city",
          "state",
          "st",
          "address",
          "zip",
          "lat",
          "long",
          "full_name"
        ]
      }
    };
  }
  return {
    "query": {
      "selector": {
        "st": {
          "$regex": ".*"
        }
      },
      "fields": [
        "id",
        "city",
        "state",
        "st",
        "address",
        "zip",
        "lat",
        "long",
        "full_name"
      ]
    }
  };
}
