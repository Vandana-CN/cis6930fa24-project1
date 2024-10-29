import pytest


from assignment1.date_detector import censor_date

@pytest.fixture
def sample_test_string():
    '''Provides a sample incident string to test detect_names method'''
    return '''James met andrew on 19th march which is one day before 22-03-2026 and 5 days after 12/12/2021 '''

def test_censor_phones(sample_test_string):
    final_string, stats = censor_date(sample_test_string, {})
    assert final_string is not sample_test_string