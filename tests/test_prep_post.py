from so.preparation import *


def test_get_markup_texts():
    body = '''<p>I've got a menu in Python. That part was easy. I'm using <code>raw_input()</code>'''
    text = get_markup_texts(body)
    assert text == '''I\'ve got a menu in Python. That part was easy. I\'m using '''


def test_get_lemmas():
    body = '''I guess what I'm looking for is a summary and list of pros and cons for each implementation. At least 2'''
    lemmas = get_lemmas(body)
    assert lemmas == ['-PRON-', 'guess', 'what', '-PRON-', 'be', 'look', 'for', 'be', 'a', 'summary', 'and', 'list',
                      'of', 'pro', 'and', 'con', 'for', 'each', 'implementation', 'at', 'least']

    body = '''I'm you are he is she is we are they are'''
    lemmas = get_lemmas(body)
    assert lemmas == ['-PRON-', 'be', '-PRON-', 'be', '-PRON-', 'be', '-PRON-', 'be', '-PRON-', 'be', '-PRON-', 'be']


def test_remove_stop_words():
    words = ['I', 'like', 'the', 'fact', 'that', 'it', 'spacy', 'is', 'easy', '.']
    stop_words_removed = remove_stop_words(words)
    assert stop_words_removed == ['I', 'like', 'fact', 'spacy', 'easy', '.']
