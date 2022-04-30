import csv
import random
import matplotlib.pyplot as plt

def average(list):
    return sum(list) / len(list)

# Parameter Declarations
number_of_processes = 250

# CPU Cycle Distribution Parameters
cpu_upper_bound = 1e+13
cpu_lower_bound = 10000000

# Memory Requirement Distribution Parameters
memory_upper_bound = 16000
memory_lower_bound = 1

process_list = []

for i in range(number_of_processes):
    cpu_cycles = random.randint(cpu_lower_bound, cpu_upper_bound)
    memory = random.randint(memory_lower_bound, memory_upper_bound)

    process = [i + 1, cpu_cycles, memory]
    process_list.append(process)

# Open or Create File to Write Data
with open('processes.csv', 'w', newline='') as csvfile:
    # Initialize Writer Class
    writer = csv.writer(csvfile)

    # Write Column Headers
    writer.writerow(['Process ID', 'CPU Cycles', 'Memory Requirement'])
    # Write Process Data
    writer.writerows(process_list)

# Select Values from CPU Cycles Column Only
cpu_cycles = [row[1] for row in process_list]

# Create Historgram of CPU Cycles
plt.hist(cpu_cycles, 10)
# Add Title and Axis Labels
plt.title("CPU Cycle Distribution")
plt.xlabel('CPU Cycles')
plt.ylabel('Frequency')
# Display Histogram
plt.show()

# Select Values from Memory Requirement Column Only
memory = [row[2] for row in process_list]

# Create Histogram of Memory Requirements
plt.hist(memory, 10)
# Add Title and Axis Labels
plt.title("Memory Distribution")
plt.xlabel('Memory Requirement')
plt.ylabel('Frequency')
# Display Histogram
plt.show()

# Print Calculated Average, Min Value & Max Value
print("CPU Cycles")
print("Average: ", average(cpu_cycles))
print("Min Value: ", min(cpu_cycles))
print("Max Value: ", max(cpu_cycles))

# Print Calculated Average, Min Value & Max Value
print("\nMemory Requirement")
print("Average: ", average(memory))
print("Min Value: ", min(memory))
print("Max Value: ", max(memory))