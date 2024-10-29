import pyap
import spacy
import warnings
import nltk
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import re
import argparse

warnings.filterwarnings("ignore")
def detect_address(text):
    '''This function detects address entities from a text'''
    pyap_addresses = pyap.parse(text, country='US')
    nlp = spacy.load("en_core_web_md")
    doc = nlp(text)

    # Extract named entities (persons)
    spacy_location_entities = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return pyap_addresses, spacy_location_entities

def censor_address(text, stats):
    '''This function detects address from a text and censors them with special characters'''
    pyap_addresses, spacy_loc_entities = detect_address(text)

    for address in pyap_addresses:
        text = text.replace(str(address), 'X' * len(str(address)))
    for tag in spacy_loc_entities:
        text = text.replace(tag, 'X' * len(tag))
    stats['addresses masked'] = len(pyap_addresses) + len(spacy_loc_entities)
    
    return text, stats

def detect_and_redact_concepts(data, concepts, stats):
    syn_list =[]
    text=data
    sent=data.split('\n')
    concept_list =[]
    # result =[]
    match_count = 0
    # print(sent)
    for concept in concepts:
        for syn in wordnet.synsets(concept):
            for l in syn.lemmas():
                syn_list.append(l.name())
        # print(syn_list)
    for i in sent:
        token=[]
        token = nltk.word_tokenize(i)
        # print(token)
        for j in token:
            for synonyms in syn_list:
                if synonyms in j:
                    concept_list.append(j)
                    # print(j)
        # print(concept_list)
        
        for j in concept_list:
            if j in text:
                match_count+=1
                text = text.replace(j, '^'*len(j))
                # print(j)
        # result.append(text)

        # string = "redacted_concept"
        # get_stats(string, len(concept_list))
        # concept_list.clear()
        stats['concepts masked'] = match_count
    # print(f'matched concepts - {match_count}')
    return text, stats


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--concept', action='append', help='<Required> Set flag', required=True)
    args = parser.parse_args()
    input_concepts = args.concept
    data = '''Hello, Here is a spreadsheet from the charwoman confirmations group of all kid financial trades between ENA and this entity that have ever been entered into the 
    
    jolly of this girl child Mickey mouse. Let me know what you think. brant youngster'''

    print(detect_and_redact_concepts(data, input_concepts))