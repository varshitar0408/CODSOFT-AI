# Menu Based Chatbot

print("===================================")
print("      WELCOME TO AI CHATBOT")
print("===================================")

name = input("Enter your name: ")

print("\nHello", name + "!")
print("I am your chatbot.\n")

while True:

    print("\n========= MENU =========")
    print("1. Greeting")
    print("2. About Chatbot")
    print("3. Tell a Joke")
    print("4. Simple Calculator")
    print("5. Motivation Quote")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # Greeting
    if choice == "1":
        print("Bot: Hello! Hope you are doing well.")

    # About chatbot
    elif choice == "2":
        print("Bot: I am a Rule-Based Chatbot created using Python.")

    # Joke
    elif choice == "3":
        print("Bot: Why did the computer go to the doctor?")
        print("Bot: Because it caught a virus!")

    # Calculator
    elif choice == "4":

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        print("\nSelect Operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        op = input("Choose operation: ")

        if op == "1":
            print("Result =", num1 + num2)

        elif op == "2":
            print("Result =", num1 - num2)

        elif op == "3":
            print("Result =", num1 * num2)

        elif op == "4":
            print("Result =", num1 / num2)

        else:
            print("Invalid operation")

    # Motivation quote
    elif choice == "5":
        print("Bot: Believe in yourself and keep learning!")

    # Exit
    elif choice == "6":
        print("Bot: Goodbye", name + "!")
        break

    # Invalid choice
    else:
        print("Bot: Invalid choice. Please try again.")