### [ Practice Module ] Project Submission Template: Github Repository & Zip File

**[ Naming Convention ]** CourseCode-StartDate-BatchCode-TeamName-ProjectName.zip

* **[ MTech Thru-Train Group Project Naming Example ]** IRS-PM-2020-01-18-IS02PT-GRP-AwsomeSG-HDB_BTO_Recommender.zip

* **[ MTech Stackable Group Project Naming Example ]** IRS-PM-2020-01-18-STK02-GRP-AwsomeSG-HDB_BTO_Recommender.zip

[Online editor for this README.md markdown file](https://pandao.github.io/editor.md/en.html "pandao")

---

### <<<<<<<<<<<<<<<<<<<< Start of Template >>>>>>>>>>>>>>>>>>>>

---

## SECTION 1 : PROJECT TITLE
## MyCroft Discovery and Applications

<img src="SystemCode/clips/static/hdb-bto.png"
     style="float: left; margin-right: 0px;" />

---

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
Singapore ranks amongst countries with the highest population density in the world. In a bid to have firm control over long term urban planning, the Singapore government came up with the “Built to Order” (abbreviated BTO) initiative back in 2001. These are new Housing Development Board (HDB) flats tightly controlled by their eligibility and quantity released every year. In more recent years, the modern BTO scheme in Singapore requires a waiting period of 3-4 years, and is generally targeted at young Singaporean couples looking to purchase their first property and set up a family. Nationality and income ceilings are some of the broad filters that determine one’s eligibility for the highly sought after projects. 


Our team, comprising of 6 young Singaporeans, all hope to be property owners one day. Many of our peers opt for BTO flats due to their affordability, existence of financial aid from the government, as well as their resale value. However, there often exists a knowledge gap for these young couples during the decision making process and they end up making potentially regretful decisions. We would like to bridge this knowledge gap, and have hence chosen to base our project on creating a recommender system for BTO flats, utilizing the data from recent launches in Tampines, Eunos, Sengkang and Punggol. 


Using the techniques imparted to us in lectures, our group first set out to build a sizeable knowledge base via conducting an interview and administering a survey. While building the system, we utilized tools such as Java to scrape real time data from HDB website and transform it into a database, CLIPS to synthesize the rule based reasoning process, and Python to integrate it into an easy to use UI for the everyday user. To add icing on the cake, we even hosted the system on a website so that the everyday user can access it through the click of a link.


Our team had an amazing time working on this project, and hope to share our insights with everyone. Despite a focus on BTO flats, we would recommend it for everybody interested in understanding property market trends for residence or investment purposes. There truly are a wide array of factors behind the decision to invest in a property, and we only wish there was more time to work on the scope and scale of the project. 

---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Name  | Student ID  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| LI XIAO XIA   | A1234567A | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567A@nus.edu.sg |
| YANG YANG     | A1234567B | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567B@gmail.com |
| TAN WOEI MING | A0229974L | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| twming2001@yahoo.com.sg |
| JIANG AI GUO  | A1234567D | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567D@yahoo.com |
| ANG JENN NING | A1234567E | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567E@qq.com |

---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

[![MyCroft Application](http://img.youtube.com/vi/AQxaRUFnKfw/0.jpg)](https://youtu.be/AQxaRUFnKfw "MyCroft Application")

---

## SECTION 5 : USER GUIDE

`Refer to MDDS_User_Guide file.`

### [ 1 ] To run the system using iss-vm

> download pre-built virtual machine from http://bit.ly/iss-vm

> start iss-vm

> open terminal in iss-vm

> $ git clone https://github.com/telescopeuser/Workshop-Project-Submission-Template.git

> $ source activate iss-env-py2

> (iss-env-py2) $ cd Workshop-Project-Submission-Template/SystemCode/clips

> (iss-env-py2) $ python app.py

> **Go to URL using web browser** http://0.0.0.0:5000 or http://127.0.0.1:5000

### [ 2 ] To run the system in other/local machine:
### Install additional necessary libraries. This application works in python 2 only.

> $ sudo apt-get install python-clips clips build-essential libssl-dev libffi-dev python-dev python-pip

> $ pip install pyclips flask flask-socketio eventlet simplejson pandas

---
## SECTION 6 : PROJECT REPORT

1. Project Overview
2. Business Perspective
3. Market Research
4. Project Objectives
5. System Specification
5.1 Mycroft Architecture
5.2 Mycroft Data Privacy Handling
5.3 Mycroft Home-UI Setting
5.4 Mycroft Linux Installation and Application
5.5 Picroft Installation and Application
5.6 Mycroft Personal Selene Server setup
5.7 Mycroft Skill Management
5.8 Use Cases Specification
6. System Implementation
6.1 Mycroft Home Setup
6.2 Mycroft Linux Installation and Configuration
6.3 Mycroft Picroft Config
6.4 Private Skill Create and Run
6.5 Public Skill Create and Run
6.6 Mycroft Personal Server setup
6.7 Use Cases Implementation
7.  Project Conclusions
- Appendix: Project Proposal
- Appendix: Mapped System Functionalities against MR, RS, CGS	35
- Appendix: Installation and User Guide
- Appendix: References

---
## SECTION 7 : MISCELLANEOUS

`Refer to Github Folder: Miscellaneous`

---

### <<<<<<<<<<<<<<<<<<<< End of Template >>>>>>>>>>>>>>>>>>>>

---

**This [Machine Reasoning (MR)](https://www.iss.nus.edu.sg/executive-education/course/detail/machine-reasoning "Machine Reasoning") course is part of the Analytics and Intelligent Systems and Graduate Certificate in [Intelligent Reasoning Systems (IRS)](https://www.iss.nus.edu.sg/stackable-certificate-programmes/intelligent-systems "Intelligent Reasoning Systems") series offered by [NUS-ISS](https://www.iss.nus.edu.sg "Institute of Systems Science, National University of Singapore").**

**Lecturer: [GU Zhan (Sam)](https://www.iss.nus.edu.sg/about-us/staff/detail/201/GU%20Zhan "GU Zhan (Sam)")**

[![alt text](https://www.iss.nus.edu.sg/images/default-source/About-Us/7.6.1-teaching-staff/sam-website.tmb-.png "Let's check Sam' profile page")](https://www.iss.nus.edu.sg/about-us/staff/detail/201/GU%20Zhan)

**zhan.gu@nus.edu.sg**
