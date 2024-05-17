#!/bin/bash
# This script downloads data from sreality.cz, processes them and saves them to ../data/sreality/sreality.json
# Jindřich Bär (barjin), 2024

# Expected usage: ./index.sh
#  - the script stores the data in `data/sreality/index.json`
#  - in case of any errors, try running `chmod +x ./*.sh` in this directory first.

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Download the listing ids from Sreality.cz
$SCRIPT_DIR/downloader.sh

# Parse the response and pull the hash_ids for each listing
jq ._embedded.estates[] data.json | jq -s . > array.json
jq .[].hash_id ./array.json  > ids.csv

# Download the details for each listing, based on the hash_id and store them in details.json
$SCRIPT_DIR/download.details.sh
jq . details.json | jq -s . > details_array.json

# Combine the locality and recommendations_data into a single object and store it in index.json
jq ".[] | { locality: .locality.value } + .recommendations_data" ./details_array.json | jq -s . > ../../data/sreality/index.json

# Clean up
rm data.json array.json details.json details_array.json ids.csv