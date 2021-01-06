# Team-25 Janahelper
A proposed solution for the challenge posed by Janaagraha NPO. The minimum viable prototype consists of a single step text submission to raise an issue, automatic categorization through a trained ML model and the one which can work for several Backend API for requests.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. <br/>

Python 3 has been used for this project.

### Clone
Clone this repo to your local machine using [GitHub](https://github.com/CFGIndia20/team-25.git)

### Setup
Run the following command to install all the dependencies and get the environment ready: <br/> 

```bash
pip install -r requirements.txt
```

## Features
* A single step text submission to raise an issue at hand
* The issue is automatically categorized through a trained ML model (detailed machine learning manual present inside team-25/API/classification/ML Manual.pdf )
* A one stop Backend API for requests
* Removes the barrier of language that is, it allows users to post issues in their preferred language (Googletrans api used)
* Eases integration with social media platforms too (telegram bot is what used here)

## Usage

To run the project in your local machine, follow the steps given below.

* Go to team-25 folder
* Then to move to api folder, run: <br/> cd api
* Run the command: <br/> python app.py
* Come out of the api folder, run: <br/> cd ../
* Then to move to client folder, run: <br/> cd client
* On a separate terminal, run the command: <br/> python app.py

This will make the api to be in a functioning state.

### Test Case

* Input Format Example:<br/>
```json
{
    "complaint_text":"Potholes near my locality",
    "cdlat":"35.46789",
    "cdlon":"45.678"
}
```
* Successful Output Example: <br/>
```json
{"categories": "Mobility - Roads, Footpaths and Infrastructure", "location": {"latitude": "35.46789", "longitude":
"45.678"}}
```
* Erroneous Output Example: </br>
```json
Redirecting to the same location or Error 404
```

### Built With

1. Frontend:
   - Bootstrap
2. API:
   - Flask
3. ML Model:
   - TensorFlow
   - Keras
   - NLTK
4. Social Media Integration
   - Telegram Bot API

### Roadmap

* Image processing <br/>
For now our machine learning model does the text-processing to get the keywords from the text complaint to respond with the complaint category, which can be extended towards image processing. We will then be able to get a more accurate complaint category which would ease the process.

* Feedback from the user <br/>
Once the complaint status for a user turns out to be done or solved in the database which gets updated in every 5 minutes then the user will receive an email to fill out a survey as a part of the feedback collection system.

* Voice input for raising an issue <br/>
Since as per the current solution the user needs to raise an issue in the text format supported in several languages, to ease the process and for a change we can incorporate the input taking through voice.


##### The code ("Code") in this repository was created solely by the student teams during a coding competition hosted by JPMorgan Chase Bank, N.A. ("JPMC").						JPMC did not create or contribute to the development of the Code.  This Code is provided AS IS and JPMC makes no warranty of any kind, express or implied, as to the Code,						including but not limited to, merchantability, satisfactory quality, non-infringement, title or fitness for a particular purpose or use.