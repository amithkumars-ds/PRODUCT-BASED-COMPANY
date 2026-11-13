class Processor:
    def process(self):
        return "Processing data"

class Memory:
    def load(self):
        return "Loading data into memory"

class Computer:
    def __init__(self,
                 processor_obj:Processor=None,
                 memory_obj:Memory=None):
        self.processor = processor_obj
        self.memory = memory_obj

    def run(self):
        return self.processor.process() + "\n" + self.memory.load()


if __name__ == "__main__":
    processor = Processor()
    memory = Memory()

    computer = Computer(processor, memory)

    print(computer.run())
    print(computer.processor is processor)
    print(computer.memory is memory)
