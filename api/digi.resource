*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://api.digikala.com/v1/dynamic-landing/mobile/
&{HEADERS}    accept=application/json    origin=https://www.digikala.com    user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36    x-web-client=desktop    x-web-optimize-response=1

*** Keywords ***
Setup Digikala API Session
    Create Session    digikala    ${BASE_URL}    headers=&{HEADERS}

Send GET Request To Digikala API
    ${response}    GET On Session    digikala    /
    Set Test Variable    ${response}    ${response}   
    
Response Should Be 200
    Should Be Equal As Strings    ${response.status_code}    200

Log Response Body
    Log    ${response.json()}
