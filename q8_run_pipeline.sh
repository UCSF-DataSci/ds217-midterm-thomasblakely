#!/bin/bash

# NOTE: This script assumes Q1 has already been run to create directories and generate the dataset
# NOTE: Q2 (q2_process_metadata.py) is a standalone Python fundamentals exercise, not part of the main pipeline
# NOTE: Q3 (q3_data_utils.py) is a library imported by the notebooks, not run directly
# NOTE: The main pipeline runs Q4-Q7 notebooks in order

chmod +x q8_run_pipeline.sh

echo "Starting clinical trial data pipeline..." > reports/pipeline_log.txt

echo "Running Q4: Data Exploration..." >> reports/pipeline_log.txt

jupyter nbconvert --execute --to notebook --inplace q4_exploration.ipynb || {
    echo "Error, Q4 has failed." >> reports/pipeline_log.txt; exit 4;
}

echo "Running Q5: Missing Data Analysis" >> reports/pipeline_log.txt

jupyter nbconvert --execute --to notebook --inplace q5_missing_data.ipynb || {
    echo "Error, Q5 has failed." >> reports/pipeline_log.txt; exit 5;
}

echo "Running Q6: Data Transformation" >> reports/pipeline_log.txt

jupyter nbconvert --execute --to notebook --inplace q6_transformation.ipynb || {
    echo "Error, Q6 has failed." >> reports/pipeline_log.txt; exit 6;
}

echo "Running Q7: Group Operation and Final Analysis" >> reports/pipeline_log.txt

jupyter nbconvert --execute --to notebook --inplace q7_aggregation.ipynb || {
    echo "Error, Q7 has failed." >> reports/pipeline_log.txt; exit 7;
}

echo "Pipeline complete!" >> reports/pipeline_log.txt
