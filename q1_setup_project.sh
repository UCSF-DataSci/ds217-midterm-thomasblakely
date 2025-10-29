#!/bin/bash

chmod +x q1_setup_project.sh

mkdir -p data output reports

python3 generate_data.py

ls -la > reports/directory_structure.txt


