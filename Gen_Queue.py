# General Queue Program
n = int(input("Enter queue size: "))
queue = [0] * n
front = -1
rear = -1

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        if rear == n - 1:
            print("Queue is full")
        else:
            x = int(input("Enter element: "))
            if front == -1:
                front = 0
            rear = rear + 1
            queue[rear] = x

    elif ch == 2:
        if front == -1 or front > rear:
            print("Queue is empty")
        else:
            print("Deleted element:", queue[front])
            front = front + 1

            if front > rear:
                front = -1
                rear = -1

    elif ch == 3:
        if front == -1:
            print("Queue is empty")
        else:
            for i in range(front, rear + 1):
                print(queue[i], end=" ")
            print()

    elif ch == 4:
        break

    else:
        print("Invalid choice")
