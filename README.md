[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11208034&assignment_repo_type=AssignmentRepo)
# Project-Structure
```
.
├── docs                    # Documentation files (alternatively `doc`)
│   ├── scope-charter       # Scope and Charter
│   ├── design              # Design documents
│   ├── final               # Final documents
│   ├── weekly logs         # Team and Individual Logs
│   ├── marking             # Documents for grading
│   ├── porting             # Documentation for porting code editors
│   ├── communication       # Documentation for communication with client
│   ├── archived            # Documentation from autoER group
│   └── mvp                 # Documentation used for MVP
│
├── databaseCourse          # Course files
├── drone                   # Automated tests (Old)
├── tests                   # Selenium Front-end testing
├── README.md
├── .drone.yml              # Automated tests
└── docker-compose.yml      # Creating docker container

```
Also, update your README.md file with the team and client/project information.  You can find details on writing GitHub Markdown [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) as well as a [handy cheatsheet](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf).   

Roles:  
Project Manager:    Nishant Srinivasan  
Client Liason:      Matthew Obirek  
Technical Lead:     Skyler Alderson  
Integration Lead:   Andrei Zipis  


# Docker

This project requires two Docker containers. The first Docker container runs PrairieLearn and the course instance. The second Docker container hosts a server to run RelaX queries, which is required for grading relational algebra and displaying expected outputs for relational algebra questions.


## Docker Documentation for PrairieLearn

1. Install docker, docker-compose, and docker-desktop(optional)

2. git clone this repository: `https://github.com/UBCO-COSC-499-Summer-2023/project-3-a-automating-database-question-generation-automating-db-q-gen-marking-team-a.git`

3. In your terminal, navigate to cloned directory.

4. In your terminal run `docker-compose up`

5. (Optional) To check if the docker container is running, run `docker-compose ps`. if the response is empty, run `docker-compose ps -a`, and it will show the status of the closed docker container.


## Creating the relaxAPI container

1. Visit repository found at `https://github.com/azipis/RelaXQueryAPI`

2. Follow directions found at that repository.


# Linters

This project makes use of two linters, ESLint for JavaScript and pylint for Python.  


## ESLint

ESLint requires Node.js to be installed locally. To download Node.js, visit `https://nodejs.org/en`. Navigate to the project folder and run the command `npm install eslint`. ESLint can then be run either through the console (visit `https://eslint.org/docs/latest/` for more information) or the recommended route of installing it through Visual Studio Code's extensions. The linter automatically runs when used through Visual Studio Code.  
To adjust ESLinter's configuration, use the `.eslintrc.json` file and adjust the `"rules"` block. Visit `https://eslint.org/docs/latest/rules/` for a complete list of rules.  


## pylint

pylint must be installed in the project folder. Navigate to the project folder and run the command `pip install pylint`. pylint can be run through either the console (visits `https://docs.pylint.org/index.html` for more information) or the recommended route of installing it through Visual Studio Code's extensions.  The linter automatically runs when used through Visual Studio Code.  
To adjust pylint's configuration, use the `.pylintrc` file. Visit `https://docs.pylint.org/index.html` for more information about pylint configuration.
