import spacy
import warnings
warnings.filterwarnings("ignore")
def detect_names(text):
    '''This function detects name entities from a string'''
    # Load the English language model from spaCy
    nlp = spacy.load("en_core_web_md")

    # Process the text using spaCy
    doc = nlp(text)

    # Extract named entities (persons)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    
    return names


def censor_names(text, stats):
    '''This function detects named entities from a text and censors them with special characters'''
    # Call the detect_names function from the name_detector module
    names = detect_names(text)

    # Censor the names in the text
    for name in names:
        # Replace each character in the name with 'X' (you can choose a different character)
        text = text.replace(name, 'X' * len(name))
    stats['names masked'] = len(names)

    return text, stats

