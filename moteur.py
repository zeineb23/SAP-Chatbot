# -*- coding: utf-8 -*-
"""Moteur.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GZDR24IT-GYTDbZaUFXpfaS8cfAYo32Y

**Data Scraping**
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install selenium==4.10.0
# %pip install pandas
# %pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urllib.request import Request, urlopen
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import warnings
import json
import time
import os
import requests

def driversetup():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("lang=en")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=service, options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    return driver

def pagesource(url, driver):
    driver = driver
    driver.get(url)
    soup = BeautifulSoup(driver.page_source)
    questions = [x.get("href") for x in soup.findAll('a') if str(x.get("href")).startswith('/questions/')][1:]
    return questions

"""**Questions from website**"""

tags = [
    "99724818299614502762190973596969",
    "416658401661843526040169665289086",
    "876619786935845126962162607976597",
    "773921536755532122004239005965168",
    "250948378054223096392454848767354",
    "182542228769759641292999239253882",
    "859834545111167391953063734572784",
    "212358834767912649313917434384826",
    "410250962940517507034023885688755",
    "443595830163800786360189759964915",
    "188663251671469173336120566262897",
    "132949817163443344955330185779754",
    "bd524d9b-1ee4-452d-a5b4-c25520976179",
    "0c9ec02c-46fe-498e-a301-66c5a13461e9",
    "01200615320800000636"
]

questions = []
for tag in tags:
    print("tag:", tag)
    for i in range(1, 130):
            url = f"https://answers.sap.com/tags/{tag}?page={i}&pageSize=15&sort=active&filter=accepted"
            response = requests.get(url)
            # Parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")
            question = soup.select("li.dm-contentListItem a[href^='/questions/']")
            if len(question) == 0: break
            else:
                questions.extend(question)

len(questions)

"""***Question answering with top 5  similar questions ***"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

question = input("What is your question ")
cosinesim=[]
for quest in questions:
  # Create the TF-IDF vectorizer
  vectorizer = TfidfVectorizer()

  # Fit and transform the data
  tfidf_matrix = vectorizer.fit_transform([question, quest.text.strip()])
  # Calculate cosine similarity
  similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
  cosinesim.append((similarity, "https://answers.sap.com"+quest["href"]))


sorted_data = sorted(cosinesim, key=lambda x: x[0], reverse=True)

for i in range(5) :
  print(sorted_data[i][0]," the question : ",sorted_data[i][1])
