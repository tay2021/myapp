*** Settings ***
Library    Browser

*** Keywords ***
Open browser and go to page
    Open Browser    https://playwright.dev/    browser=chromium    headless=True
    Click    //a[text()='Get started']