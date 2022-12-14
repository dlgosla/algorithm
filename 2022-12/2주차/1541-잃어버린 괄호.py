expression = "(" + input() + ")"

bracket_added_expression = ""
for elem in expression:
    if elem == "-":
        bracket_added_expression += ")-("
    else:
        if elem == "0":
            if (not bracket_added_expression) or (
                bracket_added_expression[-1] in ["(", "+", "-"]
            ):
                continue
        bracket_added_expression += elem

# print(bracket_added_expression)
print(eval(bracket_added_expression))
