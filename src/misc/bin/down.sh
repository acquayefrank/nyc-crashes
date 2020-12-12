#!/bin/bash

SCRIPT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source ${SCRIPT_PATH}/environment-vars.sh

cd $SCRIPT_PATH/../../
docker-compose -f docker-compose.yml -p $PROJECT_USER down
cd -
