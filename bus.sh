#!/bin/sh
/usr/local/bin/python -m src.main >> logs/logs_$(date '+%Y-%m-%d').txt
