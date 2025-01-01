// main.go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Server struct {
	ID   int
	Load int // Simulated load percentage
}

type LoadBalancer struct {
	Servers []Server
}

func (lb *LoadBalancer) DistributeLoad() {
	totalServers := len(lb.Servers)
	if totalServers == 0 {
		fmt.Println("No servers available.")
		return
	}

	// Simulate dynamic load distribution
	taskLoad := rand.Intn(100) + 1
	leastLoadedServer := &lb.Servers[0]

	// Find the server with the least load
	for i := 1; i < totalServers; i++ {
		if lb.Servers[i].Load < leastLoadedServer.Load {
			leastLoadedServer = &lb.Servers[i]
		}
	}

	// Assign task to the least loaded server
	leastLoadedServer.Load += taskLoad
	fmt.Printf("Task with load %d assigned to Server %d. Current Load: %d\n", taskLoad, leastLoadedServer.ID, leastLoadedServer.Load)
}

func main() {
	rand.Seed(time.Now().UnixNano())

	// Initialize servers
	servers := []Server{
		{ID: 1, Load: rand.Intn(50)},
		{ID: 2, Load: rand.Intn(50)},
		{ID: 3, Load: rand.Intn(50)},
	}

	lb := LoadBalancer{Servers: servers}

	// Display initial server loads
	fmt.Println("Initial Server Loads:")
	for _, server := range lb.Servers {
		fmt.Printf("Server %d: %d\n", server.ID, server.Load)
	}

	fmt.Println("\nDistributing Load...")
	for i := 0; i < 5; i++ { // Simulate 5 tasks
		lb.DistributeLoad()
	}

	// Display final server loads
	fmt.Println("\nFinal Server Loads:")
	for _, server := range lb.Servers {
		fmt.Printf("Server %d: %d\n", server.ID, server.Load)
	}
}
