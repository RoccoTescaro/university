
operators = ['!', '&', '|', '=>', '<=>']

def validate_bnf(tokens):

    if len(tokens) == 1 and tokens[0] not in operators:
        return True
    
    expected_variable = True
    parentesis_index_stack = []
    for i, token in enumerate(tokens):
        if token == '(':
            #expected_variable = False
            parentesis_index_stack.append(i)
        elif token == ')':
            if len(parentesis_index_stack) == 0:
                return False
            start_index = parentesis_index_stack.pop()
            if not validate_bnf(tokens[start_index+1:i]):
                return False
        else:
            if token == "!":
                continue
            if (expected_variable and token in operators) or (not expected_variable and token not in operators):
                return False
            else:
                expected_variable = not expected_variable
    
    if len(parentesis_index_stack) != 0:
        return False
    
    return True  

test_case = "! ( A => B ) & B | ( C | ! D )"
tokens = test_case.split()
print(test_case)
print(validate_bnf(tokens))

def left_token(index, tokens):
    left_parenthesis_count = 0
    right_parenthesis_count = 0
    for i in range(index-1, -1, -1):
        if tokens[i] == ')':
            right_parenthesis_count += 1
        elif tokens[i] == '(':
            left_parenthesis_count += 1
        if left_parenthesis_count > right_parenthesis_count:
            return tokens[i+1:index] 
    return tokens[i:index]

def right_token(index, tokens):
    i = index + 1
    left_parenthesis_count = 0
    right_parenthesis_count = 0
    for i in range(index+1, len(tokens)):
        if tokens[i] == "(":
            left_parenthesis_count += 1
        elif tokens[i] == ")":
            right_parenthesis_count += 1
        if left_parenthesis_count < right_parenthesis_count:
            return tokens[index+1:i]
    return tokens[index+1:i+1]

def negate(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] == "!":
            i += 1
            continue
        elif tokens[i] == "&":
            tokens[i] = "|"
        elif tokens[i] == "|":
            tokens[i] = "&"
        elif tokens[i] == "(":
            tokens = tokens[:i] + ["!"] + tokens[i:]
            unresolved_parentesis = 1
            index = i+2
            while tokens[index] != ")" and unresolved_parentesis != 0:
                index += 1 
                if tokens[index] == "(":
                    unresolved_parentesis += 1
                elif tokens[index] == ")":
                    unresolved_parentesis -= 1
            i = index
        else:
            tokens = tokens[:i] + ["!"] + tokens[i:]
            i += 1
        i += 1
    return tokens

def bnf_to_cnf(tokens):
    # Replace <=>
    while "<=>" in tokens:
        index = tokens.index("<=>")
        left = left_token(index, tokens)
        right = right_token(index, tokens)
        tokens = tokens[:index-len(left)] + ["("] +  left + ["=>"] + right + [")", "&"] + ["("] + right + ["=>"] + left + [")"] + tokens[index+1+len(right):]

    # Replace =>
    while "=>" in tokens:
        index = tokens.index("=>")
        left = left_token(index, tokens)
        right = right_token(index, tokens)
        tokens = tokens[:index-len(left)] + ["!","("] + left + [")","|"] + right + tokens[index+1+len(right):]

    # Move negation inwards
    found = True
    while found:
        found = False
        for i in range(len(tokens)-1):
            if tokens[i] == "!" and tokens[i+1] == "(":
                # Remove the negation
                tokens = tokens[:i] + tokens[i+1:]
                # Find the end of the expression
                unresolved_parentesis = 1
                index = i+1
                while index < len(tokens) and unresolved_parentesis != 0:
                    if tokens[index] == "(":
                        unresolved_parentesis += 1
                    elif tokens[index] == ")":
                        unresolved_parentesis -= 1
                    index += 1
                # Apply De Morgan's Law
                tokens = tokens[:i+1] + negate(tokens[i+1:index-1]) + tokens[index-1:]
                found = True

    #simplify negations
    i = 0
    while i < len(tokens)-1:
        if tokens[i] == "!" and tokens[i+1] == "!":
            tokens = tokens[:i] + tokens[i+2:]
            i -= 2
        i += 1
    
    # Distribute OR over AND
    # simplify parentesis
    parentesis_index_stack = []
    i = 0 
    while i < len(tokens)-1:
        if tokens[i] == "(":
            parentesis_index_stack.append(i)
        elif tokens[i] == ")":
            start_index = parentesis_index_stack.pop()
            first_operator = None
            remove_parentesis = True
            for j in range(start_index+1, i):
                if tokens[j] in ["&", "|"]:
                    if first_operator is None:
                        first_operator = tokens[j]
                    elif tokens[j] != first_operator:
                        remove_parentesis = False
                        break
            if remove_parentesis:
                tokens = tokens[:start_index] + tokens[start_index+1:i] + tokens[i+1:]    
                i = start_index      
        i += 1   

    return " ".join(tokens)

print(bnf_to_cnf(tokens))