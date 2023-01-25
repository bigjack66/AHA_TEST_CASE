### robot_test_features.robot ###
*** Settings ***
Resource    robot_test_keywords.robot

*** Variables ***
${WebDriverRemoteUrl}       NONE
${LocalFilePath}            NONE

*** Test Cases ***

AHA Test Login by Email
    [tags]    test-login-email
    Test Login By Email    ${WebDriverRemoteUrl}    ${LocalFilePath}

AHA Test Logout
    [tags]    test-logout
    Test Logout    ${WebDriverRemoteUrl}    ${LocalFilePath}

AHA Test Edit Profile
    [tags]    test-edit-profile
    Test Edit Profile    ${WebDriverRemoteUrl}    ${LocalFilePath}
 