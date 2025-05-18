# 🚀 Level 3: Auxiliary Code Generation with AI

### 🎯 Objective:
Learn how to use AI (e.g., Claude, ChatGPT) to generate complete, functional scripts for specialized tasks such as data analysis, visualization, and processing. This activity demonstrates how AI can help students and educators tackle complex coding tasks that would otherwise require significant manual effort and domain expertise.

---

## 🧠 Concept: One-shot Script Generation for Data Analysis

In this activity, we explore how AI can be used to generate complete scripts for specific tasks, particularly data analysis and visualization. Instead of writing code from scratch, we focus on using AI to **transform requirements** into ready-to-use code that students can run, understand, and modify.

---

## 🎓 Pedagogical Framing

The goal isn't to replace students' programming skills, but to:

- **Accelerate complex implementation tasks** so students can focus on higher-level concepts and analysis
- Provide **practical examples of good coding practices** that students can learn from
- Help students **bridge the gap** between theoretical understanding and practical implementation
- Enable **more ambitious projects** that would be too time-consuming to code manually

This approach promotes:
- More time spent on analysis and interpretation rather than implementation details
- Exposure to more advanced programming techniques than students might be ready to write themselves
- A mindset of *focusing on the problem* rather than getting stuck on syntax

---

## 🔍 Example Scenario: Microprocessor Signal Analysis

In this example from a Microprocessor-based Design course, students need to analyze timing data from digital signals. The PulseCap module captures the timing of rising and falling edges, but students need to process and visualize this data to understand signal behavior.

### The Challenge:
- Students have captured signal timing data in a specialized format 
- They need to plot the cumulative probability distribution (CDF) of latency between falling and rising edges
- The analysis requires statistical processing and professional-quality visualization

---

## 📊 Input Data Format

The input data is in CSV format with the following columns:
1. Sample Time (in seconds)
2. Edge type (0 for RISING, 1 for FALLING)
3. Duration since last edge of same type (e.g., RISING → RISING)
4. Duration since last edge of opposite type (e.g., FALLING → RISING)

This data comes from the PulseCap kernel module used for capturing the timing of digital signals at 10ns accuracy.

---

## 🤖 Suggested AI Prompt

To generate a script that can process and visualize this data, you can use the following prompt with an AI assistant (like Claude or ChatGPT):

> **Prompt:**
>
> "I need a Python script to analyze timing data from digital signals. I have a CSV file with the following columns:
> 1. Sample Time (in seconds)
> 2. Edge type (0 for RISING, 1 for FALLING)
> 3. Duration since last edge of same type (seconds)
> 4. Duration since last edge of opposite type (seconds)
> 
> Please write a script that:
> 1. Reads the CSV file
> 2. Extracts the latency between falling and rising edges (column 4 when edge type is 0/RISING)
> 3. Calculates and plots the cumulative probability distribution (CDF) of this latency
> 4. Adds appropriate labels, title, and grid to the plot
> 5. Displays some basic statistics (mean, median, min, max, standard deviation)
> 6. Saves the plot as a PNG file
> 
> Please include comments explaining the code and handle potential errors."

---

## ✅ Sample Generated Script

```python
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
        data = pd.read_csv(csv_file, header=None)
        
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
```

---

## 💡 How to Use the Generated Script

1. **Save the script** as a Python file (e.g., `analyze_latency.py`)
2. **Install required packages** if necessary:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. **Run the script** with your CSV file:
   ```bash
   python analyze_latency.py path/to/your_data.csv
   ```
4. **Review the output** statistics and CDF plot to analyze signal latency

The generated script provides a foundation that students can further customize for their specific analysis needs.

---

## 💬 Reflection Questions

After using AI to generate this script, consider:

- How would this script need to be modified for different timing characteristics?
- What additional analyses might be valuable for understanding signal behavior?
- How does having a working script impact your ability to focus on interpreting the results rather than implementation details?
- What parts of the code would you have struggled to implement on your own?

---

## 🧑‍🏫 Instructor Activity: Designing an AI-Supported Data Analysis Task

Now that you've explored how AI tools can generate complete scripts for data analysis, consider how you might use this approach in your own teaching.

### 🎓 Your Task:
Design a **classroom activity** where students use an AI assistant to generate a script that processes and analyzes data relevant to your course.

1. **Identify a data-heavy task** in your curriculum that typically requires extensive coding
2. **Craft a detailed prompt** that would help an AI assistant generate a useful script
3. **Consider how students will learn** from analyzing and potentially modifying the generated code
4. **Plan for assessment** that focuses on understanding and interpretation rather than implementation

This approach allows students to engage with more complex analyses than might otherwise be possible, while still developing their understanding of programming concepts and practices.
