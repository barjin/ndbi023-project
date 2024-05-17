#!/bin/bash
# This script uses jq to process the stops data from http://data.pid.cz/stops/json/stops.json to a smaller, more readable file.
# Jindřich Bär (barjin), 2024
#
# Expected usage: ./process_stops.sh ./stops.json
#  - pass the path to the json file from the link above as the first (and only) parameter.
#  - the script outputs the processed JSON into stdout.

jq "
    .stopGroups[] | 
    { 
        name: .uniqueName, 
        lat: .avgLat, 
        lng: .avgLon,
        types: .stops | [.[].lines[].type] | unique
    }
" "$1" | jq -s