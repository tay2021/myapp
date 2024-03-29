*** Settings ***
Library    ../steps/utils.py
Resource    ../steps/login.resource


*** Test Cases ***
As a user I want to login with valid credential
    ${response}    Send Request To Login
    Log    ${response.status_code}
    Log    ${response.content}

As a user I want to open browser
    Open Browser And Go To Page