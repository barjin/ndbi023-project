#!/bin/bash

counter=0
for id in $(cat ids.csv); do
    counter=$((counter+1))
    echo "Downloading details for $id ($counter)";
    curl -s "https://www.sreality.cz/api/cs/v2/estates/$id" >> details.json
done