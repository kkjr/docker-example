#!/bin/bash
docker run --name myapi --rm -d -p 35000:80 continuous

sleep 2
for i in {1..10}; do    
    echo -n "Request: name$i --> Result: "
    curl -X 'POST' 'http://localhost:35000/hello' -H 'Content-Type: application/json' -d '{"name": "name'$i'"}'
    echo
done

docker stop myapi