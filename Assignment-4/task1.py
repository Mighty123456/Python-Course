try:
    with open("sample.txt", "r") as file:
        print("--- File Content ---")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
