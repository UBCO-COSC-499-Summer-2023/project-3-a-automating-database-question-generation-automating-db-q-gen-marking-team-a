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

# Docker Documentation for PrairieLearn and AutoER
1. Install docker, docker-compose, and docker-desktop(optional)

2. git clone the prairielearn repo, and the AutoER Repo.

3. Make Sure that in the Docker-compose.yml file in the AutoER database the Image line states `prairielearn/prairielearn:latest`, instead of `prairielearn/prairielearn:local`
or
build the docker image from the prairielearn repo.
test to make sure you have the docker image by running `docker images`

4. inside the AutoER repo, run `docker-compose create`
then `docker-compose start`

5. to check if the docker container is running, run `docker-compose ps`. if the response is empty, run `docker-compose ps -a`, and it will show the status of the closed docker container.


### Issues With PrairieLearn pertaining to AutoER

1. the `elements/pl-iml-element` element does not work when loaded universally in the `[prairielearn directory]` and must be loaded in the `[course directory]` of choice. Prairielearn Documentation ***EXPLICITLY*** states that the elements directory be in either directory - depending on desired functionality.

2. The AutoER `docker-compose.yml` file was set to load a local image of prairielearn, which does not exist on a virgin machine. as staeted in step 3. changing the Image line from `prairielearn/prairielearn:latest`, instead of `prairielearn/prairielearn:local` should solve this issue. Otherwise building the image from the PrairieLearn repo, then launching the docker-compose inside the AutoER directory should work.

3. As per the PrairieLearn Documentation. All question directories should have a `server.py` file. none of the AutoER questions have that. This creates confusion.
