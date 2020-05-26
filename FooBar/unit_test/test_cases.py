import pytest
import requests


@pytest.mark.usefixtures("driver_get")
class TestNumber:
    @pytest.mark.selenium
    @pytest.mark.parametrize('input', [2, 4, 6, 7, 100, 15, 20, 105, 27])
    def test_verify_numbers(self, input):
        self.driver.get("http://localhost:8000/home")
        enter_number = self.driver.find_element_by_id('inputNumber')
        enter_number.send_keys(input)
        result_button = self.driver.find_element_by_xpath('//*[@id="getFooBar"]/input[2]')
        result_button.click()

        result_value = self.driver.find_element_by_xpath('//*[@id="results_2"]')
        result = result_value.get_attribute('value')

        if input % 3 == 0 and input % 5 == 0:
            expected_result = 'foo and bar'
        elif input % 3 == 0:
            expected_result = 'foo'
        elif input % 5 == 0:
            expected_result = 'bar'
        else:
            expected_result = ""

        assert result == expected_result, f"Expected result {expected_result} is different from actual result {result}"


class TestNumber2:
    @pytest.mark.requests
    @pytest.mark.parametrize('input', [20, 41, 60, 72, 105, 15, 21, 45, 27, 49, 3, 1, 99, 30, 101, 56, 23, 33])
    def test_verify_numbers_by_requests(self, input):
        url = "http://localhost:8000/get_result/"
        params = {'number': input}

        response = requests.post(url, data=params)
        result = response.json()['data']
        result = result if result else ""

        if input % 3 == 0 and input % 5 == 0:
            expected_result = ['foo', 'bar']
        elif input % 3 == 0:
            expected_result = ['foo']
        elif input % 5 == 0:
            expected_result = ['bar']
        else:
            expected_result = ""

        assert result == expected_result, f"Expected result {expected_result} is different from actual result {result}"