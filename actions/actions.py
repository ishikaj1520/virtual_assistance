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
         print(response['status'])
         if( response['status']=="hold"):
           dispatcher.utter_message("The status of your order is hold.")
           base_zipcode = 'https://app.zipcodebase.com/api/v1/search?apikey=d263f8e0-2ced-11ec-a591-333aa69c9333&codes='
           zipcode_url = ''.join([base_zipcode, response['postal']])
           zip_auth = requests.get(zipcode_url).json()
           zip_code = response["province"]
           #print(zip_auth["results"][zip_code][0]["state_code"])
           try:
            if(zip_auth["results"][response['postal']][0]["state_code"]!=zip_code):
              dispatcher.utter_message("Your pincode seems to be invalid. Please provide a valid pincode")
           except:
               dispatcher.utter_message("Your pincode seems to be invalid. Please provide a valid pincode")
            #else:

           regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
           email=response["email"]
           if not re.search(regex, email):
              dispatcher.utter_message("Your email id seems to be invalid. PLease provide a valid email id")
                # regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                # email= tracker.get_slot("email")
                # if re.search(regex, email):
                #   dispatcher.utter_message("Your email id seems to be invalid. PLease provide a valid email id")
                # if(zip_auth["results"][zip_code][0]["country_code"]!=zip_code)
                #   dispatcher.utter_message("Your pincode seems to be invalid. Please provide a valid pincode")
         else:
           dispatcher.utter_message("The status of your order is Success! The Product will be delivered soon")
           #x = requests.post(url,json={"order_status":"Success"})
         return[]







class ActionValidation(Action):

    def name(self) -> Text:
        return "action_validation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pin_valid=False
        email_valid=False
        if not tracker.get_slot("orderid"):
          dispatcher.utter_message("Please enter order id first")
        else:
            #regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
            if tracker.get_slot("pincode"):
              pincode = tracker.get_slot("pincode")
              base_zipcode = 'https://app.zipcodebase.com/api/v1/search?apikey=d263f8e0-2ced-11ec-a591-333aa69c9333&codes='
              zipcode_url = ''.join([base_zipcode, pincode])
              zip_auth = requests.get(zipcode_url).json()

              base_url1 = 'https://us-central1-virtual-assistance-1.cloudfunctions.net/app/api/read/'
              url1 = ''.join([base_url1, tracker.get_slot("orderid")])
              response = requests.get(url1).json()
              zip_code = response["province"]
              #print(zip_auth["results"][pincode][0]["state_code"])
              print("Checking pin")
              try:
                if(zip_auth["results"][pincode][0]["state_code"]!=zip_code):
                  dispatcher.utter_message("Your pincode seems to be invalid. Please provide a valid pincode")
                else:
                  pin_valid=True
              except:
                dispatcher.utter_message("Your pincode seems to be invalid. Please provide a valid pincode")


            if tracker.get_slot("email"):
              regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
              email=tracker.get_slot("email")
              if not re.search(regex, email):
                dispatcher.utter_message("Your email id seems to be invalid. PLease provide a valid email id")
              else:
                email_valid=True
            
            if(pin_valid and email_valid):
             
              url='https://us-central1-virtual-assistance-1.cloudfunctions.net/app/api/read/'+ tracker.get_slot("orderid")
              obj=requests.get(url).json()
              obj["postal"]=tracker.get_slot("pincode")
              obj["email"]=tracker.get_slot("email")
              obj["status"]="Success"
              url= "https://us-central1-virtual-assistance-1.cloudfunctions.net/app/api/update"
              res= requests.post(url,json=obj)

              url='https://us-central1-virtual-assistance-1.cloudfunctions.net/app/api/read/'+ tracker.get_slot("orderid")
              response=requests.get(url).json()
              if response["status"]=="Success":
                print("updated")
              dispatcher.utter_message("Thankyou for the details. The status of your order is Success! The Product will be delivered soon")
        return []


class ActionAdmin(Action):

     def name(self) -> Text:
         return "action_admin"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             if(tracker.get_slot("mode")=="admin"):
                dispatcher.utter_message("Hello admin")
             else:
                dispatcher.utter_message("Sorry you are not the admin")
             return []