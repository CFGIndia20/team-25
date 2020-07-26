# Team-25 Janahelper
A proposed solution for the challenge posed by Janaagraha NPO. The minimum viable prototype consists of a single step text submission to raise an issue, automatic categorization through a trained ML model and the one which can work for several Backend API for requests.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

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

