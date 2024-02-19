result = "("
start = 0
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open("output.txt", "w") as file:
    for month in months:
        # Initialize result for each month
        result = "("
        
        for i in range(start + 1, start + month + 1):
            result += f"UP_Rainfall_2012@{i}+"

        result = result[:-1]  # Remove the trailing "+"
        result += f")/{month}"
        
        # Write the result to the file
        file.write(f"{result}\n")
        
        start = month + start