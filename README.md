# FitApp API Backend

![coverage](coverage.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Heroku](https://heroku-badge.herokuapp.com/?app=fit-app-tc)

# Description

This is a simple implementation of a Fitness tracking application, a tool that helps visualize and track your weight loss progress. 

## Live Demo

[https://fitapp.as12production.com/](https://fitapp.as12production.com/)

## Swagger UI  can be accessed here
[https://fit-app-tc.herokuapp.com](https://fit-app-tc.herokuapp.com/)

![FitApp](banner.gif)

# Technology Stack

- Python 3.7
- Flask
- Flask Migrate
- SQL Alchemy
- Postgres SQL
- Swagger UI (API Documentation)
- Auth0 Security

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Database Setup

### Postgres SQL
Follow instructions to install the lastest version of PostgresSQL [postgres docs](https://wiki.postgresql.org/wiki/Detailed_installation_guides)

Create two empty data. One for running the application, and another for running test. This can be any name but let's call it Fit and Fit-test respectively. 

### Setting environment variables

The database connection string should be set in the conf file.

Create a flask configuration for running in a local environment.
```bash
touch conf/api.local.conf
```

The content of this file should be something like this.
```
SQLALCHEMY_DATABASE_URI="postgres://localhost:5432/Fit"
SQLALCHEMY_TRACK_MODIFICATIONS=False
ERROR_404_HELP=False
```

Do the same for api.test.conf for test database as well.
```
SQLALCHEMY_DATABASE_URI="postgres://localhost:5432/Fit-Test"
SQLALCHEMY_TRACK_MODIFICATIONS=False
ERROR_404_HELP=False
```

### Setup Authentication 

The endpoints are secured by using Auth0 as an identity provider. Please refers to Auth0 documentation on how to setup your Application and API security.
Once you have the configuration variable, you can configure them in the conf/auth.conf file.

The content of conf/auth.conf should look like this.
```
AUTH0_DOMAIN={your-auth0-prefix}.auth0.com
AUTH0_ALGORITHM=RS256
AUTH0_API_AUDIENCE={your-auth0-api-audience}
```

### Running the server

The server can be executed by running executing the run.sh for mac environment or simply run the following command.
```bash
export ENV=local
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```

By default the server should be listening for request on localhost:5000

Please refers to flask documentation for other operating system configuration. The environment variable should be set accordingly.

## Testing

### Before running the test

Since the endpoints are secured by Auth0. You will have to obtain the client secret from Auth0. Please refers to Auth0 documentation for this process.
Once you have the client secret, you can modify run-test.sh with the required information.

```
export ENV=test
export CLIENT_SECRET={Your-Auth0-Client-Secret}
export CLIENT_ID={Your-Auth0-Client-ID}
coverage run test_fitapp.py
coverage report
```

```bash
./run-test.sh
```


## API Behavior and Documentation

### Security Roles
 #### Authenticated user
   Default roles for user who signed up for service.:
   - GET users/{user_id}
   - POST users    
   - PATCH users/{user_id}
   - GET progress/{user_id}
   - POST progress/{user_id}
    
 #### Auditor
   Auditors have an additional privileged from Authenticated user to access the following end point.
   - GET users
   - GET progress
    
 #### Administrator
   Have access to every end points.
    
### Accessing the API Doc

Online API documentation:. 
[https://fit-app-tc.herokuapp.com](https://fit-app-tc.herokuapp.com/)

Offline Doc:
[swagger.md](swagger.md)




## License

MIT License. See [LICENSE.md](LICENSE.md)





