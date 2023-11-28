#!/bin/bash
ascii_art="
           _____ _____ _    _ _    _ ____  
     /\   |  __ \_   _| |  | | |  | |  _ \ 
    /  \  | |__) || | | |__| | |  | | |_) |
   / /\ \ |  ___/ | | |  __  | |  | |  _ < 
  / ____ \| |    _| |_| |  | | |__| | |_) |
 /_/    \_\_|   |_____|_|  |_|\____/|____/ 

V 1.2
By L4y3rSev3n
"
echo "$ascii_art"
python3 change.py
pkill php
python3 dump.py &
cd tmp
php -S 127.0.0.1:8080 > /dev/null 2>&1 &
sleep 20
cd ..
. verify_response.sh

