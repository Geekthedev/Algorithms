import random

class Node:
    def __init__(self, node_id, load):
        self.node_id = node_id
        self.load = load
        self.is_balanced = False

    def __repr__(self):
        return f"Node {self.node_id}: Load {self.load}"

class System:
    def __init__(self, num_nodes):
        self.nodes = [Node(i, random.randint(1, 100)) for i in range(num_nodes)]

    def display(self):
        for node in self.nodes:
            print(node)

    def sender_initiated(self):
        for node in self.nodes:
            if node.load > 50:
                target_node = random.choice(self.nodes)
                if target_node != node:
                    transfer_load = min(node.load - 50, 10)
                    node.load -= transfer_load
                    target_node.load += transfer_load
                    print(f"Node {node.node_id} sent {transfer_load} load to Node {target_node.node_id}")

    def receiver_initiated(self):
        for node in self.nodes:
            if node.load < 30:
                source_node = random.choice(self.nodes)
                if source_node != node:
                    transfer_load = min(30 - node.load, 10)
                    node.load += transfer_load
                    source_node.load -= transfer_load
                    print(f"Node {node.node_id} received {transfer_load} load from Node {source_node.node_id}")

    def symmetrically_initiated(self):
        for node in self.nodes:
            if node.load > 50:
                target_node = random.choice(self.nodes)
                if target_node != node and target_node.load < 30:
                    transfer_load = min(node.load - 50, 10)
                    node.load -= transfer_load
                    target_node.load += transfer_load
                    print(f"Node {node.node_id} and Node {target_node.node_id} balanced loads symmetrically: {transfer_load}")

def main():
    system = System(5)
    print("Initial System State:")
    system.display()
    
    print("\nSender-Initiated Load Balancing:")
    system.sender_initiated()
    
    print("\nReceiver-Initiated Load Balancing:")
    system.receiver_initiated()
    
    print("\nSymmetrically-Initiated Load Balancing:")
    system.symmetrically_initiated()
    
    print("\nFinal System State:")
    system.display()

if __name__ == "__main__":
    main()
