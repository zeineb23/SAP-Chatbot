# SAP Chatbot

SAP Chatbot is a project aimed at building a chatbot system that leverages natural language processing techniques to provide answers to frequently asked questions (FAQs) related to SAP software.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Description

The SAP Chatbot project consists of two Jupyter notebooks:

1. **Moteur.ipynb**: This notebook implements a web scraping mechanism to extract frequently asked questions (FAQs) related to SAP from various sources. It utilizes the pipeline question-answering model from the Transformers library to provide the top 5 similar questions for a user's input question.

2. **answering_pptx.ipynb**: This notebook is responsible for extracting answers from PowerPoint presentations (PPTX) using the pipeline question-answering model from the Transformers library.

## Installation

To run the notebooks locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/zeineb23/SAP-Chatbot.git
```
2.Navigate to the project directory:
```bash
cd SAP-Chatbot
```
3.Install the required dependencies:
```bash
pip install -r requirements.txt
```
## **Usage** 

To use the SAP Chatbot notebooks, follow the instructions provided in each notebook. These notebooks provide step-by-step guides on how to scrape FAQs, extract answers from PowerPoint presentations, and use the pipeline question-answering model from the Transformers library.

## **Contributing**
If you'd like to contribute to the SAP Chatbot project, please follow these guidelines:

1.Fork the repository
2.Create a new branch (git checkout -b feature)
3.Make your changes and commit them (git commit -am 'Add new feature')
4.Push to the branch (git push origin feature)
5.Create a new Pull Request

Please ensure that your contributions align with the project's goals and coding standards.
