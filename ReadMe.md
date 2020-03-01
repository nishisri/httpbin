# HttpBin

## Technologies Used:

* Language - Python
* Test framework - Pytest
* Build tool - Pyenv

## How to start the application:
To run the test simply run the command -   **python httpBin-get-test.py**
This application assumes that Python3 already installed in the system also it assumes that Pytest and requests are also installed.

## Functionality Description:
WebService Url “https://httpbin.org/get” will give the IP address of the client in “Origin” tag in Json Response.
It will give mentioned details in the headers like “Host,User agent,language etc” of the body.
It will give Url in the “Url” key  in the Json response.
User agent will give the details depending upon the browser and its version in each transaction in the response.
And the query parameters can pass in “args” Key of the service. 
“X-Amzn-Trace-Id” is an unique Id which is changing incrementally “a to f” and “0 to 9” in each call of the service.

## Summary: 
For this Service created automation test around 
with 'args' section as mentioned below using python+pytest:-
* test_should_add_string_key_value_params_in_Args
* test_should_add_string_key_value_params_in_Args2 with multiple values
* test_should_accept_special_characters_inParams
* test_aruguments_should_be_empty_if_nothing_passed_after_question_mark
* test_origin_should_have_callers_IP

## Additional Point:
Dockerize test : Assumes that Docker is already installed in the system.
Docker File is provided to configure the docker image 
Run the commands :
docker build -t httbin:test -f ./DockerFile ./

To run the test use below command:
docker run httbin:test

# Areas of Improvement
* Test names can be created more meaningful.
*  As I am a beginner in Python created simple Pytest.
