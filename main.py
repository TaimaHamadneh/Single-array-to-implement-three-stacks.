class Three_Stacks:
    def __init__(self, stackSize):
        self.stackSize = stackSize
        self.array = [None] * (stackSize * 3)
        self.pointers = [0, stackSize, 2 * stackSize]

    def push(self, stack_num, value): # three stacks, stack_num [0 or 1 or 2], value = any elements
        if self.is_full(stack_num):
            print(f"Stack {stack_num} is full.")
            return
        self.array[self.pointers[stack_num]] = value  ## Ex: p[0] = 1
        self.pointers[stack_num] += 1 #p --> 1

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            print(f"Stack {stack_num} is empty.")
            return None
        self.pointers[stack_num] -= 1
        value = self.array[self.pointers[stack_num]]
        self.array[self.pointers[stack_num]] = None
        return value

    def is_full(self, stack_num):
        return self.pointers[stack_num] == (stack_num + 1) * self.stackSize

    def is_empty(self, stack_num):
        return self.pointers[stack_num] == stack_num * self.stackSize


three_stacks = Three_Stacks(3)
three_stacks.push(0, 1)
three_stacks.push(1, 2)
three_stacks.push(2, 3)


print(three_stacks.array)  # Output: [1, None, None, 2, None, None, 3, None, None]
