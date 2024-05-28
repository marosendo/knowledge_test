# knowledge_test

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Run](#run-tests)
4. [BDD given-when-then](#BDD-given-when-then)

## General Info
***
It is a project to test my knowledge with automatic tests, both on the web and in the API.
## Technologies
***
A list of technologies used within the project:
* Selenium
* pytest  
* requests

## Run tests
command(python -m unittest discover -s tests ) all tests
command(python -m unittest test/"urlTest) a single test

## BDD given-when-then

Test navigation Home
Given acces to web when load the web then click on Home
Given acces to home when load the home then extract the text on the paragraph

Test navigation Who
Given acces to web when load the web then click on Who we are
Given acces to home when load the home then extract the text on the paragraph

Test API
Given call the service when to response then check the response
