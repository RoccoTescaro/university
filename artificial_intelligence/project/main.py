import random
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.parent = None
        self.left = left
        self.right = right


operators_precedence = {
    "!": 4,
    "&": 3,
    "|": 2,
    "=>": 1,
    "<=>": 0
}

operators = {
    "!": lambda left: Node("!", left=left),
    "&": lambda left, right: Node("&", left=left, right=right),
    "|": lambda left, right: Node("|", left=left, right=right),
    "=>": lambda left, right: Node("=>", left=left, right=right),
    "<=>": lambda left, right: Node("<=>", left=left, right=right)
}

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
    
    if tokens[-1] in operators:
        return False
    
    if len(parentesis_index_stack) != 0:
        return False
    
    return True  


# Shuting yard algorithm
def setup_tree(sentence):
    tokens = sentence.split()
    prefix = []
    operator_stack = []
    tokens = tokens[::-1]  
    for token in tokens:
        if token not in operators and token not in ["(", ")"]:
            prefix.append(token)
        elif token in operators and not operator_stack:
            operator_stack.append(token)
        elif operator_stack:
            if token == ")":
                operator_stack.append(token)
            elif token == "(":
                while operator_stack and operator_stack[-1] != ")":
                    prefix.append(operator_stack.pop())
                if operator_stack:
                    operator_stack.pop()
            elif operator_stack[-1] == ")" or operators_precedence[token] >= operators_precedence[operator_stack[-1]]:
                operator_stack.append(token)
            else:
                while operator_stack and operator_stack[-1] != ")" and operators_precedence[token] < operators_precedence[operator_stack[-1]]:
                    prefix.append(operator_stack.pop())
                operator_stack.append(token)
    while operator_stack:
        prefix.append(operator_stack.pop())
    return prefix

def str_to_bnf(sentence):
    tokens = setup_tree(sentence)

    def make_tree():
        node = None
        if tokens[-1] not in operators and tokens[-1] not in ["(", ")"]:
            return Node(tokens.pop())
        elif tokens[-1] in operators:
            token = tokens.pop()
            if token == "!":
                node = operators[token](make_tree())
            else:
                node = operators[token](make_tree(), make_tree())
            return node

    return make_tree()

def print_tree(root):
    if not root:
        return
    if not root.left: #is a variable
        print(root.value, end=' ')
    elif not root.right: #is a negation
        print(root.value, end=' ')
        print_tree(root.left)
    else:
        print("(", end=' ')
        print_tree(root.left)
        print(root.value, end=' ')
        print_tree(root.right)
        print(")", end=' ')

def remove_biconditional(root):
    if not root or not root.left:
        return
    
    if root.value == "<=>":
        root.value = "&"
        temp_left = root.left
        temp_right = root.right
        root.left = operators["=>"](temp_left, temp_right)
        root.right = operators["=>"](temp_right, temp_left)

    remove_biconditional(root.left)
    remove_biconditional(root.right)

def remove_implication(root):
    if not root or not root.left:
        return
    
    if root.value == "=>":
        root.value = "|"
        temp_left = root.left
        root.left = operators["!"](temp_left)
    
    remove_implication(root.left)
    remove_implication(root.right)

def move_neagation_inward(root):
    if not root:
        return
    
    if root.value == "!":
        demorgan = ["&", "|"]
        if root.left.value == "!":
            temp_left = root.left.left
            root.value = temp_left.value
            root.left = temp_left.left
            root.right = temp_left.right
        elif root.left.value in demorgan: 
            root.value = demorgan[root.left.value == "&"]
            temp_left = root.left
            root.left = operators["!"](temp_left.left)
            root.right = operators["!"](temp_left.right)
                
    move_neagation_inward(root.left)
    move_neagation_inward(root.right)

def update_parents(root):
    if not root:
        return

    if root.left:
        root.left.parent = root
        update_parents(root.left)
    if root.right:
        root.right.parent = root
        update_parents(root.right)

def distribute_or_over_and(root):
    if not root:
        return
    
    if root.value == "|":
        if root.left.value == "&":
            temp_ll = root.left.left
            temp_lr = root.left.right
            temp_r = root.right
            root.value = "&"
            root.left = operators["|"](temp_ll, temp_r)
            root.right = operators["|"](temp_lr, temp_r)
            
            #update parents            
            root.left.left.parent = root.left
            root.left.right.parent = root.left
            root.right.left.parent = root.right
            root.right.right.parent = root.right

            if root.parent and root.parent.value == "|":
                distribute_or_over_and(root.parent)
        
        if root.right.value == "&":
            temp_rl = root.right.left
            temp_rr = root.right.right
            temp_l = root.left
            root.value = "&"
            root.left = operators["|"](temp_rl, temp_l)
            root.right = operators["|"](temp_rr, temp_l)

            #update parents
            root.left.left.parent = root.left
            root.left.right.parent = root.left
            root.right.left.parent = root.right
            root.right.right.parent = root.right

            if root.parent and root.parent.value == "|":
                distribute_or_over_and(root.parent)
    
    distribute_or_over_and(root.left)
    distribute_or_over_and(root.right)


def bnf_to_cnf(root):
    #Remove <=> operator
    remove_biconditional(root)
    #Remove => operator
    remove_implication(root)
    #Move negation inwards
    move_neagation_inward(root)
    #Disribute | over &
    update_parents(root)
    distribute_or_over_and(root)

def generate_random_bnf(number_of_variables, number_of_repetitions, operators_prob=[0.1,0.3,0.3,0.2,0.1]):
    #generate variables name
    variables = ["x_"+str(i+1) for i in range(number_of_variables)]

    variables_repeated = variables.copy()
    for _ in range(number_of_repetitions):
        variables_repeated.append(random.choice(variables))
    random.shuffle(variables_repeated)
 
    def generate_bnf(_variables):
        if not _variables:
            return ""
        
        if _variables and len(_variables) == 1:
            #choose between variable and variable negation
            return random.choice([_variables[0], "! " + _variables[0]])
        
        operator = random.choices(["!", "&", "|", "=>", "<=>"], operators_prob)[0]
        if operator == "!":
            return operator + " " + generate_bnf(_variables)  
    
        left = generate_bnf(_variables[:len(_variables)//2])
        right = generate_bnf(_variables[len(_variables)//2:])
        return "( " + left + " " + operator + " " + right + " )"
    
    return generate_bnf(variables_repeated)

def cnf_to_str(root):
    if not root:
        return ""
    if not root.left:
        return root.value
    if root.value == "!":
        return root.value + " " + cnf_to_str(root.left)
    if root.value == "&":
        left_str = cnf_to_str(root.left)
        right_str = cnf_to_str(root.right)
        if root.left.value == "|":
            left_str = "( " + left_str + " )"
        if root.right.value == "|":
            right_str = "( " + right_str + " )"
        return left_str + " " + root.value + " " + right_str
    return cnf_to_str(root.left) + " " +  root.value + " " + cnf_to_str(root.right)


def test(n_test, n_variables, n_repetitions, invalid=False):
    for i in range(n_test):
        test_case = generate_random_bnf(n_variables, n_repetitions)
        tokens = test_case.split()
        if invalid:
            random_operator = random.choice(["!", "&", "|", "=>", "<=>"]) 
            random_index = random.randint(0, len(tokens)-1)          
            while tokens[random_index] in operators:
                random_index = random.randint(0, len(tokens)-1)
            tokens[random_index] = random_operator
            if validate_bnf(tokens):
                print("Invalid test case not detected")
                print(" ".join(tokens))
                return
        else:
            if not validate_bnf(tokens):
                print("Invalid test case detected")
                print(test_case)
                return
            
            tree = str_to_bnf(test_case)
            bnf_to_cnf(tree)
            print(cnf_to_str(tree))   


def test_string(test_case):
    tokens = test_case.split()
    if not validate_bnf(tokens):
        print("Invalid test case detected")
        print(test_case)
        return
        
    tree = str_to_bnf(test_case)
    bnf_to_cnf(tree)
    print(cnf_to_str(tree))


# test(100, 3, 2)
# test(100, 3, 2, invalid=True)
# test_string("( A & B ) | ( C & D )")
