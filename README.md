[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11208034&assignment_repo_type=AssignmentRepo)
# Project-Starter

Please use the provided folder structure for your docs (scope & charter, design documenation, communications log, weekly logs and final documentation), source code, tesing, etc.    You are free to organize any additional internal folder structure as required by the project.  Please use a branching workflow and once an item is ready, do remember to issue a PR, review and merge in into the master brach.
```
.
├── docs                    # Documentation files (alternatively `doc`)
│   ├── scope_and_charter   # Scope and Charter
│   ├── design              # Getting started guide
│   ├── final               # Getting started guide
│   ├── logs                # Team Logs
│   └── ...          
├── src                     # Source files (alternatively `lib` or `app`)
├── test                    # Automated tests (alternatively `spec` or `tests`)
├── tools                   # Tools and utilities
└── README.md
```
Also, update your README.md file with the team and client/project information.  You can find details on writing GitHub Markdown [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) as well as a [handy cheatsheet](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf).   


Roles:  
Project Manager:    Nishant Srinivasan  
Client Liason:      Matthew Obirek  
Technical Lead:     Skyler Alderson  
Integration Lead:   Andrei Zipis  

#### Setup DroneCI
1. create an Oauth in github

2. Create public URL using gnork `ngrok http 8090`, and add the randomly generated url to the Oauth as such
```
Homepage URL
https://e869-64-180-128-103.ngrok-free.app

Authorization callback URL
https://e869-64-180-128-103.ngrok-free.app/login

```
3. in an new terminal, create a rand hex code `openssl rand -hex 16`

4. create and format a .env file like such
```
  DRONE_GITHUB_CLIENT_ID=[github client id]
  DRONE_GITHUB_CLIENT_SECRET=[github client secret]
  DRONE_SERVER_HOST=[ngork public url]
  DRONE_RPC_SECRET=[openssl hex code]
  CLIENT_DRONE_RPC_HOST=e869-64-180-128-103.ngrok-free.app
  username=[Github-Username]
```

5. run `docker-compose build` `docker-compose start`