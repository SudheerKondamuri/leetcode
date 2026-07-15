
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Pushes element x and rotates the queue so x sits at the front.
        Time Complexity: O(N)
        """
        self.q.append(x)
        # Rotate all previous elements to the back
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes and returns the top element from the front.
        Time Complexity: O(1)
        """
        if self.empty():
            raise IndexError("pop from an empty stack")
        return self.q.popleft()

    def top(self) -> int:
        """
        Returns the top element (always at index 0).
        Time Complexity: O(1)
        """
        if self.empty():
            raise IndexError("top from an empty stack")
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
