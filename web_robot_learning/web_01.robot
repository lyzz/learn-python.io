*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://www.baidu.com
${BROWSER}        Chrome

*** Test Cases ***
百度搜索关键字
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Input Text      id:kw       helloworldrob