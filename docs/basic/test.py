
class Queue:
    def __init__(self,size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0      # 队尾 进队
        self.front = 0     # 队首 出队

    def push(self,element):
        """增加"""
        if not self.is_fulled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is full")

    def pop(self):
        """删除"""
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            return None

    def is_empty(self):
        """判断队列是否为空 图1"""
        return self.rear == self.front

    def is_fulled(self):
        """判断队列是否为满"""
        return (self.rear + 1) % self.size == self.front



if __name__ == '__main__':
    q = Queue(5)
    for i in range(4):
        q.push(i)
    print(q.is_fulled())    # 查看队列是否满
    print(q.pop())
    print(q.pop())
    print(q.queue[(q.front + 1):])

