user_input = input("Enter some text: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")


append_input = input("Enter more text to append: ")
with open("output.txt", "a") as file:
    file.write(append_input + "\n")

print("\n--- Final Content of output.txt ---")
with open("output.txt", "r") as file:
    print(file.read())
