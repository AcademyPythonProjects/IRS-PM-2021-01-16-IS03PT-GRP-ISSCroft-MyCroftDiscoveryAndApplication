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

from mycroft.messagebus.message import Message
from mycroft.skills.core import intent_handler
from mycroft.util import get_arch, connected, LOG
import json
import requests
from requests import HTTPError, RequestException
import os
import re
from os.path import join, expanduser, isdir
from mycroft.skills.context import adds_context, removes_context
#API URL hosted on local
#ISS_API_URL = "http://127.0.0.1:5000"
#API URL accessed via internet
ISS_API_URL = "http://42.60.37.128:5000"

ISS_SKILL_PATH="/opt/mycroft/skills/mycroft-iss-project"

class Api:
    """ Generic class to wrap web APIs """
    
    def __init__(self, path):
        self.path = path      
        self.url = ISS_API_URL       

    def request(self, params):        
   
        self.build_path(params)
        return self.send(params)

   

    def send(self, params):

        query_data = frozenset(params.get('query', {}).items())
        params_key = (params.get('path'), query_data)
       
        method = params.get("method", "GET")
        headers = self.build_headers(params)
        data = self.build_data(params)
        json_body = self.build_json(params)
        query = self.build_query(params)
        url = self.build_url(params)

    
        response = requests.request(
            method, url, headers=headers, params=query,
            data=data, json=json_body, timeout=(3.05, 15)
        )
       
        return self.get_response(response)

    def get_response(self, response):
     
        data = self.get_data(response)

        if 200 <= response.status_code < 300:
            return data
 
        raise HTTPError(data, response=response)

    def get_data(self, response):
        try:
            return response.json()
        except Exception:
            return response.text

    def build_headers(self, params):
        headers = params.get("headers", {})
        self.add_content_type(headers)
        params["headers"] = headers
        return headers

    def add_content_type(self, headers):
        if not headers.__contains__("Content-Type"):
            headers["Content-Type"] = "application/json"


    def build_data(self, params):
        return params.get("data")

    def build_json(self, params):
        json = params.get("json")
        if json and params["headers"]["Content-Type"] == "application/json":
            for k, v in json.items():
                if v == "":
                    json[k] = None
            params["json"] = json
        return json

    def build_query(self, params):
        return params.get("query")

    def build_path(self, params):
        path = params.get("path", "")
        params["path"] = self.path + path
        return params["path"]

    def build_url(self, params):
        path = params.get("path", "")
        return self.url +"/" + path

class ISSFileAccess: 

    def __init__(self, path):
        #: Member value containing the root path of the namespace
        self.path = self.__init_path(path)

    @staticmethod
    def __init_path(path):
        if not isinstance(path, str) or len(path) == 0:
            raise ValueError("path must be initialized as a non empty string")
        path = join(ISS_SKILL_PATH, path)

        if not isdir(path):
            os.makedirs(path)
        return path

    def open(self, filename, mode):
       
        file_path = join(self.path, filename)
        return open(file_path, mode)

    def check_if_exists(self, filename):
    
        return os.path.exists(join(self.path, filename))
    
   

class ISSApi(Api):
   

    def __init__(self):
        super(ISSApi,self).__init__('iss')
        
    def get_iris_result(self,data):   
   

        return self.request({
            "method": "POST",
            "path": "/iris/predict",
            "json": {"IrisSpecies":data}
        })
    
    def get_delivery_result(self,vehicle_num,current_postalCode):   

        return self.request({
            "method": "POST",
            "path": "/delivery/address",
            "json": {"vehicle_num":vehicle_num,
                     "current_postalCode":current_postalCode
                    }
        })


class ISSProjectSkill(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__("ISSProjectSkill")
        self.learning = True

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')
        self.iss_api= ISSApi()
        self.iss_input=ISSFileAccess("input")

 
    @intent_handler('project.info.intent')
    def handle_project_info_intent(self, message):
        """ This is a Padatious intent handler.
        It is triggered using a list of sample phrases."""
        self.speak_dialog("project.info")
       
    
    @intent_handler(IntentBuilder("").require("Iris").build())                    
    def handle_test_iris_intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        #self.log.info(self.file_system.path)
        if self.iss_input.check_if_exists("iris_input.json"):        
            input_param=dict() 
            with self.iss_input.open('iris_input.json', 'r') as f:
                try:
                    input_param=json.load(f)
                    #self.log.info(input_param)
                except Exception as e:
                    self.log.exception("Error: {0}".format(e))
                    self.speak_dialog("input.exception",{"project":"iris"},wait=True)
                    raise                
                if isinstance(input_param["sepal_length"], float) !=True:
                    self.speak('input sepal length is not a float',wait=True)
                elif isinstance(input_param["sepal_width"], float) !=True:
                    self.speak('input sepal width is not a float',wait=True)
                elif isinstance(input_param["petal_length"], float) !=True:
                    self.speak('input petal length is not a float',wait=True) 
                elif isinstance(input_param["petal_width"], float) !=True:
                    self.speak('input petal width is not a float',wait=True)
                else:
                    
                    self.speak_dialog("start.load.input",{"project":"iris"},wait=True)
                    try:     
                        self.speak_dialog("iris.input",data={"sepal_length":input_param["sepal_length"],
                                            "sepal_width":input_param["sepal_width"],
                                            "petal_length":input_param["petal_length"],
                                            "petal_width":input_param["petal_width"]},wait=True)
                    except Exception as e:
                        self.log.exception("Error: {0}".format(e))
                        self.speak_dialog("input.exception",{"project":"iris"},wait=True)
                        raise
                    
                    try:
                        self.speak_dialog("start.call.api",{"project":"iris"},wait=True)
                        #self.log.info(json.dumps(input_param))
                        result=self.iss_api.get_iris_result(json.dumps(input_param))
                        if result is not None or result != '':       
                            self.speak_dialog("iris.result",data={"prediction": result["prediction"],"probability":result["probability"]},wait=True)
                            self.speak_dialog("change.input",{"project":"iris"},wait=True)
                        else:
                            self.speak_dialog("no.result",{"project":"iris"})
                    except Exception as e:
                        self.log.exception("Error: {0}".format(e))
                        self.speak_dialog("api.exception",{"project":"iris"},wait=True)
                        raise
        else:
            self.speak_dialog("not.find.file",{"project":"iris"},wait=True)
  
    @intent_handler(IntentBuilder("").require("Delivery").build())    
    def handle_test_delivery_intent(self, message):        
        if self.iss_input.check_if_exists("delivery_input.json"):        
            input_param=dict() 
            with self.iss_input.open('delivery_input.json', 'r') as f:
                try:
                    input_param=json.load(f)
                    #self.log.info(input_param)           
                    #test=re.match(r'[0-9]','w')
                    #self.log.info(test)
                    #test=re.match(r'\d{6}','560324')
                    #self.log.info(test)
                except Exception as e:
                    self.log.exception("Error: {0}".format(e))
                    self.speak_dialog("input.exception",{"project":"delivery"},wait=True)
                    raise  
                if isinstance(input_param["vehicle_num"], str) !=True:
                    self.speak('Input vehicel number is not a string',wait=True)
                elif re.search(r'[0-9]{6}',str(input_param["current_postalCode"]))==None:
                    self.speak('Input postal code must be 6 digit number',wait=True)
                else:
                    self.speak_dialog("start.load.input",{"project":"delivery"},wait=True)
                    try:        
                        self.speak_dialog("delivery.input",data={"vehicle_num":input_param["vehicle_num"],
                                              "current_postalCode":input_param["current_postalCode"]
                                              },wait=True)
                    except Exception as e:
                        self.log.exception("Error: {0}".format(e))
                        self.speak_dialog("input.exception",{"project":"delivery"},wait=True)
                        raise
                                                                 
                    try:
                        self.speak_dialog("start.call.api",{"project":"delivery"},wait=True)
                        result=self.iss_api.get_delivery_result(input_param["vehicle_num"],input_param["current_postalCode"])
                        if result is not None or result != '':       
                            self.speak_dialog("delivery.result",{"result":result},wait=True)
                            self.speak_dialog("change.input",{"project":"delivery"},wait=True)
                        else:
                            self.speak_dialog("no.result",{"project":"delivery"},wait=True)
                    except Exception as e:
                        self.log.exception("Error: {0}".format(e))
                        self.speak_dialog("api.exception",{"project":"delivery"},wait=True)
        else:
            self.speak_dialog("not.find.file",{"project":"delivery"},wait=True)
      
       
                    
   
    
    def stop(self):
        pass        
    


def create_skill():
    return ISSProjectSkill()
