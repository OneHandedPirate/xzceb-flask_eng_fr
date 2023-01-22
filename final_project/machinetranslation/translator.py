import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

translator.set_service_url(url)

def english_to_french(english_text):
    if english_text:
        french_text = translator.translate(text=english_text, model_id='en-fr')\
            .get_result()['translations'][0]['translation']
    else:
        return 'You have entered an empty string'
    return french_text

def french_to_english(french_text):
    if french_text:
        english_text = translator.translate(text=french_text, model_id='fr-en')\
            .get_result()['translations'][0]['translation']
    else:
        return 'Vous avez entré une chaîne vide'
    return english_text
