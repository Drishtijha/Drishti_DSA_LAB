# Stack operation

stack = []

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = int(input("Enter element: "))
        stack.append(x)
        print("Element pushed")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Deleted element:", stack.pop())

    elif choice == 3:
        print("Stack:", stack)

    elif choice == 4:
        break

    else:
        print("Invalid choice")



# Reverse of string using stack

s = input("Enter a string: ")
stack = []

for ch in s:
    stack.append(ch)

rev = ""

while len(stack) > 0:
    rev = rev + stack.pop()
print("Reverse string:", rev)


# Matching Parentheses using stack

s = input("Enter an expression: ")
stack = []
balanced = True

for ch in s:
    if ch == '(':
        stack.append(ch)

    elif ch == ')':
        if len(stack) == 0:
            balanced = False
            break
        else:
            stack.pop()

if len(stack) != 0:
    balanced = False
if balanced:
    print("Parentheses are balanced")
else:
    print("Parentheses are not balanced")
