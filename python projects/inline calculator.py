operators = ["+","-", "^","%","*",".","<",">","(",")","/","="]
digits = []
used_operators = []
problem = "1-23(1.3+0.45)"
operand_message = "The Operands are: "
operator_message = "The Operators are: "

for operand in problem:
    if operand.isdigit():
        digits.append(operand)
    elif operand in operators:
        used_operators.append(operand)
    else:
        print(f"Error at operand {problem.index(operand)}")


for digit in digits:
    operand_message += digit + "," + " "

print(operand_message)

for operator in used_operators:
    operator_message += operator + "," + " "

print(operator_message)
print("DONE!")