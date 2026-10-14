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
        if (rear + 1) % n == front:
            print("Queue is full")
        else:
            x = int(input("Enter element: "))
            if front == -1:
                front = 0
            rear = (rear + 1) % n
            queue[rear] = x

    elif ch == 2:
        if front == -1:
            print("Queue is an empty")
        else:
            print("Deleted element:", queue[front])

            if front == rear:
                front = -1
                rear = -1
            else:
                front = (front + 1) % n

    elif ch == 3:
        if front == -1:
            print("Queue is empty")
        else:
            i = front
            while True:
                print(queue[i], end=" ")
                if i == rear:
                    break
                i = (i + 1) % n
            print()

    elif ch == 4:
        break

    else:
        print("Invalid choice")