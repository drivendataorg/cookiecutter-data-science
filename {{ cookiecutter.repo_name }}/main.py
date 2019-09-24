try:
    import unzip_requirements
except ImportError:
    pass



def lambda_function(event, context):
    request_json = None
    ## For local test the lambda_function recieves a dict instead of a json-str
    if type(event) == dict:
        raw_response = "I'm testing"
    else:
        raw_response = "I'm deployed"

    return {
            'isBase64Encoded': False,
            'statusCode': 201,
            'headers': { 'Content-type': 'application/json' },
            'body': json.dumps(raw_response)
            }
