# Processor State Determination


import psutil
import random
import time

# Function to get the current CPU usage (0-100%)
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Function to get the current CPU temperature (simulated for this example)
def get_cpu_temperature():
    # psutil's sensors_temperature() is available on Linux and certain platforms, but we will simulate.
    return random.randint(30, 100)  # Temperature between 30 and 100 degrees Celsius.

# Function to simulate power state (we assume it's either 'low', 'normal', or 'high')
def get_power_state():
    return random.choice(['low', 'normal', 'high'])

# Function to determine processor state
def determine_processor_state():
    cpu_usage = get_cpu_usage()
    cpu_temp = get_cpu_temperature()
    power_state = get_power_state()

    state = ""
    
    # Determine state based on CPU usage, temperature, and power state
    if cpu_usage < 10:
        state = "Idle"  # CPU is not doing much work, it's idle.
    elif cpu_usage > 90:
        if cpu_temp > 85:
            state = "Thermal Throttling"  # CPU is under high load and temperature is too high.
        else:
            state = "High Performance"  # CPU is under heavy load and working at full capacity.
    elif power_state == "low":
        state = "Low Power"  # CPU is in a power-saving mode.
    elif power_state == "high":
        state = "Overclocked"  # CPU is running at a higher clock speed for performance.
    else:
        state = "Normal"  # CPU is working in a regular state.

    return state, cpu_usage, cpu_temp, power_state

# Simulate the state determination over time
def simulate_processor_state():
    while True:
        state, cpu_usage, cpu_temp, power_state = determine_processor_state()
        
        # Print the determined processor state
        print(f"CPU Usage: {cpu_usage}% | Temperature: {cpu_temp}°C | Power State: {power_state} | Determined State: {state}")
        
        # Wait for some time before the next evaluation
        time.sleep(2)

# Start the simulation
simulate_processor_state()
