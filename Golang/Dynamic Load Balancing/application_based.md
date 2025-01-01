# Load Measurement and Dynamic Load Balancing in Golang

## Overview
This project demonstrates a simple approach to dynamic load balancing using Golang. The program simulates a scenario where multiple servers handle varying task loads. It uses an application-based method to dynamically assign tasks to the least loaded server.

## Key Concepts
- **Dynamic Load Balancing**: Dynamically distributing tasks across servers based on their current load to ensure optimal resource utilization and efficiency.
- **Simulation**: Server loads and task assignments are simulated with random values to mimic real-world scenarios.

## How the Code Works
1. **Initialization**: A set of servers is initialized, each with a random starting load.
2. **Task Assignment**: Tasks with random load values are generated and assigned to the server with the least load.
3. **Load Distribution**: The program updates the server's load after assigning a task.
4. **Output**: The initial and final loads of each server are displayed to illustrate the dynamic balancing process.

## Usage
To run the program:
1. Install [Golang](https://golang.org/) if not already installed.
2. Copy the code from `main.go` into a file named `(Whatever-you-named-your-file).go`.
3. Run the program:
   ```bash
   go run main.go
