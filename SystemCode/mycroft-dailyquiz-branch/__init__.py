# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import requests
import json
import random


class LoadProject(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()
        self.learning = True
        self.url='https://opentdb.com/api.php?amount=1&category=27&difficulty=easy&type=boolean'
        self.question=None
        self.answer=''
        self.score=0
        self.retry=0

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')

    @intent_handler(IntentBuilder('askIntent').require('ask'))
    def handle_ask_intent(self, message):
        r=requests.get(self.url)
        if r.status_code==200:
            data=json.loads(r.text)
            self.log.info(data)
            self.question=data['results'][0]['question']
            self.answer=data['results'][0]['correct_answer'].lower().strip()
            self.speak_dialog(self.question)
            self.retry=0
            #self.speak_dialog(self.answer)
        else:
            self.speak_dialog('Please try again')

    @intent_handler(IntentBuilder('ansIntent').require('ans'))
    def handle_ans_intent(self, message):
        ans=message.data.get('utterance')
        if self.answer==ans:
            self.speak_dialog('You are good')
            if self.retry==0:
                self.score=self.score+1
        else:
            self.speak_dialog('Sorry try again')
        self.retry=self.retry+1

    @intent_handler(IntentBuilder('scoreIntent').require('score'))
    def handle_score_intent(self, message):
        self.speak_dialog('Your score is '+str(self.score))

    @intent_handler(IntentBuilder('resetIntent').require('reset'))
    def handle_reset_intent(self, message):
        self.score=0
        self.retry=0
        self.speak_dialog('Your score is reset.')

    def stop(self):
        pass


def create_skill():
    return LoadProject()
