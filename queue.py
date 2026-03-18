queue = []

# enqueue (add element)
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# dequeue (remove element)
queue.pop(0)
print("After dequeue:", queue)

# front element
print("Front:", queue[0])
