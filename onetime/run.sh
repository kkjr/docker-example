#!/bin/bash

for i in {1..10}; do    
    echo -n "Request: name$i --> Result: "
    docker run --rm onetime "name$i"
done