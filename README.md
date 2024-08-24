# 4insite Backend Take-home Assignment
This is the RESTful API backend (Django and PostgreSQL) counterpart of the frontend demo found at: https://gloriousloaf.github.io/4i-take-home-backend/

# Table of Contents
- [Technologies](#technologies)
- [MVP Features](#mvp-features)
  - [Employees](#employees)
  - [Assets](#assets)
- [Demos](#demos)
  - [Employee endpoints demo](#employee-endpoints-demo)
  - [Asset endpoints demo](#asset-endpoints-demo)
- [Models](#models)
  - [**Employee**](#employee)
  - [**Asset**](#asset)
- [REST API](#rest-api)
  - [Employees](#employees-1)
  - [Sample of Employee POST request](#sample-of-employee-post-request)
  - [Assets](#assets-1)
  - [Sample of Asset POST request](#sample-of-asset-post-request)
- [Resources](#resources)

## Technologies
- Django 5.1
- PostgreSQL 16
- python-dotenv v1.0.1 (load `.env` variables)
- psycopg2-binary v2.9.9 (adapter for PostgreSQL)
- Pre-commit
- Ruff (python linter and formatter)

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

## Demos

### Employee endpoints demo
<video controls src="media/videos/demo_employees_endpoints.mp4" title="Employee endpoints demo"></video>

### Asset endpoints demo
<video controls src="media/videos/demo_assets_endpoints.mp4" title="Title"></video>

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


## REST API

### Employees

| Method | URL                 | What it does                    |
| ------ | :------------------ | :------------------------------ |
| GET    | /api/employees/     | Gets a list of employees        |
| GET    | /api/employees/:id/ | Gets the details of an employee |
| POST   | /api/employees/     | Creates an employee             |
| PUT    | /api/employees/:id/ | Updates an employee             |
| DELETE | /api/employees/:id/ | Deletes an employee             |

### Sample of Employee POST request
```json
{
  "first_name": "Johnny",
  "last_name": "Doe",
  "email": "johnny.doe@email.com",
  "telephone": "(123) 456-7892",
  "bio": "Hello, my name is Johnny Doe and I'm a human."
}
```

### Assets

| Method | URL              | What it does                 |
| ------ | :--------------- | :--------------------------- |
| GET    | /api/assets/     | Gets a list of assets        |
| GET    | /api/assets/:id/ | Gets the details of an asset |
| POST   | /api/assets/     | Creates an asset             |
| PUT    | /api/assets/:id/ | Updates an asset             |
| DELETE | /api/assets/:id/ | Deletes an asset             |

### Sample of Asset POST request
```json
{
  "asset_name": "Lenovo IdeaPad 1 HD Laptop Intel Celeron N4020",
  "serial_number": "89ZXCVBN01",
  "price": "199.99",
  "color": "Silver",
  "description": "Customers love the Lenovo Ideapad 1 for its budget-friendly price, user-friendly interface, long battery life, and lightweight design, making it a great choice for basic computing tasks and as a gift. However, some users have expressed concerns about its slow performance, limited RAM, and processor speed, which may not be suitable for more demanding tasks."
}
```

## Resources
- [Django docs](https://docs.djangoproject.com/en/5.1/)
- [Django Styleguide](https://github.com/HackSoftware/Django-Styleguide) by HackSoft
