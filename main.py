## imports
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions

## functions
## init funtion 
def in_it():
  print("in_it method ")
  callIbmNlu()


def callIbmNlu():
  natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='syvCtnQCZoxqdJBqWRBFQQ-6jny7hUUOA8f9WQZdjEGH',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api'
  )
  
  response = natural_language_understanding.analyze(
    url='www.ibm.com',
    features=Features(keywords=KeywordsOptions(sentiment=True,emotion=True,limit=2))).get_result()
  
  print(json.dumps(response, indent=2))


## main function
if __name__ == "__main__":
  print("__main__ method ")
  ## call init to start flow
  in_it()
