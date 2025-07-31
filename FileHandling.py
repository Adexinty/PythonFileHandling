def read_file():
    try:
        # Ask the user for a filename (without ".txt")
        filename = input("Enter the filename (without extension): ")
        
        # Append ".txt" to the filename
        full_filename = f"{filename}.txt"

        # Attempt to open and read the file
        with open(full_filename, 'r') as file:
            content = file.read()
            print("\nFile Content:\n")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{full_filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read the file '{full_filename}'.")

# Run the function
read_file()

