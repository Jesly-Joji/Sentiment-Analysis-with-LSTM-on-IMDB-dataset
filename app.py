#IMPORT STATEMENTS
import torch
import requests
from flask import Flask

#Get the model from github
url="https://raw.githubusercontent.com/Jesly-Joji/Sentiment-Analysis-with-LSTM-on-IMDB-dataset/main/sentiment_analysis_lstm.pt"

response=request.get(url)

with open("model.pt","wb") as file:
  file.write(response.context)

#Load the model
model=torch.load("model.pt")

  
