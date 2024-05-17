#!/bin/bash

for i in $(seq 1 60); do
    echo "Downloading page $i";
    curl "https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=2&locality_region_id=10&per_page=60&page=$i&tms=1715159262664" >> "data.json";
done