import json
from pronouncing import rhymes, syllable_count, phones_for_word, search_stresses, stresses
from random import choice, sample
from grammatical_types import (
    Noun, 
    TransitiveVerb, 
    IntransitiveVerb,
    Adjective,
    Adverb,
    Meter
)

def get_words():
    with open("words.json") as datafile:
        words = json.load(datafile)
    words['nouns'] = set([Noun(w) for w in words['nouns']])
    words['transitive_verbs'] = set([TransitiveVerb(w) for w in words['transitive_verbs']])
    words['intransitive_verbs'] = set([IntransitiveVerb(w) for w in words['intransitive_verbs']])
    words['adjectives'] = set([Adjective(w) for w in words['adjectives']])
    words['adverbs'] = set([Adverb(w) for w in words['adverbs']])
    return words

words = get_words()

word_types = {
    Noun: "nouns",
    TransitiveVerb: "transitive_verbs",
    IntransitiveVerb: "intransitive_verbs",
    Adjective: "adjectives",
    Adverb: "adverbs"
}

def random_word(word_type, count=1, rhymes_with=None, meter=None, syllables=None):
    """Returns one or more randomly-chosen words. 

        >>> random_word(Noun)
        'pineapple'
        >>> random_word(Adjective, syllables=4)
        'methodical'
        >>> random_word(Adverb, count=3)
        ['flatly', 'gravely', 'gently']
        >>> random_word(Noun, count=4, rhymes_with="sand")
        ['grand', 'command', 'band', 'brand']

    Args:
        word_type (type): `Noun`, `TransitiveVerb`, `IntransitiveVerb`, `Adjective`, or `Adverb`.
        count (int): Optional, default `1`. Number of words to return. 
        rhymes_with (str): Optional. When provided, the word(s) must rhyme. 
        meter (Meter): Optional. When provided, the word(s) must match the given meter.
        syllables (int): Optional. When provided, the word(s) must have the given number of syllables.

    Returns:
        word_type: Or a list of `word_type` when count is greater than 1.
    """
    if word_type not in word_types.keys():
        raise TypeError("random words are not supported for type {}".format(word_type))
    assert isinstance(count, int)
    assert rhymes_with is None or isinstance(rhymes_with, str)
    assert meter is None or isinstance(meter, Meter)     
    assert syllables is None or isinstance(syllables, int)

    conditions = []
    matches = words[word_types[word_type]]
    if rhymes_with:
        conditions.append("rhymes with " + rhymes_with)
        matches = matches.intersection(map(word_type, rhymes(rhymes_with)))
    if meter:
        conditions.append("has meter " + meter)
        matches = matches.intersection(map(word_type, search_stresses('^' + meter + '$')))
    if syllables:
        conditions.append("has {} syllables".format(syllables))
        matches = matches.intersection(word for word in matches if count_syllables(word) == syllables)
    if len(matches) < count:
        target = "a " + word_type.__name__ if count == 1 else str(count) + ' ' + word_type.__name__ + 's'
        raise NoWordError("Couldn't find {} with conditions: {}".format(
             target, " and ".join(conditions)))
    return sample(tuple(matches), count) if count > 1 else choice(tuple(matches))

def rhyming_pair(first_word_type, second_word_type, meter=None, syllables=None, attempts=20):
    """Returns a pair of words which rhyme.

        >>> rhyming_pair(Noun, Adjective, syllables=2)
        ('traffic', 'graphic')
        >>> rhyming_pair(TransitiveVerb, IntransitiveVerb, meter="10")
        ('fumble', 'grumble')

    Args:
        first_word_type (type): `Noun`, `TransitiveVerb`, `IntransitiveVerb`, `Adjective`, or `Adverb`.
        second_word_type (type): `Noun`, `TransitiveVerb`, `IntransitiveVerb`, `Adjective`, or `Adverb`.
        meter (Meter): Optional. A stress pattern for syllables like "01" (ad MIRE) or "100" (SYM phon y) 
        syllables (int): Optional. The number of syllables in each word.
        attempts (int): Optional, default is `20`. Number of times to try before giving up. 
            This function chooses the first word first, and then looks for a matching second word. If there
            is no match, we need to throw away the first word and try again. Without a limit on the number
            of attempts, this function would potentially search forever, locking up your program. 
            The default value of `attempts` should be fine, but you can tune it if you want. 

    Returns: 
        (first_word_type, second_word_type)
    """
    if first_word_type not in word_types.keys():
        raise TypeError("random words are not supported for type {}".format(first_word_type))
    if second_word_type not in word_types.keys():
        raise TypeError("random words are not supported for type {}".format(second_word_type))
    assert meter is None or isinstance(meter, Meter)     
    assert syllables is None or isinstance(syllables, int)
    assert isinstance(attempts, int)

    for i in range(attempts):
        try:
            first = random_word(first_word_type, meter=meter, syllables=syllables)
            second = random_word(second_word_type, rhymes_with=first, meter=meter, syllables=syllables)
            return first, second
        except NoWordError:
            continue
    conditions = []
    if meter:
        conditions.append("has meter " + meter)
    if syllables:
        conditions.append("has {} syllables".format(syllables))
    raise NoWordError("Couldn't find a rhyming {} and {} with {}".format(
        first_word_type.__name__, second_word_type.__name__, 
        " and ".join(conditions)))

def count_syllables(word):
    """Counts the number of syllables in a word.

        >>> count_syllables("bogus")
        2

    Args: 
        word (str)

    Returns:
        int: The number of syllables in the word.
    """
    phones = phones_for_word(word)
    if len(phones) > 0:
        return syllable_count(phones[0])

def get_meter(word):
    """Returns the word's meter, or its pattern of stresses when the word is spoken.
    Meter can be used to write poetry with a beat.
    The meter is a string of digits. 1 means primary stress (loudest), 
    2 means secondary stress (medium), and 0 means unstressed (quiet). 
    For example: 
    
        >>> get_meter("animal")
        '100'
        >>> get_meter("helicopter")
        '1020'
        >>> get_meter("inexcusable")
        '20100'

    Args: 
        word (str)

    Returns:
        Meter
    """
    phones = phones_for_word(word)
    if not phones:
        raise NoWordError("Could not pronounce " + word)
    return Meter(stresses(phones[0]))

def starts_with_vowel_sound(text):
    """Checks whether the text starts with a vowel sound.
    Useful for determining whether to use 'a' or 'an' as an 
    indefinite article.

        >>> starts_with_vowel_sound("horrible hounds")
        False
        >>> starts_with_vowel_sound("awesome owls")
        True

    Args: 
        text (str): One or more words.

    Returns: 
        bool: `True` if the text starts with 
    """
    first_word = text.split(" ")[0]
    vowel_phones = ["AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IY", "IH", "OW", "OY", "UH", "UW"]
    phones = phones_for_word(first_word)
    return len(phones) > 0 and phones[0].split(' ')[0][:2] in vowel_phones

class NoWordError(Exception):
    "This error means no word(s) matched the search."

