def format_data(data):
    # Function to format scraped data
    formatted_data = data.strip().title()
    return formatted_data

def save_to_file(data, filename):
    # Function to save data to a file
    with open(filename, 'w') as file:
        file.write(data)

def read_from_file(filename):
    # Function to read data from a file
    with open(filename, 'r') as file:
        return file.read()

def log_message(message):
    # Function to log messages to the console
    print(f"[LOG] {message}")