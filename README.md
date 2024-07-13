# TierIV-Test-Cases

### Project Name: YouTube Login
### Created By: Savithri Wewala
### Created Date: 2024/07/13

Scenario ID | Scenario| Test Case ID |  Test Case |Prerequisites| Test Data | Execution Steps | Expected Result | Tester | Status | Actual Result |  Comment | 
----- | ----- | ----- | ----- |----- |----- |----- |----- |----- |----- |----- |----- |
1 |Logging In| 1.1 | Log in with Valid Credentials | https://www.youtube.com is loaded ↓ ↓ ↓  | email:t70323534@gmail.com password:test123|  1.Click 'Login' button 2.Enter **valid** username 3.Click 'Next' button 4.Enter **invalid** password 5.Click 'Next' button | User successfully logs in |
  |  |  |1.2 |Log in with Invalid Credentials | | email:t70323534@test.com password:invalid123| 1.Click 'Login' button 2.Enter **valid** username 3.Click 'Next' button 4.Enter **invalid** password 5.Click 'Next' button |1.User is prevented from logging in 2.Error message is displayed |
