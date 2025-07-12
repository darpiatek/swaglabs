# Swag Labs Testing Framework

[![N|Solid](https://www.saucedemo.com/v1/img/Login_Bot_graphic.png)](https://www.saucedemo.com/v1/)


# Overview

Testing framework using PyTest to automate Swag Labs e-commerce workflows, including logging in, adding items to the cart, completing checkout, and verifying order confirmation.
# Getting Started

## Setup test env

* install [Python 3.8][python] or greater
* install [Git][git]
* install [Allure][allure]
* open command line and clone the project from GitHub
```cmd
https://github.com/darpiatek/swaglabs.git
``` 
* Create Python virtual environment
```
cd swaglabs
python3 -m venv venv
source venv/bin/activate
```
* Install requirements
```
python3 -m pip install -r conf/requirements.txt
```
* Create .env file in the project directory and add following. Add to .env file the key received in the email. Its required to decrypt credentials
```.env
ENV=DEV
LOG_LEVEL=INFO
FERNET_KEY=<paste key from email>
```

## Run tests

Open command line in the project directory and run command:
```
python3 -m pytest --alluredir allure-results
```
## Generate reports

Open command line in the project directory and run command:
```
allure generate allure-results --clean -o allure-report
allure open allure-report
```

[python]: <python.org>
[git]: <https://git-scm.com/downloads>
[allure]: <https://allurereport.org/start/>