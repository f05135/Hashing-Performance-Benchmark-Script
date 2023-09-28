# Hashing Performance Benchmark Script

## Summary

This Python script is designed to benchmark the performance of various hashing algorithms by measuring the average time it takes to hash a set of random strings of different lengths. It utilizes multiprocessing to perform concurrent hashing for efficient analysis. The script generates visualizations in the form of a bar chart, saves the results as a JSON file, and creates an interactive HTML plot for further analysis.

## Key Points

- **Hashing Algorithms**: The script supports the following hashing algorithms for benchmarking:
  - MD5
  - SHA-1
  - SHA-256
  - SHA-512
  - SHA3-256
  - SHA3-512

- **String Lengths**: It tests hashing performance across various string lengths, including 10, 25, 50, 75, 100, 150, 200, 500, 1000 and 5000 characters.

- **Parallel Processing**: The script leverages the `multiprocessing` module to hash random strings concurrently, making efficient use of available CPU cores.

- **Visualization**: It generates a bar chart using Matplotlib, illustrating the average hashing time versus string length for each algorithm.

- **Results Storage**: The results, including the bar chart, are saved in a timestamped folder. The results folder contains:
  - A PDF of the bar chart.
  - A JSON file containing the average hashing times.
  - An interactive HTML plot for further exploration.
  - ![](https://github.com/f05135/Hashing-Performance-Benchmark-Script/blob/main/Media%20Assets/hashing_results_folder_video.gif)

## Details

### How the Script Works

1. **Importing Libraries**: The script imports the necessary libraries and modules, including hashlib, random, string, time, multiprocessing, Matplotlib, and mpld3.

2. **Constants**: It defines various constants, including the hashing algorithms to test, different string lengths to test, the number of random strings to generate, and a custom color palette for plotting.

3. **Random String Generation**: The script provides a function (`generate_random_string`) to generate random strings of a specified length, excluding emojis.

4. **Hashing Function**: Another function (`hash_string`) is defined to hash a given input string using a specified hashing algorithm.

5. **Hashing and Measurement**: The `hash_and_measure_avg_time` function hashes a set of random strings using a chosen algorithm and measures the average time it takes to hash them. It leverages the `multiprocessing` module for parallel processing.

6. **Main Function**: The `main` function orchestrates the entire benchmarking process:
   - Determines the number of available CPU cores.
   - Generates random strings of various lengths.
   - Initializes a dictionary to store the benchmark results.
   - Creates a timestamped folder to store results.
   - Iterates over the specified hashing algorithms, using multiprocessing for efficient hashing.
   - Pauses for 2 seconds between algorithm changes.
   - Generates a bar chart to visualize the average hashing times.
   - Converts the Matplotlib plot to an interactive HTML plot using `mpld3`.
   - Saves the results as a PDF, a JSON file, and an HTML file in the results folder.

### Running the Script

1. Ensure you have Python installed.

2. Install required libraries using pip: `pip install matplotlib mpld3`

3. Execute the script: `python Hashing_Performance_Benchmark_Script.py`

4. The script will generate hash times and visualizations for various hashing algorithms and string lengths, saving results in a timestamped folder for analysis.
