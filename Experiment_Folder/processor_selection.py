import random

class Processor:
    def __init__(self, processor_id, load=0):
        self.processor_id = processor_id
        self.load = load

    def __repr__(self):
        return f"Processor {self.processor_id}: Load {self.load}"

class System:
    def __init__(self, num_processors):
        self.processors = [Processor(i) for i in range(num_processors)]

    def display(self):
        for processor in self.processors:
            print(processor)

    def sequential_selection(self, task_load):
        print("\nSequential Processor Selection:")
        for i, processor in enumerate(self.processors):
            print(f"Assigning task with load {task_load} to Processor {processor.processor_id}")
            processor.load += task_load
            if i == len(self.processors) - 1:
                print(f"All processors are assigned tasks sequentially.")
                break

    def random_selection(self, task_load):
        print("\nRandom Processor Selection:")
        processor = random.choice(self.processors)
        print(f"Assigning task with load {task_load} to Processor {processor.processor_id}")
        processor.load += task_load

    def direct_neighbor_selection(self, task_load):
        print("\nDirect Neighbor Processor Selection:")
        for i in range(len(self.processors)):
            if i < len(self.processors) - 1:
                processor = self.processors[i + 1]  # Select the next processor as the neighbor
                print(f"Assigning task with load {task_load} to Processor {processor.processor_id}")
                processor.load += task_load
                break
            else:
                processor = self.processors[i]  # For the last processor, select itself as the neighbor
                print(f"Assigning task with load {task_load} to Processor {processor.processor_id}")
                processor.load += task_load

def main():
    system = System(5)
    task_load = 10

    print("Initial System State:")
    system.display()

    system.sequential_selection(task_load)
    system.display()

    system.random_selection(task_load)
    system.display()

    system.direct_neighbor_selection(task_load)
    system.display()

if __name__ == "__main__":
    main()
