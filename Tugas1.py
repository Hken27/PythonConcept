# fungsi pengurangan
def minus(a, b):
    return a - b


# fungsi perkalian
def mult(a, b):
    return a * b


# fungsi pembagian
def div(a, b):
    if b == 0:
        return "Tidak bisa dibagi dengan nol"
    return a / b


print(minus(9, 5))
print(mult(2, 5))
print(div(8, 2))


def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == "-":
            return minus(tree(left_operand) - tree(right_operand))
        elif operator == "*":
            return mult(tree(left_operand) * tree(right_operand))
        elif operator == "/":
            return div(tree(left_operand) / tree(right_operand))


# Contoh pohon ekspresi : (2 + 3) * (5 - 1)
# expression_tree = ("*", ("-"), 2, 3), ("-", 5, 1)
expression_tree = ((2, '+', 3), '*', (5, '-',1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi", result)
