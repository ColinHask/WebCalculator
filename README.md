# KSU SWE 3643 Software Testing and Quality Assurance Semester Project: Web-Based Calculator

This repository contains a Web-Based calculator for statistical and linear regression operations.
The project uses Python Flask for the web server and Python for the logical backend.
Unit tests are included using pytest, and end-to-end testing through playwright is also included.

## Table of Contents
- [Team Members](#team-members)
- [Architecture](#Architecture)
- [Environment](#environment)
- [Executing the Web Application](#executing-the-web-application)
- [Executing Unit Tests](#executing-unit-tests)
- [Reviewing Unit Test Coverage](#reviewing-unit-test-coverage)
- [Executing End-To-End Tests](#executing-end-to-end-tests)
- [Final Video Presentation](#final-video-presentation)

## Team Members
 - Colin Haskins
 - Michael 

## Architecture
The Web-Based Calculator architecture uses four main modules, the logic module, web server module, unit test module, and end-to-end testing module. 

![diagram.svg](README.assets/diagram.svg)

### Functional Modules
The *web server* module renders HTML templates while handling inputs and communicating with the logical module.
The *logical module* receives parameters, handles calculations, and returns values to the web module.

### Testing Modules
The *unit testing* module handles unit tests for the logical module with 100% coverage.
This module references the logical module directly and utilizes pytest for testing. 

The *end-to-end testing* module handles end-to-end Playwright testing for the web server.
Unlike the unit testing module, this module does *not* directly reference the web module, and the server must be running for tests to function.

## Environment

This is a cross-platform application and should work in Windows 10+, Mac OSx Ventura+, and Linux environments. Note that the application has only been carefully tested in Windows 11 and Mac OS.

### To prepare your environment to execute this application:
 1. [Install the latest version of python for your system.](https://www.python.org/downloads/)
 2. [Ensure that pip is correctly installed, updated, and configured.](https://www.datacamp.com/tutorial/pip-upgrade-python)
 3. [Install and configure git if not already set up.](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
4. git Clone this repository via http to an easily accessible directory. <br>
   <br>i. Navigate to the directory you wish to clone the repository. 
   <br>ii. Clone via the following command:
    ```cmd
    git clone https://github.com/ColinHask/WebCalculator.git
    ```
 5. Download necessary dependencies by running the following command:
    ```cmd
    pip install <path-to-requirements.txt> -r 
    ```
    (replace <path-to-requirements.txt> wth the actual path to the requirements.txt file)
### To configure Playwright for end-to-end testing:
  1. [Install and configure Playwright](https://playwright.dev/python/docs/intro)

## Executing the Web Application