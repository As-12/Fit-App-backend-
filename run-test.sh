#!/usr/bin/env bash

# Unit Testing the application
# This should only be used to start local development environment
export ENV=test
export CLIENT_SECRET=
export CLIENT_ID=
coverage run test_fitapp.py
coverage report
