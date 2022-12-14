# This project is to technical interview of Justo.mx


## Overview:

Spy's Platform

# The .env file
Because this project a interview, the file .env stay inside the project.
**This practice is awful to enviromento difference to local**


## Objectives

This project proposes a solution to create a simple spy's platform to create Hits, assign Hitmen, and manage Hitmen.


## Use cases to support:

### Hitmens 
- Register Hitnem (Login not necessary)

- Login Hitmen (Login not necessary)
 (Login not necessary)
- Logout Hitmen

### Managers 

- Change Hitmen of open project (Login necessary)

- Disable Hitmen (Login necessary)

- List own hits and his subordinates (Login necessary)

- Create Hit (Login necessary)

- Read details a his subordinate (Login necessary)

- List his subordinates (Login necessary)

### BigBoss 
The BigBoss has more permissions than the manager.

- List all Hitmens include Manager (Login necessary)

- Change Hitmen of open project (Login necessary)

- Disable Hitmen (Login necessary)

- List own hits and his subordinates (Login necessary)

- Create Hit (Login necessary)

- Read details a his subordinate (Login necessary)

- List his subordinates (Login necessary)


## Use cases unsupported:

- Delete Hitmen

- Update Password

- Interactions with apis o thirds



## Stack's technology

- Python

- Django

- PostgreSQL

- Docker

- Docker Compose

- Makefile


## The structure this project is based on:

[Django StyleGuide from HackSoftware](https://github.com/HackSoftware/Django-Styleguide)

**with some changes**


## Instructions to up project


#### These instructions use [make](https://es.wikipedia.org/wiki/Make) to streamline interaction with the project.

> Note: If not had `make` on your compute at the bottom of this page are instructions with docker commands


### To build and run project

**Build project**

`make build`


**Run project**

`make run`


#### To stop project

`make stop`

#### To run tests

`make test`


## Other commands

#### To enter the inside of the container bash

`make bash`


#### To watch logs of Back

`make logs-back`


#### To watch logs of DB

`make logs-db`


## Instructions with Docker Compose

#### To run project

`docker-compose up`


#### To stop project

`docker-compose stop`


## Documentation

In the next link you can see a document with examples of the project and its operation.
[Flow](https://es.wikipedia.org/wiki/Make)


