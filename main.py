import crawler
import os
import json
from datetime import datetime, timedelta

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
                process(stock_num)
                # crawler.get_data(stock_num)

        except ValueError:
            # Handle the case where the user didn't enter a valid integer
            print("Invalid input. Please enter a valid integer.")

def process(stock_num):
    json_path = f"data/{stock_num}/{stock_num}.json"
    directory_path = f"data/{stock_num}"
    # if isNeedUpdate(stock_num):
    print(f"isNeedUpdate : {isNeedUpdate(stock_num)}")
    # if not os.path.exists(json_path):
    #     if not os.path.exists(directory_path):
    #         # If not, create the directory
    #         os.makedirs(directory_path)
    #     print(f"json path {json_path} is not exist. start creating")
    #     current_datetime = datetime.now()
    #     date_string = current_datetime.strftime("%Y-%m-%d")
    #     data = {"update_date":date_string}
    #     with open(json_path, 'w') as json_file:
    #         json.dump(data, json_file)
    #     print(f"json path {json_path} create done")

    # else:
    #     with open(json_path, "r") as json_file:
    #         parse_data = json.load(json_file)
    #     json_date = parse_data["update_date"]
    #     print(f"json path {json_path} is exist. date : data = {json_date}. type = {type(json_date)}")
    #     obj_date = datetime.strptime(json_date, "%Y-%m-%d").date()
    #     print(f"date = {obj_date}. type = {type(obj_date)}")

def isNeedUpdate(stock_num):
    json_path = f"data/{stock_num}/{stock_num}.json"
    if not os.path.exists(json_path):
        return True
    
    cur_date = datetime.now().date()
    with open(json_path, "r") as json_file:
        parse_data = json.load(json_file)
    pre_date = datetime.strptime(parse_data["update_date"], "%Y-%m-%d").date()
    # Calculate the difference between the two datetimes
    time_difference = cur_date - pre_date

    # Check if the difference is over 30 days
    if time_difference > timedelta(days = 30):
        return True
    return False


if __name__ == "__main__":
    main()