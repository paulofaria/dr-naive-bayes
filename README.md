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

```
GET /query?nausea=1&vomiting=1
```
