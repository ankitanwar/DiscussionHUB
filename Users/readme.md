# User Service
User Service is responsible for creating the account and It contains all the information user

<b>User Features</b>

| Feature  | Description  |
|----------|:-------------|
| CreateAccount | Ability To Create A New Account |
| DeleteAccount | Ability To Delete Account From The System |
| GetDetails | Ability To View The Details Saved In The system |
| Update Details | Ability To Update The Saved Details In The System |

<br></br>

<b>End Points</b>

| Request  | Description  | Url |
|----------|:-------------|:-------------|
| Post | To Create The New User | host:8080/user |
| Post | To Verify The User By Email ID and Password |host:8080/verify |
| Get | To Get The Details Of The User |host:8080/user |
| Delete | To Delete The User Account |host:8080/user |
| Patch | To Update The Information Of the User |host:8080/user |
| Patch | To Change The Password Of The User |host:8080/verify |



<br></br>