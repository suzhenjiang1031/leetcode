class Queue:
    def __init__(self):
        # 使用列表存储队列元素
        self.items = []

    def is_empty(self):
        """判断队列是否为空"""
        return len(self.items) == 0

    def enqueue(self, item):
        """入队操作，将元素添加到队尾"""
        self.items.append(item)

    def dequeue(self):
        """出队操作，从队首移除并返回元素"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        # pop(0) 从列表头部弹出元素，但时间复杂度为 O(n)
        return self.items.pop(0)

    def size(self):
        """返回队列中元素的数量"""
        return len(self.items)


# 示例使用
if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    print("队列大小:", q.size())  # 输出：队列大小: 3
    print("出队元素:", q.dequeue())  # 输出：出队元素: 10
    print("出队元素:", q.dequeue())  # 输出：出队元素: 20
    print("队列是否为空:", q.is_empty())  # 输出：队列是否为空: False
    print("出队元素:", q.dequeue())  # 输出：出队元素: 30
    print("队列是否为空:", q.is_empty())  # 输出：队列是否为空: True
