### robot_test_keywords.robot ###

*** Settings ***
Library    robot_test_cases.py

*** Keywords ***
Test Login By Email    
    [Arguments]    ${WebDriverRemoteUrl}    ${LocalFilePath} 
    robot_test_cases.setup_method    ${WebDriverRemoteUrl}    ${LocalFilePath}
    robot_test_cases.test_login_email
    robot_test_cases.teardown_method

Test Logout
    [Arguments]    ${WebDriverRemoteUrl}    ${LocalFilePath} 
    robot_test_cases.setup_method    ${WebDriverRemoteUrl}    ${LocalFilePath}
    robot_test_cases.test_login_email
    robot_test_cases.test_aha_logout
    robot_test_cases.teardown_method

Test Edit Profile
    [Arguments]    ${WebDriverRemoteUrl}    ${LocalFilePath} 
    robot_test_cases.setup_method    ${WebDriverRemoteUrl}    ${LocalFilePath}
    robot_test_cases.test_login_email
    robot_test_cases.test_aha_edit_profile
    robot_test_cases.test_aha_logout
    robot_test_cases.teardown_method