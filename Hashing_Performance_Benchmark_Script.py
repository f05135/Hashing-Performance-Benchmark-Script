import hashlib
import random
import string
import time
import matplotlib.pyplot as plt
import multiprocessing
import os
from datetime import datetime
import json
import mpld3

# CONSTANTS
algorithms = ['md5', 'sha1', 'sha256', 'sha512', 'sha3_256', 'sha3_512']
string_lengths = [10, 25, 50, 75, 100, 150, 200, 500, 1000, 5000]  # Different string lengths to test
num_samples = 50000  # Number of random strings to generate for each length, needs to be >= 50000.

# Set a random seed for reproducibility
random_seed = 42
random.seed(random_seed)

# Define a custom color palette with distinct colors
custom_colors = ['#1f77b4', '#FFD700', '#2ca02c', '#d62728', '#BDBDBD', '#000000']

# Function to generate a random string excluding emojis
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to hash a string using various hashing algorithms
def hash_string(input_string, algorithm):
    hash_func = hashlib.new(algorithm)
    hash_func.update(input_string.encode())
    return hash_func.hexdigest()

# Function to perform hashing and return average time with a 2-second pause
def hash_and_measure_avg_time(args):
    algorithm, random_strings = args
    num_samples = len(random_strings)
    
    start_time = time.time_ns()
    
    [hash_string(s, algorithm) for s in random_strings]  # Perform hashing
    
    end_time = time.time_ns()

    total_time = end_time - start_time
    return total_time / num_samples

# Main function to perform the comparison and create a bar chart
def main():
    print("\n----- Unless you have a NASA computer, go grab a coffee and come back later because it will take some time to complete this script. -----")
    for i in range(10):
        num_cpus = multiprocessing.cpu_count()  # Get the number of available CPU cores

        # Get CPU information
        cpu_count = os.cpu_count()
        
        print(f"\nUsing {num_cpus} CPU cores for analysis")
        print(f"Number of CPU cores available: {cpu_count}")

        # Generate random strings for all lengths
        random_strings = {}
        for length in string_lengths:
            random_strings[length] = [generate_random_string(length) for _ in range(num_samples)]

        results = {}  # Store the results for plotting

        # Create a Results folder with a timestamped name
        timestamp = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
        results_folder = f"results_{timestamp}"
        os.makedirs(results_folder, exist_ok=True)

        # Modify this part of the code in the main() function
        for algorithm in algorithms:
            results[algorithm] = {}  # Use a dictionary to store the average times

            print(f"\nTesting hashing algorithm: {algorithm}")
            with multiprocessing.Pool(processes=num_cpus) as pool:
                args = [(algorithm, random_strings[length]) for length in string_lengths]
                results_list = pool.map(hash_and_measure_avg_time, args)

            for length, result in zip(string_lengths, results_list):
                results[algorithm][length] = result  # Store average time for each string length

            # Pause for 1 second before changing the algorithm
            time.sleep(1)

        # Create a bar chart
        plt.figure(figsize=(10, 6))
        for i, (algorithm, avg_times) in enumerate(results.items()):
            avg_times = [avg_times[length] for length in string_lengths]
            plt.plot(
                string_lengths,
                avg_times,
                marker='o',            # Marker style
                markersize=4,          # Adjust marker size here (e.g., 4 for a smaller size)
                label=algorithm,
                color=custom_colors[i]
            )

        plt.title('Average Hashing Time vs. String Length')
        plt.xlabel('String Length')
        plt.ylabel('Average Hashing Time (ns)')
        plt.legend()
        plt.grid(True)
        
        # Convert the Matplotlib plot to an interactive HTML plot
        interactive_plot = mpld3.fig_to_html(plt.gcf())
        
        # Save the plot as a PDF with a timestamped filename
        plot_filename_two = f"a_result_{timestamp}.pdf"
        plt.savefig(os.path.join(results_folder, plot_filename_two))
        
        # Save the results as a JSON file with a timestamped filename
        results_json_filename = f"b_result_{timestamp}.json"
        with open(os.path.join(results_folder, results_json_filename), 'w') as json_file:
            json.dump(results, json_file, indent=4)

        # Save the interactive plot as an HTML file with a timestamped filename
        plot_filename = f"c_result_{timestamp}.html"
        with open(os.path.join(results_folder, plot_filename), 'w') as html_file:
            html_file.write(interactive_plot)


if __name__ == "__main__":
    print("\n----- Welcome to the Hashing Performance Benchmark -----")
    main()