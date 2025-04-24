def modify_file_content(content):
    # Example modification: convert to uppercase
    return content.upper()

def main():
    input_filename = input("Enter the filename to read: ")

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied to read the file '{input_filename}'.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    modified_content = modify_file_content(content)

    output_filename = "modified_" + input_filename
    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to '{output_filename}'.")
    except