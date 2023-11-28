def main():

    while(True):
        # Get an integer input from the user
        user_input = input("Enter a stock number: ")

        try:
            # Convert the input to an integer
            user_integer = int(user_input)
            if(user_integer == 0):
                break
            else:
                # Print the entered integer
                print(f"You entered: {user_integer}")

        except ValueError:
            # Handle the case where the user didn't enter a valid integer
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()