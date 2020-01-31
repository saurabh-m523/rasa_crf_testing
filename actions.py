from typing import Any, Text, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.events import FollowupAction
from rasa_sdk.executor import CollectingDispatcher


class ActionUtterChitchat(Action):
    """Revertible mapped action for chitchat"""

    def name(self):
        return "action_utter_chitchat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message("I can't help you with that currently.")

        return [FollowupAction('action_restart')]
