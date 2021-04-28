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
#import pandas as pd
import git
import shutil


class LoadProject(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()
        self.learning = True
        self.projectlist=[]
        self.projectselect=''
        self.basepath='~/mycroft-core/skills'
        self.gitpath='https://github.com/twming/'
        self.loadproject()
 

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')

    def loadproject(self):
        #self.projectlist=pd.read_csv('~/mycroft-core/skills/mycroft-loadproject/projectlist.txt',header=None,sep=',').values.tolist()
        with open('/opt/mycroft/skills/mycroft-loadproject/projectlist.txt') as f:
            self.projectlist=[line.rstrip().split(',') for line in f]

    @intent_handler(IntentBuilder('showprojIntent').require('showproj'))
    def handle_showproj_intent(self, message):
        if self.projectlist==[]:
            self.speak_dialog('There is no project.')
        else:     
            for item in self.projectlist:
                self.log.info("Project :"+item[0]+", Path :"+item[1])
            self.speak_dialog('Here is all the project.')

    @intent_handler('selectproj.intent')
    def handle_selectproj_intent(self, message):
        item=message.data['number']
        if item=='one' or item=='1':
            self.projectselect=self.projectlist[0][1]
            self.speak_dialog('project one selected')
        elif item=='two' or item=='2':
            self.projectselect=self.projectlist[1][1]
            self.speak_dialog('project two selected')
        elif item=='three' or item=='3':     
            self.projectselect=self.projectlist[2][1]
            self.speak_dialog('project three selected')
        self.log.info("Project :"+self.projectselect)

    @intent_handler(IntentBuilder('installprojIntent').require('installproj'))
    def handle_installproj_intent(self, message):
        if self.projectselect=='':
            self.speak_dialog('Please select a project.')
        else:  
            git.Git(self.basepath).clone(self.gitpath+self.projectselect+'.git')
            self.speak_dialog('project install complete')
            self.log.info("project install complete")

    #same as using 'uninstall <project>'
    @intent_handler(IntentBuilder('removeprojIntent').require('removeproj'))
    def handle_removeproj_intent(self, message):
        shutil.rmtree('/opt/mycroft/skills/'+self.projectselect)
        self.speak_dialog('project remove')

    def stop(self):
        pass


def create_skill():
    return LoadProject()
