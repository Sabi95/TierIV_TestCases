# TierIV-Test-Cases

### Project Name: LinkedIn Login
### Created By: Savithri Wewala
### Created Date: 2024/07/13

Scenario ID | Scenario| Test Case ID |  Test Case |Prerequisites| Test Data | Execution Steps | Expected Result | Tester | Status | Actual Result |  Comment | 
----- | ----- | ----- | ----- |----- |----- |----- |----- |----- |----- |----- |----- |
1 |Logging In| 1.1 | Log in with Valid Credentials | https://www.linkedin.com/login is loaded ↓ ↓ ↓  | email:t70323534@gmail.com password:test123|  1.Enter **valid** username and **valid** password 2.Click 'Sign In' button | User successfully logs in |
  |  |  |1.2 |Log in with Invalid Credentials | | email:invalidemail@test.com password:invalid123| 1.Enter **invalid** username and **invalid** password 2.Click 'Sign In' button |1.User is prevented from logging in 2.Error message is displayed |
