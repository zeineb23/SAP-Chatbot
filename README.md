# SAP Chatbot

SAP Chatbot is a project aimed at building a chatbot system that leverages natural language processing techniques to provide answers to frequently asked questions (FAQs) related to SAP software.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

The SAP Chatbot project consists of two Jupyter notebooks:

1. **Moteur.ipynb**: This notebook implements a web scraping mechanism to extract frequently asked questions (FAQs) related to SAP from various sources. It utilizes the pipeline question-answering model from the Transformers library to provide the top 5 similar questions for a user's input question.

2. **answering_pptx.ipynb**: This notebook is responsible for extracting answers from PowerPoint presentations (PPTX) using the pipeline question-answering model from the Transformers library.

## Installation

To run the notebooks locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your_username/SAP-Chatbot.git
