# quick_savannah
A brief description of what your project does and its purpose.

## Features

- User authentication with JWT (JSON Web Token).
- SMS notifications for specific actions using Africa's Talking API.
- Function-based views for signup, signin, and customer/order management.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

python>=3.8
Django>=3.2
djangorestframework
djangorestframework-simplejwt
africastalking
django-allauth


### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/yourprojectname.git
```
### Navigate to the project directory:
```bash
cd quick_savannah
```
### Install required packages:
```bash

pip install -r requirements.txt
```

### Run migrations to create the database schema:
```bash

python manage.py migrate
```

### Running the Tests
```bash

python manage.py test
```
### Usage

This section provides details on how to interact with the API, including endpoints for user signup and managing customers and orders.

### Signup

Create a new user account.

- **Endpoint**: `/user/signup/`
- **Method**: POST
- **Data Example**:

```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "securepassword123",
  "number": "1234567890"
}
```
#### Customers
List Customers
Retrieve a list of all customers.


- **Endpoint**: `/customers/`
- **Method**: GET
- **Data Example**:
```json
{
    "id": 1,
    "number": "+2541234567",
    "name": "janedoe",
    "code": null,
    "created_at": "2024-02-23T15:29:58.443387Z",
    "updated_at": "2024-02-23T15:29:58.443418Z",
    "user": 2
}
```

#### Orders

- **Endpoint**: /orders/
-**Method**: POST
Create Order
Place a new order and trigger an SMS notification to the customers number if order is successful


Data Example:
``` json
{
  "customer": 1,
  "item": "Mazda cx5",
  "amount": 19.99
}
```

