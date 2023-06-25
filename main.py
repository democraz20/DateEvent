import os
import datetime

def create_file():
    # Create a new text file if it doesn't exist, or continue from the latest date if it does
    if os.path.exists('dates.txt'):
        with open('dates.txt', 'r') as file:
            dates = file.read().splitlines()
            latest_date = dates[-1]
            starting_date = datetime.datetime.strptime(latest_date, '%d-%m-%Y').date()
    else:
        starting_date = datetime.datetime.strptime(input("Enter the starting date (DD-MM-YYYY): "), '%d-%m-%Y').date()
        with open('dates.txt', 'w') as file:
            file.write(starting_date.strftime('%d-%m-%Y') + '\n')

    ending_date = datetime.datetime.strptime(input("Enter the ending date (DD-MM-YYYY): "), '%d-%m-%Y').date()

    # Event loop
    while True:
        current_date = starting_date.strftime('%d-%m-%Y')
        print("Processing date:", current_date)

        # Run the command "c -d 'Month DD YYYY'" (replace with your actual command)
        # Your command can be executed using subprocess or any other method suitable for your needs
        # For demonstration purposes, we'll simply print the command.
        time_str = starting_date.strftime('%B %d 00:01:00 %Y')
        command = f"git commit -m \"{current_date}\" --date \"{time_str}\""
        print("Executing command:", command)
        os.system("git add .")
        os.system(command)

        # Append the current date to the file
        with open('dates.txt', 'a') as file:
            file.write(current_date + '\n')

        # Check if the current date is the ending date
        if current_date == ending_date.strftime('%d-%m-%Y'):
            break

        # Move to the next date
        starting_date += datetime.timedelta(days=1)

if __name__ == "__main__":
    create_file()
