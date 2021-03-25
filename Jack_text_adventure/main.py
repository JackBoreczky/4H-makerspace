# Types of values:
string = "this is a string"

running = True

num_loops = 10

for i in range(10):
    print(i)

while running:
    name = input("Hello! please tell me who you are: ")

    print(name)

    if name == "Jack":
        print("You're our favorite!")
    elif name == "Luke":
        print("You're not allowed into my program")
        running = False
    else:
        print("You're not Jack")

    num_loops = num_loops - 1

    # Jump back to the while and check the condition

print("Goodbye!")
