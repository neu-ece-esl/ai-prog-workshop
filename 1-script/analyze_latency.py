import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import seaborn as sns
from pathlib import Path
import sys

def analyze_edge_latency(csv_file):
    """
    Analyze timing data from PulseCap and plot CDF of falling-to-rising edge latency.
    
    Args:
        csv_file: Path to the CSV file containing edge timing data
    """
    try:
        # Set visual style for plots
        sns.set_style("whitegrid")
        plt.figure(figsize=(10, 6))
        
        # Read the CSV file
        print(f"Reading data from {csv_file}...")
        data = pd.read_csv(csv_file, header=None, skiprows=1)  # Skip the first row
        
        # Assign column names based on documentation
        data.columns = ['SampleTime', 'EdgeType', 'SameEdgeDuration', 'OppositeEdgeDuration']
        
        # Extract only the RISING edges (EdgeType = 0)
        rising_edges = data[data['EdgeType'] == 0]
        
        # The OppositeEdgeDuration column for rising edges gives us the FALLING→RISING latency
        latencies = rising_edges['OppositeEdgeDuration']
        
        # Convert to microseconds for better readability
        latencies_us = latencies * 1e6
        
        # Calculate basic statistics
        stats = {
            'count': len(latencies_us),
            'mean': np.mean(latencies_us),
            'median': np.median(latencies_us),
            'min': np.min(latencies_us),
            'max': np.max(latencies_us),
            'std': np.std(latencies_us)
        }
        
        # Print statistics
        print("\nFalling→Rising Edge Latency Statistics (microseconds):")
        print(f"Count: {stats['count']}")
        print(f"Mean: {stats['mean']:.3f} µs")
        print(f"Median: {stats['median']:.3f} µs")
        print(f"Min: {stats['min']:.3f} µs")
        print(f"Max: {stats['max']:.3f} µs")
        print(f"Std Dev: {stats['std']:.3f} µs")
        
        # Sort latencies for CDF
        sorted_latencies = np.sort(latencies_us)
        
        # Calculate the CDF (probability from 0 to 1 for each data point)
        # For each value, what percentage of the data is less than or equal to it
        cdf = np.arange(1, len(sorted_latencies) + 1) / len(sorted_latencies)
        
        # Plot the CDF
        plt.plot(sorted_latencies, cdf, 'b-', linewidth=2)
        
        # Add a line for the mean
        plt.axvline(x=stats['mean'], color='r', linestyle='--', 
                    label=f"Mean: {stats['mean']:.3f} µs")
        
        # Add a line for the median
        plt.axvline(x=stats['median'], color='g', linestyle='-.',
                    label=f"Median: {stats['median']:.3f} µs")
        
        # Configure the plot
        plt.grid(True, alpha=0.3)
        plt.xlabel('Latency (microseconds)')
        plt.ylabel('Cumulative Probability')
        plt.title('Cumulative Distribution Function (CDF) of Falling→Rising Edge Latency')
        plt.legend()
        
        # Create formatter for x-axis
        formatter = ScalarFormatter(useOffset=False)
        formatter.set_scientific(False)
        plt.gca().xaxis.set_major_formatter(formatter)
        
        # Save the plot
        output_file = Path(csv_file).stem + "_latency_cdf.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"\nPlot saved as {output_file}")
        
        # Show the plot
        plt.tight_layout()
        plt.show()
        
        return True
        
    except Exception as e:
        print(f"Error analyzing data: {e}")
        return False

if __name__ == "__main__":
    # Get the CSV file from command-line arguments or use a default
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    else:
        # Prompt user for file if not provided as argument
        csv_file = input("Enter the path to the CSV file: ")
    
    # Run the analysis
    analyze_edge_latency(csv_file)