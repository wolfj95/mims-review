from vocabulary import random_word, rhyming_pair, get_meter
from grammar import *
from grammatical_types import *
from random import randint

def love_poem():
    "() -> Poem"
    poem = Poem() 
    poem.append("roses are red")
    poem.append("violets are blue")
    poem.append(pluralize(random_word(Noun)) + " are " + random_word(Adjective))
    poem.append("and so are you.")
    return poem

def couplet():
    "() -> Poem"
    poem = Poem() 
    first_noun, second_noun = rhyming_pair(Noun, Noun, meter=Meter("1"))
    first_adjective = random_word(Adjective, meter=Meter("100"))
    first_np = make_indefinite(noun_phrase(first_adjective, first_noun))
    second_adjective = random_word(Adjective, meter=Meter("10"))
    second_np = make_indefinite(noun_phrase(second_adjective, second_noun))
    poem.append("I used to have " + first_np)
    poem.append("Until I swapped it for " + second_np + ".")
    return poem
    
def limerick(name, subjective_pronoun):
    "str, str -> Poem"
    noun0, noun1 = random_word(Noun, count=2, rhymes_with=name)
    adjective = random_word(Adjective, meter=Meter("100"))
    adverb = random_word(Adverb, meter=Meter("10"))
    verb0, verb1 = rhyming_pair(TransitiveVerb, TransitiveVerb, meter=Meter("10"))
    object_pronoun = Pronoun("it")

    np0 = make_indefinite(noun_phrase(adjective, noun0))
    np1 = make_indefinite(noun1)
    verb0 = past_tense_transitive(verb0)
    verb1 = past_tense_transitive(verb1)
    vp0 = verb_phrase(adverb, verb_phrase_transitive(verb0, object_pronoun))
    vp1 = verb_phrase_transitive(verb1, object_pronoun)

    poem = Poem() 
    poem.append("there once was a person named " + name)
    poem.append("who owned " + np0 + ".")
    poem.append(subjective_pronoun + " " + vp0 + ",") 
    poem.append("and then " + subjective_pronoun + " " + vp1 + ",")
    poem.append("until it turned into " + np1 + ".")
    return poem

from random import randint
def haiku_line(syllables):
    "() -> Sentence"
    noun_syllables = randint(1, syllables-1)
    verb_syllables = syllables - noun_syllables
    noun = random_word(Noun, syllables=noun_syllables)
    plural_noun = pluralize(noun)
    noun_phrase = NounPhrase(plural_noun)
    
    verb = random_word(IntransitiveVerb, syllables=verb_syllables)
    verb_phrase = VerbPhrase(verb)
    
    sentence = Sentence(noun_phrase + " " + verb_phrase)
    return sentence

def haiku():
    "() -> Poem"
    line_0 = haiku_line(5)
    line_1 = haiku_line(7)
    line_2 = haiku_line(5)
    
    poem = Poem() 
    poem.append(line_0)
    poem.append(line_1)
    poem.append(line_2)
    
    return poem
