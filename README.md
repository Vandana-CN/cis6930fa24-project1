Name: Vandana Cendrollu Nagesh

# Project Description
1. FEATURES
This python package takes a glob pattern, outputs directory and a few files flags as the input and does the following actions - 
1 - Fetches all the files that match the glob pattern in the program working directory and processes each file at a time.
2 - Extracts names, phone numbers, dates and concepts from the file and maskes the entities with special characters.
3 - Extract statistics of each document and output them in stderr, stdout or a custom stats file.
4 - Store the censored content in a new file with a '.censored' extension with the same file name.

2. PROJECT STRUCTURE
The project is structured to have a censoror file that is triggered initially, which then calls a main file which utilizes four different modules, namely - date_detector, phone_detector, address detector and name_detector to perform the above described actions. All these files are in the assignment1 folder which lies in the root directory, hence the modules are individually imported in the main.py file to make use of the functions in those modules.

The downloaded files is saved into the directory path give in the --output flag. 

3. TESTING
This project can be classified into 3 parts - extracting and censoring entities, storing the data, writing the stats. Test files are designed to test each phase.
test_<entityname>.py file tests the detection and redaction of such entities.


# How to install
pipenv install

## How to run
pipenv run python censoror.py --input '*.'                     --names --dates --phones --concept 'kids'                    --output 'files/'                     --stats stderr

## How to test
pipenv run python3 -m pytest <test_file>

## Functions
#### censoror.py \
censor_docs() - This function processes all files that extend matching the glob , returns stats and .censored files

#### main.py \
mask_content() - This function passes the file_content into different censoring pipelines and censors the detected entities

#### name_detector.py \
detect_names() - This function detects name entities from a string

censor_names() - This function detects named entities from a text and censors them with special characters

#### date_detecor.py \ 
censor_date() - This function detects dates in any format from a text and censors them with special characters

#### phone_detector.py \ 
detect_phone() - This function detects phone numbers entities from a text

censor_phone() - This function detects phone numbers from a text and censors them with special characters

#### concept_detector.py \ 
detect_and_redact_concepts() - This function takes a list of concept words as input and masks all the words that are synonyms or have the similar meaning to the concept words.



## Bugs and Assumptions
1. names are detected using an entity recognition framework called spacy. The accuracy depends on the ability of the underlying model pipeline and it is never 100%. Hence, few entities may not be recognized even though they fall under the category.

