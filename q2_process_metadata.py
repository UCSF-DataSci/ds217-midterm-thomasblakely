#!/usr/bin/env python3
import random

def parse_config(filepath: str) -> dict:
    """
    Parse config file (key=value format) into dictionary.

    Args:
        filepath: Path to q2_config.txt

    Returns:
        dict: Configuration as key-value pairs

    Example:
        >>> config = parse_config('q2_config.txt')
        >>> config['sample_data_rows']
        '100'
    """
    # TODO: Read file, split on '=', create dict
    config = {}
    with open(filepath, 'r') as file:
        for row in file:
            row = row.strip()
            key, value = row.split('=')
            config[key] = value
    return config


def validate_config(config: dict) -> dict:
    """
    Validate configuration values using if/elif/else logic.

    Rules:
    - sample_data_rows must be an int and > 0
    - sample_data_min must be an int and >= 1
    - sample_data_max must be an int and > sample_data_min

    Args:
        config: Configuration dictionary

    Returns:
        dict: Validation results {key: True/False}

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> results = validate_config(config)
        >>> results['sample_data_rows']
        True
    """
    # Validate config dict has length 3
    if len(config) != 3:
        raise ValueError(f"Error, invalid argument length: {len(config)}")
    
    validation = {}
    # Validates each config metric using if/elif/else logic
    for key, value in config.items():
        if key == 'sample_data_rows':
            if value.isdigit():
                validation[key] = int(value) > 0
            else:
                validation[key] = False
        elif key == 'sample_data_min':
            if value.isdigit():
                validation[key] = int(value) >= 1
            else:
                validation[key] = False
        elif key == 'sample_data_max':
            min_value = config.get('sample_data_min')
            if value.isdigit() and min_value.isdigit():
                validation[key] = int(value) > int(min_value)
            else:
                validation[key] = False
        else:
            validation[key] = False
    return validation


def generate_sample_data(filename: str, config: dict) -> None:
    """
    Generate a file with random numbers for testing, one number per row with no header.
    Uses config parameters for number of rows and range.

    Args:
        filename: Output filename (e.g., 'sample_data.csv')
        config: Configuration dictionary with sample_data_rows, sample_data_min, sample_data_max

    Returns:
        None: Creates file on disk

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> generate_sample_data('sample_data.csv', config)
        # Creates file with 100 random numbers between 18-75, one per row
        >>> import random
        >>> random.randint(18, 75)  # Returns random integer between 18-75
    """
    # Parse config values (convert strings to int)
    num_rows = int(config['sample_data_rows'])
    min_value = int(config['sample_data_min'])
    max_value = int(config['sample_data_max'])

    # Generate random numbers and save to file
    # Use random module with config-specified range
    with open(filename, 'w') as file:
        for row in range(num_rows):
            random_number = random.randint(min_value, max_value)
            file.write(f"{random_number}\n")
 


def calculate_statistics(data: list) -> dict:
    """
    Calculate basic statistics.

    Args:
        data: List of numbers

    Returns:
        dict: {mean, median, sum, count}

    Example:
        >>> stats = calculate_statistics([10, 20, 30, 40, 50])
        >>> stats['mean']
        30.0
    """
    # Calculate stats
    cs_count = len(data)
    cs_sum = sum(data)
    cs_mean = sum(data) / len(data)
    data_sort = sorted(data)

    # Calculate median based on even or odd number of values
    if cs_count % 2 == 0:
        cs_median = (data_sort[(cs_count // 2) - 1] + data_sort[cs_count // 2]) / 2
    else:
        cs_median = data_sort[cs_count // 2]
    return {
        'mean' : cs_mean,
        'median' : cs_median,
        'sum' : cs_sum,
        'count' : cs_count
    }


if __name__ == '__main__':
    # Test  functions with sample data
    config = parse_config('q2_config.txt')
    validation = validate_config(config)
    generate_sample_data('data/sample_data.csv', config)
    
    # Read the generated file and calculate statistics
    numbers = []
    with open('data/sample_data.csv', 'r') as file:
        for row in file:
            row = row.strip()
            numbers.append(int(row))
    stats = calculate_statistics(numbers)

    # Save statistics to output/statistics.txt
    with open('output/statistics.txt', 'w') as file:
        for key, value in stats.items():
            file.write(f"{key}: {value}\n")
    print("q2_process_metadata.py has successfully run")