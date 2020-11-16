def convert(number):
    divisor_dict = {3:"Pling", 5:"Plang", 7:"Plong"};
    output = ""
    for key, val in divisor_dict.items():
        if number % key == 0:
            output += val
    
    return output if len(output) != 0 else str(number)