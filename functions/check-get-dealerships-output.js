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
  if(!params.hasOwnProperty("docs")){
    return {
      "status": 500,
      "message": "Something went wrong on the server"
    };
  }
  else if(params.docs.length > 0) {
    return params;
  }
  else {
    return {
      "status": 404,
      "message": "The database is empty or The state does not exist"
    };
  }
}

