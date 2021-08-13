from vocabulary import starts_with_vowel_sound
from grammatical_types import (
    Noun, 
    PluralNoun,
    TransitiveVerb,
    IntransitiveVerb,
    PastTenseTransitiveVerb,
    PastTenseIntransitiveVerb,
    Adjective,
    Adverb, 
    NounPhrase,
    Determiner, 
    DeterminedNounPhrase,
    VerbPhrase, 
    Sentence
)
# LOVE POEMS

def pluralize(noun):
    "Noun -> PluralNoun"
    assert type(noun) == Noun
    if noun.endswith("s") or noun.endswith("ch") or noun.endswith("sh"):
        return PluralNoun(noun + 'es')
    else:
        return PluralNoun(noun + 's')

# COUPLETS

def noun_phrase(adjective, noun_phrase):
    "(Adjective, NounPhrase) -> NounPhrase"
    #YOUR CODE GOES HERE
    assert isinstance(adjective, Adjective)
    assert isinstance(noun_phrase, NounPhrase)
    return NounPhrase(adjective + ' ' + noun_phrase)

def determine_noun_phrase(determiner, noun_phrase):
    "(Determiner, NounPhrase) -> DeterminedNounPhrase"
    #YOUR CODE GOES HERE
    assert isinstance(determiner, Determiner)
    assert isinstance(noun_phrase, NounPhrase)
    return DeterminedNounPhrase(determiner + ' ' + noun_phrase)

#     raise NotImplemented("This function isn't done!")

def make_definite(noun_phrase):
    "NounPhrase -> DeterminedNounPhrase"
    #YOUR CODE GOES HERE
    assert isinstance(noun_phrase, NounPhrase)
    determined_noun_phrase = determine_noun_phrase(Determiner("the"), noun_phrase)
    return determined_noun_phrase
#     raise NotImplemented("This function isn't done!")

def make_indefinite(noun_phrase):
    "NounPhrase -> DeterminedNounPhrase"
    #YOUR CODE GOES HERE
    assert isinstance(noun_phrase, NounPhrase)
    if starts_with_vowel_sound(noun_phrase):
        determined_noun_phrase = determine_noun_phrase(Determiner("an"), noun_phrase)
    else:
        determined_noun_phrase = determine_noun_phrase(Determiner("a"), noun_phrase)
    return determined_noun_phrase
#     raise NotImplemented("This function isn't done!")

# LIMERICKS

def verb_phrase(adverb, verb_phrase):
    "(Adverb, VerbPhrase) -> VerbPhrase"
    #YOUR CODE GOES HERE
    assert isinstance(adverb, Adverb)
    assert isinstance(verb_phrase, VerbPhrase)
    return VerbPhrase(adverb + " " + verb_phrase)

#     raise NotImplemented("This function isn't done!")

def past_tense_transitive(verb):
    "TransitiveVerb -> PastTenseTransitiveVerb"
    #YOUR CODE GOES HERE
    assert type(verb) == TransitiveVerb
    if verb[-1] == 'e':
        past_tense_transitive_verb = PastTenseTransitiveVerb(verb + 'd')
    else:
        past_tense_transitive_verb = PastTenseTransitiveVerb(verb + 'ed')
    return past_tense_transitive_verb
#     raise NotImplemented("This function isn't done!")

def past_tense_intransitive(verb):
    "TransitiveVerb -> PastTenseTransitiveVerb"
    #YOUR CODE GOES HERE
    assert type(verb) == IntransitiveVerb
    if verb[-1] == 'e':
        past_tense_intransitive_verb = PastTenseIntransitiveVerb(verb + 'd')
    else:
        past_tense_intransitive_verb = PastTenseIntransitiveVerb(verb + 'ed')
    return past_tense_intransitive_verb

#     raise NotImplemented("This function isn't done!")

def verb_phrase_transitive(verb, noun_phrase):
    "(TransitiveVerb, NounPhrase) -> VerbPhrase"
    #YOUR CODE GOES HERE
    assert isinstance(verb, TransitiveVerb)
    assert isinstance(noun_phrase, NounPhrase)
    return VerbPhrase(verb + " " + noun_phrase)
#     raise NotImplemented("This function isn't done!")

