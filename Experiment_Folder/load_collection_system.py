import random
import time

# Node class represents each individual node in the system
class Node:
    def __init__(self, node_id, load, group_id):
        self.node_id = node_id
        self.load = load
        self.group_id = group_id
        self.is_leader = False

# System class represents the entire system of nodes
class System:
    def __init__(self, num_nodes):
        self.nodes = []
        self.groups = {}
        self.leaders = {}

        for i in range(num_nodes):
            node = Node(i, random.randint(1, 100), i % 3)
            self.nodes.append(node)
            if node.group_id not in self.groups:
                self.groups[node.group_id] = []
            self.groups[node.group_id].append(node)

        for group_id in self.groups:
            leader = random.choice(self.groups[group_id])
            leader.is_leader = True
            self.leaders[group_id] = leader

    def centralized_load_collection(self, group_id):
        total_load = sum(node.load for node in self.groups[group_id])
        return total_load

    def broadcast_load_data(self):
        data = {}
        for node in self.nodes:
            data[node.node_id] = node.load
        return data

    def group_communication(self, group_id):
        group_leader = self.leaders[group_id]
        total_load = sum(node.load for node in self.groups[group_id] if node.node_id != group_leader.node_id)
        total_load += group_leader.load
        return total_load

    def hybrid_load_collection(self):
        total_system_load = sum(node.load for node in self.nodes)
        if total_system_load < 200:
            return {group_id: self.centralized_load_collection(group_id) for group_id in self.groups}
        elif total_system_load < 500:
            return {group_id: self.group_communication(group_id) for group_id in self.groups}
        else:
            return self.broadcast_load_data()

# To make this module importable, don't run the code automatically:
if __name__ == "__main__":
    random.seed(time.time())
    system = System(10)
    system.hybrid_load_collection()
