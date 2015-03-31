#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo
  echo "Usage:"
  echo
  echo "    $0 http://www.example.com task_set"
  echo
  exit 1
fi

BIN_LOCUST=`which locust`
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
TASK_SET=$DIR/task_set/$2.py

if [ ! -f "$TASK_SET" ]; then
  echo "Task set $2 does not exist"
  exit 1
fi

$BIN_LOCUST -L DEBUG -H $1 -f $TASK_SET

