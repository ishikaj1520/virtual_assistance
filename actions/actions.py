# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from requests.models import Response

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json
import re


#class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_order"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

             orderid = tracker.get_slot("orderid")
             
             base_url1 = 'https://us-central1-virtual-assistance-1.cloudfunctions.net/app/api/read/'
             url1 = ''.join([base_url1, orderid])

             response = requests.get(url1).json()
#{"email":"carole_hughlett@hughlett.com","order_id":"BC022"}
             #data = response.text
             #parse_json = json.loads(data)
            # for data in response["email"]:
               # print(data)

             message = response['email'] + response["order_id"]
             print(message)
             dispatcher.utter_message(message)
             self.authenticate(response, dispatcher)
             return []

     def authenticate(self, response, dispatcher):
         #print("authenticate")
         if( response['status']=="hold"):
           base_zipcode = 'https://app.zipcodebase.com/api/v1/search?apikey=d263f8e0-2ced-11ec-a591-333aa69c9333&codes='
           zipcode_url = ''.join([base_zipcode, response['postal']])
           zip_auth = requests.get(zipcode_url).json()
           zip_code = response["postal"]
           print(zip_auth["results"][zip_code][0]["country_code"])
               #if re.fullmatch("\d{4}|\d{6}", response["postal"])!=True:
                #  dispatcher.utter_message("Your pincode seems to be invalid. Please provide a valid pincode")
         else:
          dispatcher.utter_message("The status of your order is Success! The Product will be delivered soon")
          #url= "https://us-central1-virtual-assistance-1.cloudfunctions.net/app/api/update/BC022"
          #x = requests.post(url,json={"order_status":"Success"})
          return[]
 
#class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_admin user"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#         
#
#         return []