# 1. Name: 
#      Lily Sorensen
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      This program is supposed to compute the number of days given between two dates. It is also supposed to account for leap years and assert any errors. 
# 4. What was the hardest part? Be as specific as possible.
#      The instructions were not very specific and I had to get a lot of clarrification from the TA. 
# 5. How long did it take for you to complete the assignment?
#      3 hours ish


# Compute whether a given year is a leap year
def is_leap_year(year):

    # A year is a leap year if it is divisible by 4. 
    # If it is divisible by 100, it must also be divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Initialize the array of days in each month (index 0 is unused, for simplicity)
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

# Validate that the year is greater than 1753
def validate_year(prompt):
    while True:
        try:
            year = int(input(prompt))
            assert year > 1753, "Error: Year must be greater than 1753"
            return year
        except (ValueError, AssertionError) as e:
            print(e)

# Validate that months are between 1 and 12
def validate_months(prompt):
    while True:
        try:
            month = int(input(prompt))
            assert 1 <= month <= 12, "Error: Month must be between 1 and 12"
            return month
        except (ValueError, AssertionError) as e:
            print(e)
    
# Validate that days are between 1 and 32
def validate_days(prompt, month):
    while True:
        try:
            day = int(input(prompt))
            assert 1 <= day <= days_in_month[month], f"Error: Day must be between 1 and {days_in_month[month]}"

            return day
        except (ValueError, AssertionError) as e:
            print(e)

def count_days():
    # Prompt the user for two dates
    first_year = validate_year("\nStart Year: ")  
    first_month = validate_months("Start month: ")
    first_day 	 = validate_days("Start day: ", first_month)		

    second_year = validate_year("End year: ")
    second_month = validate_months("End month: ")			 
    second_day 	= validate_days("End day: ", second_month)

    # Initialize total_days to 0
    total_days = 0	 		

    # Assert statements to ensure year, month, and day are valid dates
    assert first_year > 1753
    assert second_year > 1753
    assert 1 <= first_month <= 12
    assert 1 <= second_month <= 31
    assert 1 <= first_day <= 31
    assert 1 <= second_day <= 31

    # Case 1: Same month, same year
    if first_month == second_month and first_year == second_year:	

        # Assuming the user knows the correct order of dates
        assert first_day < second_day, "First date should be smaller than second date"
        total_days = second_day - first_day

    # Case 2: Same year, different months
    elif first_year == second_year:

        # Assuming the users know the first month shoudl be before the second month
        assert first_month < second_month, "First month should be smaller than second month"

        # Add the remaining days in the first month
        total_days = total_days + (days_in_month[first_month] - first_day + 1)   

        # Add the days for all the months in between
        for month in range(first_month + 1, second_month - 1):
            total_days += days_in_month[month]			

        # Add the days of the second month
        total_days = total_days + second_day
        print("Case 2")					

    # Case 3: Different years (first_year < second_year)
    elif first_year != second_year:			

        # Assuming the user knows the first year should be smaller than the second year
        assert first_year < second_year, "First year should be smaller than second year"	  
        
        # Add the remaining days in the first year until the end of that year
        total_days += (days_in_month[first_month] - first_day + 1)    

        # Add the days in the first year from January to first_month-1
        for month in range(first_month + 1, 12):            
            total_days += days_in_month[month]      

        # Loop over full years between first_year and second_year-1
        for year in range(first_year + 1, second_year -1):                
            if is_leap_year(year):                         
                total_days += 366                        
            else:
                total_days += 365                        

        # Add the days in the second year from January to second month
        for month in range(1, second_month -1):                
            total_days += days_in_month[month]					 						

        # Add the days in the second month up to the second day
        total_days += second_day
        print("Case 3")			

    # Case 4: Adjust for leap years (if necessary)
    if is_leap_year(first_year) and first_month <= 2:				
        total_days = total_days + 1   						

    if is_leap_year(second_year) and second_month > 2: 			
        total_days = total_days + 1 						

    # Output the total number of days
    print("Total days between the two dates: " + str(total_days))		

if __name__ == "__main__":
    count_days()