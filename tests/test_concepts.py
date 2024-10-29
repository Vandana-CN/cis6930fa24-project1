import pytest


from assignment1.concept_detector import detect_and_redact_concepts

@pytest.fixture
def sample_test_string():
    '''Provides a sample incident string to test detect_names method'''
    return '''Kevin O'Toole and james johnson kid
        Vice President -- Marketing charwoman
        Western Hub Properties L.L.C.
        14811 St. Marys Ln., Suite 150
        Houston, TX   77079-2908
        281-679-3591 V
        281-679-1564 F
        713-208-0153 M
        kotoole@westernhubs.com'''

@pytest.fixture
def sample_concepts():
    '''Provides a list of concepts'''
    return ['kids', 'woman']



def test_detect_and_redact_concept(sample_test_string, sample_concepts):
    text, stats = detect_and_redact_concepts(sample_test_string, sample_concepts, {})
    assert stats['concepts masked']>0

