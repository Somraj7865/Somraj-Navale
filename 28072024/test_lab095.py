import pytest


@pytest.fixture
def sample_data1():
    data= [1,2,3,4,5]
    return data
@pytest.fixture()
def sample_data2():
    return True

def test_consume_1_2(sample_data1,sample_data2):
    print(sample_data1)
    print(sample_data2)

def test_consume_1_21(sample_data1, sample_data2):
        print(sample_data1)
        print(sample_data2)