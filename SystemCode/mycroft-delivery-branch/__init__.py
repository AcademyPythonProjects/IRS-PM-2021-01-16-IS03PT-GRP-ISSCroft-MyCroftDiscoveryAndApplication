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


class DeliveryProject(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()
        self.url_start='http://42.60.37.128:5000/iss/delivery/address/5/761512'
        self.url_next='http://42.60.37.128:5000/iss/delivery/address/5/761512'
        self.url_resolve_address='https://developers.onemap.sg/commonapi/search?searchVal='
        self.current_postcode=761512
        self.current_location=''
        self.remain_package=0

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')


    @intent_handler(IntentBuilder('startIntent').require('start'))
    def handle_start_intent(self, message):
        r=requests.get(self.url_start)
        if r.status_code==200:
            myadd=[int(s) for s in r.text.split() if s.isdigit()]
            self.current_postcode=myadd[1]
            self.remain_package=myadd[0]
            #r1=requests.get(self.url_resolve_address+str(myadd[1])+'&returnGeom=N&getAddrDetails=Y')
            #if r1.status_code==200:
            #    data=json.loads(r1.text)
            #    self.current_location=data['results'][0]['SEARCHVAL']
            self.speak_dialog('Vehicle 5. Your next delivery point is '+str(myadd[1]))
            #self.log.info('Vehicle 5. Your next delivery point is '+str(myadd[1])
            self.url_next='http://42.60.37.128:5000/iss/delivery/address/5/'+str(myadd[1])
        else:
            self.speak_dialog('Sorry, you have no package to deliver')


    @intent_handler(IntentBuilder('nextIntent').require('next'))
    def handle_ask_intent(self, message):
        r=requests.get(self.url_next)
        if r.status_code==200:
            myadd=[int(s) for s in r.text.split() if s.isdigit()]
            if len(myadd)!=0:
                self.current_postcode=myadd[1]
                self.remain_package=myadd[0]
                #r1=requests.get(self.url_resolve_address+str(myadd[1])+'&returnGeom=N&getAddrDetails=Y')
                #if r1.status_code==200:
                #    data=json.loads(r1.text)
                #    self.current_location=data['results'][0]['SEARCHVAL']
                self.speak_dialog('Vehicle 5. Your next delivery point is '+str(myadd[1]))
                #self.log.info('Vehicle 5. Your next delivery point is '+str(myadd[1])
                self.url_next='http://42.60.37.128:5000/iss/delivery/address/5/'+str(myadd[1])
            else:
                self.speak_dialog('You complete the delivery')
        else:
            self.speak_dialog('Sorry, you have no package to deliver')

    @intent_handler(IntentBuilder('checkIntent').require('check'))
    def handle_check_intent(self, message):
        self.speak_dialog('You have '+str(self.remain_package)+' package to deliver, current at '+str(self.current_postcode))


    def stop(self):
        pass


def create_skill():
    return DeliveryProject()
