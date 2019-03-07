# Dr. Naive Bayes API

A Flask based API for a naive baysian network.

## Running Locally

To run the server locally, with pip is installed, run the commands below:

```sh
git clone https://github.com/paulofaria/dr-naive-bayes
cd dr-naive-bayes
pip install -r requirements.txt
FLASK_APP=server.py flask run
```

The server will take a while to start running since it will first load the model from `hw4_data_long.csv` which requires a lot of memory.

## Deployment

Deploy this application to heroku. Be sure to select a Performance-L dyno since the application requires a lot of memory. Remember to set the number of dynos to zero after using the app so you don't get charged $500 at the end of the month.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Requests

The API has a single endpoint `GET /query`. Pass the findings in the URL query, like below:

[http://localhost:5000/query?nausea=1&vomiting=1](http://localhost:5000/query?nausea=1&vomiting=1)

The response will be a sorted JSON array of objects containing the top 10 most probable diseases. Each object contains the name of the disease and its occurence probability. Below is the JSON response for the query above:

```json
[
  {
    "disease": "pancreatitis",
    "probability": 0.22424483840873
  },
  {
    "disease": "chronic kidney failure",
    "probability": 0.13489728560525
  },
  {
    "disease": "dehydration",
    "probability": 0.12967519162096
  },
  {
    "disease": "ketoacidosis diabetic",
    "probability": 0.12133618281954
  },
  {
    "disease": "cholelithiasis",
    "probability": 0.091265402699362
  },
  {
    "disease": "ulcer peptic",
    "probability": 0.070750324618138
  },
  {
    "disease": "tricuspid valve insufficiency",
    "probability": 0.063106121874109
  },
  {
    "disease": "gastritis",
    "probability": 0.055518950878351
  },
  {
    "disease": "migraine disorders",
    "probability": 0.034224526012261
  },
  {
    "disease": "diabetes",
    "probability": 0.032932097638626
  }
]
```
