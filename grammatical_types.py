
class PartOfSpeech(str):
    "A grammatical part of speech"

class NounPhrase(PartOfSpeech):
    """A phrase whose head is a noun. May contain a determiner and adjectives. 
    Examples: eagle, evil mountain, several delicious candies. that lady
    """

class DeterminedNounPhrase(NounPhrase):
    """A NounPhrase containing a determiner. 
    Examples: my shirt, the pencil, any dog
    """

class Pronoun(DeterminedNounPhrase):
    """A noun referring to another noun.
    Examples: I, you, it, he, she
    """

class Noun(NounPhrase):
    """A base noun (which is a valid NounPhrase).
    Examples: child, pillow, chair, you
    """

class PluralNoun(Noun):
    """A noun referring to more than one of something.
    Examples: cats, houses, ideas, people
    """

class VerbPhrase(PartOfSpeech):
    """A phrase whose head is a verb, possibly containing adverbs.
    Examples: think, eat a donut, swim in the ocean
    """

class TransitiveVerb(PartOfSpeech):
    """A verb which has a subject and an object. 
    (Note that many verbs may be transitive or intransitive. You can eat or eat an apple.
    Examples: annoy, cancel, chase, disobey
    """

class IntransitiveVerb(VerbPhrase):
    """A verb with a subject but no object.
    Examples: sleep, depart, run, jump
    """

class PastTenseTransitiveVerb(TransitiveVerb):
    """A transitive verb in the past tense.
    Examples: annoted, canceled, chased, disobeyed
    """

class PastTenseIntransitiveVerb(IntransitiveVerb):
    """An intransitive verb in the past tense. 
    Examples: slept, departed, ran, jumped
    """

class Adjective(PartOfSpeech):
    """A word which describes a noun. 
    Examples: blue, ugly, tiny, late
    """

class Adverb(PartOfSpeech):
    """A word which describes a verb. 
    Examples: quickly, violently, suspiciously, boldly
    """

class Determiner(PartOfSpeech):
    """A word which comes before a noun phrase and determines its referent.
    Examples: my, your, a, an, the, that, some
    """

class Sentence(PartOfSpeech):
    """A noun phrase and a verb phrase.
    Examples: I ate some old bread. The cat caught the bird. The broken chair regretted its history.
    """

class Meter(str):
    """The stress pattern of a word's syllables. 
    A Meter is a string of digits. 1 means primary stress (loudest), 
    2 means secondary stress (medium), and 0 means unstressed (quiet). 
    For example, the meter of 'animal' is '100', the meter of 'helicopter' is '1020', and
    the meter of 'inexcusable' is '20100'.
    """

    def __init__(self, code):
        allowed_digits = ['0', '1', '2']
        if not all(digit in allowed_digits for digit in code):
            raise ValueError("A Meter must be a string of digits, 0-2, like '1020'")

class Poem(list):
    """A Poem is just a list which can format itself nicely on multiple lines.
    """
    def __str__(self):
        return "\n".join(str(line).capitalize() for line in self)
