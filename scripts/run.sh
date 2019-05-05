#!/bin/bash

export PYTHONPATH=$PWD
export FLASK_APP=core/univesp/src/api
export FLASK_ENV=development
flask run
