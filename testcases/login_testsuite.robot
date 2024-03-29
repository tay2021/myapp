*** Settings ***
Library    ../steps/utils.py


*** Test Cases ***
As a user I want to login with valid credential
    ${response}    Send Request To Login
    Log    ${response.status_code}
    Log    ${response.content}
