import pytest


from assignment1.name_detector import detect_names, censor_names

@pytest.fixture
def sample_test_string():
    '''Provides a sample incident string to test detect_names method'''
    return '''Kevin O'Toole and james johnson
        Vice President -- Marketing
        Western Hub Properties L.L.C.
        14811 St. Marys Ln., Suite 150
        Houston, TX   77079-2908
        281-679-3591 V
        281-679-1564 F
        713-208-0153 M
        kotoole@westernhubs.com'''

def test_detect_names(sample_test_string):
    names = detect_names(sample_test_string)
    assert len(names)>0
    assert names is not None

def test_censor_names(sample_test_string):
    final_string, stats = censor_names(sample_test_string, {})
    assert final_string is not sample_test_string


