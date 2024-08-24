# 4insite Backend Take-home Assignment
This is the RESTful API backend (Django and PostgreSQL) counterpart of the frontend demo found at: https://gloriousloaf.github.io/4i-take-home-backend/

# Table of Contents
- [Technologies](#technologies)
- [Features](#features)
  - [Employees](#employees)
  - [Assets](#assets)
- [Demo](#demo)
- [Models](#models)
  - [**Employee**](#employee)
  - [**Asset**](#asset)


## Technologies
- Django 5.1
- PostgreSQL 16
- python-dotenv v1.0.1 (load `.env` variables)
- psycopg2-binary v2.9.9 (adapter for PostgreSQL)

## MVP Features

### Employees
- [x] Create an employee
- [x] Read all employees
- [x] Read one employee
- [x] Update one employee
- [x] Delete one employee

### Assets
- [x] Create an asset
- [x] Read all assets
- [x] Read one asset
- [x] Update one asset
- [x] Delete one asset

## Demo

WIP

## Models

### **Employee**

| Attribute  |  Type   |        Options         |
| ---------- | :-----: | :--------------------: |
| first_name | string  |     max. 200 chars     |
| last_name  | string  |     max. 200 chars     |
| email      | string  | max. 200 chars, unique |
| telephone  | string  | max. 17 chars, unique  |
| bio        | string  |    max. 1000 chars     |
| union      | boolean |     default: False     |

### **Asset**

| Attribute     |  Type   |                 Options                 |
| ------------- | :-----: | :-------------------------------------: |
| asset_name    | string  |             max. 200 chars              |
| serial_number | string  |          max. 50 chars, unique          |
| price         | decimal | min. 0, max 10 digits, 2 decimal places |
| color         | string  |              max. 50 chars              |
| description   | string  |             max. 1000 chars             |
| certification | boolean |             default: False              |
