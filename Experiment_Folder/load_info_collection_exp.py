# Hybrid Load Information Collection

import random
import time

# Node class represents each individual node in the system
class Node:
    def __init__(self, node_id, load, group_id):
        self.node_id = node_id  # Unique ID of the node
        self.load = load        # Load information (randomized for simulation)
        self.group_id = group_id  # Group to which the node belongs
        self.is_leader = False  # Flag to mark group leader

# System class that represents the entire system of nodes
class System:
    def __init__(self, num_nodes):
        self.nodes = []  # List to hold all nodes
        self.groups = {}  # Dictionary to hold nodes grouped by group_id
        self.leaders = {}  # Dictionary to hold the leaders of each group
        
        # Initialize nodes and distribute them into groups
        for i in range(num_nodes):
            node = Node(i, random.randint(1, 100), i % 3)  # Assign nodes randomly into 3 groups
            self.nodes.append(node)
            if node.group_id not in self.groups:
                self.groups[node.group_id] = []
            self.groups[node.group_id].append(node)
        
        # Assign group leaders (randomly select one node per group as the leader)
        for group_id in self.groups:
            leader = random.choice(self.groups[group_id])
            leader.is_leader = True
            self.leaders[group_id] = leader

    # Centralized method: Collect load information in a single central location
    def centralized_load_collection(self, group_id):
        total_load = sum(node.load for node in self.groups[group_id])
        print(f"Centralized Load for Group {group_id}: {total_load}")
        return total_load
    
    # Broadcast method: Broadcast load data to all nodes
    def broadcast_load_data(self):
        print("Broadcasting load data to all nodes:")
        for node in self.nodes:
            print(f"Node {node.node_id} Load: {node.load}")
    
    # Group Communication method: Load collection within each group by group leader
    def group_communication(self, group_id):
        group_leader = self.leaders[group_id]
        total_load = sum(node.load for node in self.groups[group_id] if node.node_id != group_leader.node_id)
        total_load += group_leader.load  # Add the leader's load as well
        print(f"Group {group_id} Leader Node {group_leader.node_id} collected a total load of: {total_load}")
        return total_load

    # Hybrid method: Dynamically choose which technique to use based on the total system load
    def hybrid_load_collection(self):
        total_system_load = sum(node.load for node in self.nodes)
        print(f"Total system load: {total_system_load}")
        
        if total_system_load < 200:
            # Use centralized load collection for low load systems
            print("\nUsing Centralized Load Collection (Low system load)...")
            for group_id in self.groups:
                self.centralized_load_collection(group_id)
        elif total_system_load < 500:
            # Use group communication for medium load systems
            print("\nUsing Group Communication (Medium system load)...")
            for group_id in self.groups:
                self.group_communication(group_id)
        else:
            # Use broadcast for high load systems
            print("\nUsing Broadcast Load Collection (High system load)...")
            self.broadcast_load_data()

# Simulate the operation of the system
def main():
    # Seed random number generator for reproducibility
    random.seed(time.time())
    
    # Create a system with 10 nodes
    system = System(10)
    
    # Perform hybrid load collection based on system conditions
    system.hybrid_load_collection()

if __name__ == "__main__":
    main()
