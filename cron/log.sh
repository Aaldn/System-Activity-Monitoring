#!/bin/bash

# execute python commands from "/app" directory
PYTHONPATH=/app

* 9-17 * * 1-5 /usr/bin/python3 -c 'import log; log.append_log()'
* 0 * * * /usr/bin/python3 -c 'import log; log.create_log()'
* * 1,15 * * /usr/bin/python3 -c 'import log; log.remove_log()'
