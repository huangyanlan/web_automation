import pytest
from App.testcase.conftest import api_data


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    print("这个函数有什么用呢？")
    return api_data.get(testcase_name)