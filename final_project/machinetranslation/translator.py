import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')

#print('test')

def englishToFrench(englishText):
    if englishText == '':
        return 'Error: The input text is empty'
    else:
        frenchText = language_translator.translate(text=englishText,
        model_id='en-fr').get_result()
        return frenchText['translations'][0]['translation']

def frenchToEnglish(frenchText):
    if frenchText == '':
        return 'Error: The input text is empty'
    else:
        englishText = language_translator.translate(text=frenchText,
        model_id='fr-en').get_result()
        return englishText['translations'][0]['translation']

#print(englishToFrench('I go home'))
#print(englishToFrench(''))
#print(frenchToEnglish('Je vais à la maison'))
#print(frenchToEnglish(''))