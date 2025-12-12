def decimal_to_binary(decimal):
    binary = [ ]
    while True:
        binary_variable = int(decimal)%2
        if binary_variable in ('1','0'):
            binary.append(binary_variable)
            if decimal== "0":
                msg = f"{decimal} in binary is {binary}"
                return msg
            break
        else:
            print(f"Error")

decimal_to_binary(input())