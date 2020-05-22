class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        else:
            return self.stack_out.pop()