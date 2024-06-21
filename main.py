import requests

# Base URL for the FunTranslations API
BASE_URL = 'https://api.funtranslations.com/translate/'

# Dictionary of available translation endpoints
TRANSLATIONS = {
    'yoda': 'yoda.json',
    'shakespeare': 'shakespeare.json',
    'minion': 'minion.json',
    'pirate': 'pirate.json',
    'starwars': 'sith.json',
    'dothraki': 'dothraki.json',
    'valyrian': 'valyrian.json',
    'mandalorian': 'mandalorian.json',
    'groot': 'groot.json',
    'braille': 'braille.json',
    'asian': 'asian-accent.json',
    'russian': 'russian-accent.json',
    'irish': 'irish.json',
    'british': 'british.json',
    'german': 'german-accent.json',
    'emoji': 'emoji.json'
}

def translate_text(text, language):
    if language not in TRANSLATIONS:
        raise ValueError(f"Unsupported language: {language}. Supported languages are: {list(TRANSLATIONS.keys())}")
    
    url = BASE_URL + TRANSLATIONS[language]
    payload = {
        'text': text
    }
    
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        return response.json()['contents']['translated']
    else:
        return f"Error: Unable to translate text. {response.json().get('error', {}).get('message', 'Unknown error')}"

if __name__ == "__main__":
    text = input("Enter the text you want to translate: ")
    language = input("Enter the language (yoda, shakespeare, minion, pirate, starwars, dothraki, valyrian, mandalorian, groot, braille, asian, russian, irish, british, german, emoji): ").lower()

    try:
        translated_text = translate_text(text, language)
        print(f"Translated text: {translated_text}")
    except ValueError as e:
        print(e)
