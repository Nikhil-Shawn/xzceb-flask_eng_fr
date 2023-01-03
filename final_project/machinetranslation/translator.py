import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('hBlj6yAMvoARaCuyDZLjQQpSbFam-Yzl4tkDr3qqFBGc')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/c337aea4-b88d-4490-bd53-e463221e9a94')

def englishToFrench(englishText):
    translation = language_translator.translate(text=englishText, model='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    translation = language_translator.translate(text=frenchText, model="fr-en").get_result()
    englishText = translation['translations'][0]['translation']
    return englishText 
