import unittest
import requests


class HttpBinGet(unittest.TestCase):

    def test_should_add_string_key_value_params_in_Args(self):
        responseBodyJson = requests.get("https://httpbin.org/get", params={"a": 1}).json()
        assert responseBodyJson["args"]["a"] == u'1'

    def test_should_add_string_key_value_params_in_Args2(self):
        responseBodyJson = requests.get("https://httpbin.org/get", params={"Name": "Nishi", "age": 28}).json()
        args_ = responseBodyJson["args"]
        assert args_["Name"] == u"Nishi"
        assert args_["age"] == u'28'

    def test_should_accept_special_characters_inParams(self):
        responseBodyJson = requests.get("https://httpbin.org/get", params={"Name": "Mytesting@#$%"}).json()
        assert responseBodyJson["args"]["Name"] == u"Mytesting@#$%"

    def test_aruguments_should_be_empty_if_nothing_passed_after_question_mark(self):
        responseBodyJson = requests.get("https://httpbin.org/get?").json()
        assert bool(responseBodyJson["args"]) == False

    def test_origin_should_have_callers_IP(self):
        responseBodyJson = requests.get("https://httpbin.org/get").json()
        assert responseBodyJson["origin"] == requests.get('https://api.ipify.org').text


if __name__ == '__main__':
    unittest.main()
