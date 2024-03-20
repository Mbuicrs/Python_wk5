# Task 1: File Creation
try:
    # Create a new file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is my story dated 20-03-2024 \n")
        file.write("Why 2+2 in algebra soo complicate?\n")    # Write three lines of text (mix of strings and numbers)
        file.write("Python is awesome as is help cut out algebra explanations!\n")
    print("File 'my_file.txt' created successfully!")

    # Task 2: File Reading and Display
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of 'my_file.txt':")
        print(contents)

    # Task 3: File Appending
    with open("my_file.txt", "a") as file:
        file.write("Here is where things gets intresting\n")
        file.write("County 047 - Nairobi!.\n")
        file.write("County code 001 - Mombasa\n")
        file.write("WHO THE *** DEVELOPED THIS NAMING SYSTEM?\n")
    print("File 'my_file.txt' updated successfully!")

except FileNotFoundError:   # Handles file not found errror
    print("File not found. Please check the file name.")
except PermissionError:     # Handles access restriction errror
    print("Permission denied. Make sure you have the necessary permissions.")
finally:
    print("Error handling completed.")
