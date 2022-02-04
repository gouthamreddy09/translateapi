##MAKE A JSON OBJECT TO STORE COUNTRY WISE LANG LIST, CREATE A SPARSE LANG MATRIX TO ASSESS SIMILARITY

import json

d={}
langs={'auto-detect': 'Auto-detect',
  'af': 'Afrikaans',
  'am': 'Amharic',
  'ar': 'Arabic',
  'as': 'Assamese',
  'az': 'Azerbaijani',
  'bg': 'Bulgarian',
  'bn': 'Bangla',
  'bs': 'Bosnian',
  'ca': 'Catalan',
  'cs': 'Czech',
  'cy': 'Welsh',
  'da': 'Danish',
  'de': 'German',
  'el': 'Greek',
  'en': 'English',
  'es': 'Spanish',
  'et': 'Estonian',
  'fa': 'Persian',
  'fi': 'Finnish',
  'fil': 'Filipino',
  'fj': 'Fijian',
  'fr': 'French',
  'fr-CA': 'French (Canada)',
  'ga': 'Irish',
  'gu': 'Gujarati',
  'he': 'Hebrew',
  'hi': 'Hindi',
  'hr': 'Croatian',
  'ht': 'Haitian Creole',
  'hu': 'Hungarian',
  'hy': 'Armenian',
  'id': 'Indonesian',
  'is': 'Icelandic',
  'it': 'Italian',
  'iu': 'Inuktitut',
  'ja': 'Japanese',
  'kk': 'Kazakh',
  'km': 'Khmer',
  'kmr': 'Kurdish (Northern)',
  'kn': 'Kannada',
  'ko': 'Korean',
  'ku': 'Kurdish (Central)',
  'lo': 'Lao',
  'lt': 'Lithuanian',
  'lv': 'Latvian',
  'mg': 'Malagasy',
  'mi': 'Maori',
  'ml': 'Malayalam',
  'mr': 'Marathi',
  'ms': 'Malay',
  'mt': 'Maltese',
  'mww': 'Hmong Daw',
  'my': 'Myanmar',
  'nb': 'Norwegian',
  'ne': 'Nepali',
  'nl': 'Dutch',
  'or': 'Odia',
  'otq': 'Querétaro Otomi',
  'pa': 'Punjabi',
  'pl': 'Polish',
  'prs': 'Dari',
  'ps': 'Pashto',
  'pt': 'Portuguese (Brazil)',
  'pt-PT': 'Portuguese (Portugal)',
  'ro': 'Romanian',
  'ru': 'Russian',
  'sk': 'Slovak',
  'sl': 'Slovenian',
  'sm': 'Samoan',
  'sq': 'Albanian',
  'sr-Cyrl': 'Serbian (Cyrillic)',
  'sr-Latn': 'Serbian (Latin)',
  'sv': 'Swedish',
  'sw': 'Swahili',
  'ta': 'Tamil',
  'te': 'Telugu',
  'th': 'Thai',
  'ti': 'Tigrinya',
  'tlh-Latn': 'Klingon (Latin)',
  'tlh-Piqd': 'Klingon (pIqaD)',
  'to': 'Tongan',
  'tr': 'Turkish',
  'ty': 'Tahitian',
  'uk': 'Ukrainian',
  'ur': 'Urdu',
  'vi': 'Vietnamese',
  'yua': 'Yucatec Maya',
  'yue': 'Cantonese (Traditional)',
  'zh-Hans': 'Chinese Simplified',
  'zh-Hant': 'Chinese Traditional'}

with open('country_languages.json') as f:
    d=json.load(f)

similar_languages={}

tmp=[]

for i in langs.keys():
    tmp=[]
    for j in d:
        if (langs[i] in j['languages']):
            print(langs[i])
            print(j['country'])
            tmp.append(langs[i])
    #print(tmp)
    if j['country'] in similar_languages.keys():
        similar_languages[j['country']].append(tmp)
    else:
        similar_languages[j['country']]=['']
    #print(similar_languages)
print(similar_languages)

