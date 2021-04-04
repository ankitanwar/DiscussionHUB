# Authentication Service
Auth service is responsible to give the Access Token & Verify The Given Request

<b>Auth Features</b>

| Feature  | Description  |
|----------|:-------------|
| login | To Get The AccessToken And Access Private Services |
| logout | To Delete the Access Token |
| verify | To Verify Whether The User Has Valid Access Token Or Not  |


<br></br>

<b>End Points</b>

| Request  | Description  | Url |
|----------|:-------------|:-------------|
| Post | To Get The Access Token | host:8082/access |
| Get | To Verify the Access Token |host:8082/access |
| Delete | To Delete The Access Token |host:8082/access |


<br></br>