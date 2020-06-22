from src import get_logger
import bs4
import spacy

logger = get_logger(name=None)

'''
Load pretrained statistical english model. More info here https://spacy.io/models/en#en_core_web_sm
'''
sp = spacy.load('en_core_web_sm')


def _filter_out_code(element):
    logger.error(element)


def get_markup_texts(body):
    '''
    Remove markup, remove code snippets
    Remove code and pre tags with code inside
    :param body:
    :return:
    '''
    bs = bs4.BeautifulSoup(body, 'html.parser')
    for tag in bs.find_all(['code', 'pre']):
        tag.replace_with('')
    return bs.get_text()


def get_lemmas(text):
    '''
    Convert text into their lemmas and remove punctuation
    :param text:
    :return:
    '''

    sentence = sp(text)
    return [token.lemma_ for token in sentence if not token.is_punct and not token.lemma_.isnumeric()]


def remove_short_and_numeric_words(words):
    return [word for word in words if len(word) > 2 and not word.isnumeric()]


def remove_stop_words(tokens):
    return [token for token in tokens if token not in sp.Defaults.stop_words]

