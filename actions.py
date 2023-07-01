# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
#
# class ActionHelloWorld(Action):
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

#class ActionHelloWorld(Action):

    #def name(self) -> Text:
        #return "action_hello_world"

    #def run(self, dispatcher: CollectingDispatcher,
            #tracker: Tracker,
            #domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#create custom action logic
        #dispatcher.utter_message(text="This is Hello World from custom action.")

        #return []
    
#class SearchRestaurant(Action):

    #def name(self) -> Text:
        #return "action_search_restaurant"

    #def run(self, dispatcher: CollectingDispatcher,
            #tracker: Tracker,
            #domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #entities=tracker.latest_message['entities']
        #message="No cuisine mentioned"
        #for e in entities:
            #if e['entity']=='cuisine':
                #cuisine=e['value']
                #if cuisine=="indian":
                    #message="Indian 1, Indian 2, Indian 3"
                #elif cuisine=="chinese":
                    #message="chinese 1,chinese 2,chinese 3"
                #else:
                    #message="We do not have any restaurants for this cuisine"            
        #dispatcher.utter_message(text=message)

        #return []
    
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommendAttractions(Action):

    def name(self) -> Text:
        return "action_search_destinations_attractions"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       # Fetch the entities
        destination = next(tracker.get_latest_entity_values("destination"), None)
        attraction = next(tracker.get_latest_entity_values("attraction"), None)
        if destination == "Paris" and attraction == "tourist attractions":
            response = "In Paris, you must visit the Louvre and Eiffel Tower. They are world-renowned."
        elif destination == "Italy" and attraction == "tourist attractions":
            response = "In Italy, you can visit Leaning Tower of Pisa and Trevi Fountain. They're both excellent."
        elif destination == "Germany" and attraction == "tourist attractions":
            response = "In Germany, you can visit Miniatur Wunderland and English Garden. They're both beautiful places."
        else:
            response = "I'm sorry, I don't have recommendations for that specific request."

        dispatcher.utter_message(response)

        return []

