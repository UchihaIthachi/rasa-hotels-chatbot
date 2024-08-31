from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckAvailability(Action):

    def name(self) -> Text:
        return "action_check_availability"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hotel_name = tracker.get_slot('hotel_name')
        room_type = tracker.get_slot('room_type')
        date = tracker.get_slot('date')

        dispatcher.utter_message(
            text=f"Checking availability for {room_type} room at {hotel_name} on {date}..."
        )

        # Simulate availability check
        dispatcher.utter_message(
            text=f"{room_type} room is available at {hotel_name} on {date}."
        )

        return []

class ActionCheckAmenities(Action):

    def name(self) -> Text:
        return "action_check_amenities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hotel_name = tracker.get_slot('hotel_name')
        amenities = "Free Wi-Fi, Pool, Spa, Restaurant, Gym"

        dispatcher.utter_message(
            text=f"{hotel_name} offers the following amenities: {amenities}."
        )

        return []

class ActionCheckPrice(Action):

    def name(self) -> Text:
        return "action_check_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hotel_name = tracker.get_slot('hotel_name')
        room_type = tracker.get_slot('room_type')
        price_range = tracker.get_slot('price_range')

        dispatcher.utter_message(
            text=f"The {room_type} room at {hotel_name} is available in your price range {price_range}."
        )

        return []

class ActionAskLocation(Action):

    def name(self) -> Text:
        return "action_ask_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hotel_name = tracker.get_slot('hotel_name')

        dispatcher.utter_message(
            text=f"{hotel_name} is located in the city center, close to major attractions."
        )

        return []

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from supabase_client import get_supabase_client  # Import the function to get Supabase client

# class ActionCheckAvailability(Action):

#     def name(self) -> Text:
#         return "action_check_availability"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         hotel_name = tracker.get_slot('hotel_name')
#         room_type = tracker.get_slot('room_type')
#         date = tracker.get_slot('date')

#         # Initialize Supabase client
#         supabase = get_supabase_client()

#         # Fetch availability data from Supabase
#         availability = supabase.from_('rooms').select('*').eq('hotel_name', hotel_name).eq('room_type', room_type).eq('date', date).execute()
        
#         if availability.data:
#             dispatcher.utter_message(
#                 text=f"{room_type} room is available at {hotel_name} on {date}."
#             )
#         else:
#             dispatcher.utter_message(
#                 text=f"Sorry, no {room_type} room is available at {hotel_name} on {date}."
#             )

#         return []

# class ActionCheckAmenities(Action):

#     def name(self) -> Text:
#         return "action_check_amenities"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         hotel_name = tracker.get_slot('hotel_name')

#         # Initialize Supabase client
#         supabase = get_supabase_client()

#         # Fetch amenities data from Supabase
#         amenities = supabase.from_('hotels').select('amenities').eq('hotel_name', hotel_name).execute()

#         if amenities.data:
#             amenities_list = amenities.data[0]['amenities']
#             dispatcher.utter_message(
#                 text=f"{hotel_name} offers the following amenities: {amenities_list}."
#             )
#         else:
#             dispatcher.utter_message(
#                 text=f"Sorry, I couldn't find amenities for {hotel_name}."
#             )

#         return []

# class ActionCheckPrice(Action):

#     def name(self) -> Text:
#         return "action_check_price"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         hotel_name = tracker.get_slot('hotel_name')
#         room_type = tracker.get_slot('room_type')
#         price_range = tracker.get_slot('price_range')

#         # Initialize Supabase client
#         supabase = get_supabase_client()

#         # Fetch price data from Supabase
#         price = supabase.from_('rooms').select('price').eq('hotel_name', hotel_name).eq('room_type', room_type).execute()

#         if price.data:
#             room_price = price.data[0]['price']
#             if room_price in price_range:
#                 dispatcher.utter_message(
#                     text=f"The {room_type} room at {hotel_name} is available in your price range."
#                 )
#             else:
#                 dispatcher.utter_message(
#                     text=f"The {room_type} room at {hotel_name} is not available in your price range."
#                 )
#         else:
#             dispatcher.utter_message(
#                 text=f"Sorry, I couldn't find the price for a {room_type} room at {hotel_name}."
#             )

#         return []

# class ActionAskLocation(Action):

#     def name(self) -> Text:
#         return "action_ask_location"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         hotel_name = tracker.get_slot('hotel_name')

#         # Initialize Supabase client
#         supabase = get_supabase_client()

#         # Fetch location data from Supabase
#         location = supabase.from_('hotels').select('location').eq('hotel_name', hotel_name).execute()

#         if location.data:
#             hotel_location = location.data[0]['location']
#             dispatcher.utter_message(
#                 text=f"{hotel_name} is located at {hotel_location}."
#             )
#         else:
#             dispatcher.utter_message(
#                 text=f"Sorry, I couldn't find the location for {hotel_name}."
#             )

#         return []


