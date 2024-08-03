def cidr(value):
    if value == 0:
        print("Total # of possible nodes: 4,294,967,296")
    elif value == 1:
        print("Total # of possible nodes: 2,147,483,648")
    elif value == 2:
        print("Total # of possible nodes: 1,073,741,824")
    elif value == 3:
        print("Total # of possible nodes: 536,870,912")
    elif value == 4:
        print("Total # of possible nodes: 268,435,456")
    elif value == 5:
        print("Total # of possible nodes: 134,217,728")
    elif value == 6:
        print("Total # of possible nodes: 67,108,864")
    elif value == 7:
        print("Total # of possible nodes: 33,554,432")
    elif value == 8:
        print("Total # of possible nodes: 16,777,216")
    elif value == 9:
        print("Total # of possible nodes: 8,388,608")
    elif value == 10:
        print("Total # of possible nodes: 4,194,304")
    elif value == 11:
        print("Total # of possible nodes: 2,097,152")
    elif value == 12:
        print("Total # of possible nodes: 1,048,576")
    elif value == 13:
        print("Total # of possible nodes: 524,288")
    elif value == 14:
        print("Total # of possible nodes: 262,144")
    elif value == 15:
        print("Total # of possible nodes: 131,072")
    elif value == 16:
        print("Total # of possible nodes: 65,536")
    elif value == 17:
        print("Total # of possible nodes: 32,768")
    elif value == 18:
        print("Total # of possible nodes: 16,384")
    elif value == 19:
        print("Total # of possible nodes: 8,192")
    elif value == 20:
        print("Total # of possible nodes: 4,096")
    elif value == 21:
        print("Total # of possible nodes: 2,048")
    elif value == 22:
        print("Total # of possible nodes: 1,024")
    elif value == 23:
        print("Total # of possible nodes: 512")
    elif value == 24:
        print("Total # of possible nodes: 256")
    elif value == 25:
        print("Total # of possible nodes: 128")
    elif value == 26:
        print("Total # of possible nodes: 64")
    elif value == 27:
        print("Total # of possible nodes: 32")
    elif value == 28:
        print("Total # of possible nodes: 16")
    elif value == 29:
        print("Total # of possible nodes: 8")
    elif value == 30:
        print("Total # of possible nodes: 4")
    elif value == 31:
        print("Total # of possible nodes: 2")
    elif value == 32:
        print("Total # of possible nodes: 1")

while True:
    try:
        user_input = int(input("Enter CIDR value (0, 1, 2) or 100 to exit: "))
        if user_input == 100:
            print("Exiting program.")
            break
        elif user_input in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]:
            cidr(user_input)
        else:
            print("Invalid CIDR value. Please enter a CIDR from 0-32 or 100 to exit.")
    except ValueError:
        print("Invalid input. Please enter an integer value.")