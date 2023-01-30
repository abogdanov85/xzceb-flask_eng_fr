"""Main script for translator functions"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#authenticator = IAMAuthenticator(apikey)
authenticator = IAMAuthenticator('sHstYOS27d8YVZT1nIJLomopKAY7M13YD3xOy6x5rag4')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    """English to French"""
    if english_text == '':
        return 'Error: The input text is empty'
    else:
        french_text = language_translator.translate(text=english_text,
        model_id='en-fr').get_result()
        return french_text['translations'][0]['translation']

def french_to_english(french_text):
    """French to English"""
    if french_text == '':
        return 'Error: The input text is empty'
    else:
        english_text = language_translator.translate(text=french_text,
        model_id='fr-en').get_result()
        return english_text['translations'][0]['translation']

#print(englishToFrench('I go home'))
#print(englishToFrench(''))
#print(frenchToEnglish('Je vais à la maison'))
#print(frenchToEnglish(''))
