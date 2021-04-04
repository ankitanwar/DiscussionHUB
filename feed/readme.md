# Feed Service
Feed Service is responsible to mange the post added by the users and display the result to the users

<b>Feed Features</b>

| Feature  | Description  |
|----------|:-------------|
| Add Information | To Add Information About The New Interships |
| Modify Information | To Modify The Details Of The Added Post |
| Delete Post | To Delete The Post  |
| ViewPost | To View The Post By Unique PostID  |
| View Post Of A User | To View All The Post Of The Given User  |
| Filter Posts | To Filter Post According To The Interest  |


<br></br>


<b>End Points</b>

| Request  | Description  | Url |
|----------|:-------------|:-------------|
| Post | To Add New Post Regarding The Internships | host:8070/feed |
| Delete | To Delete The Post With Given ID |host:8070/feed/:PostID |
| Get | To Get All The Post Of The Given User |host:8070/feed |
| Get | To Get The Particular Post With The Given PostID |host:8070/feed/:PostID |
| Get | To Filter Post According To The Values Provided By The Users |host:8070/filter |



<br></br>