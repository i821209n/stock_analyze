import crawler

def main():

    while(True):
        # Get an integer input from the user
        user_input = input("Enter a stock number (press 0 to exit): ")

        try:
            # Convert the input to an integer
            stock_num = int(user_input)
            if(stock_num == 0):
                break
            else:
                # Print the entered integer
                print(f"You entered: {stock_num}")
                crawler.get_data(stock_num)

        except ValueError:
            # Handle the case where the user didn't enter a valid integer
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()