# Chat Service

<b>Chat Features</b>

| Feature  | Description  |
|----------|:-------------|
| Create Group | Ability To Create New Group With People Who Have Common Interest |
| Add Members | Ability To Add The Member In the Group By the Admin Only |
| Remove Members | Ability To Remove The Member In the Group By the Admin Only  |
| Update The Group Name | Ability To Change The Group Name By Admin Only  |


<br></br>


<b>End Points</b>

| Request  | Description  | Url |
|----------|:-------------|:-------------|
| Post | To Create New Room | host:8085/room |
| Post | To Add Member |host:8082/room/:roomID |
| Get | To Get All Room Members |host:8085/room/:roomID |
| Delete | To Remove The Member |host:8085/room |
| Put | To Make Room Member An Admin |host:8085/room/:roomID |


<br></br>