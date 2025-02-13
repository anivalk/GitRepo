*** Settings ***
Library		SeleniumLibrary

*** Variables ***
${HOMEPAGE}    http://www.google.com     # This is a comment text.
${BROWSER}     edge 
${topic}       Browser stack 

*** Test Cases ***
# Avataan selain

Opening Browser
    Open Browser to Site URL

# Tehdään Google-haku
Search on Google
    Search topic    ${topic}

*** Keywords ***
Open Browser to Site URL
    Open Browser    ${HOMEPAGE}    ${BROWSER} 
    Click Element    id:L2AGLb
    Title Should Be    Google 

Search topic
    [Arguments]    ${topic}
    Input Text  name=q    ${topic}
    Click Button  name=btnK

*** Comments ***
Here is a comment text.
