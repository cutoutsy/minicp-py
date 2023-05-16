#!/usr/bin/env bash

ROOT_FOLDER=`pwd`
export PYTHONPATH=$ROOT_FOLDER

# pytest -s tests
pytest -s tests/minicp
