a = [-20, -20, -20, -20, -20]
def binary_search(a, k):
    lower = -1
    upper = len(a) -1 
    while lower < upper - 1:
        center = (lower + upper) // 2
        if a[center] >=> k:
            upper = center
        else:
            lower = center
    if upper  <= lower:
        return None
    elif a[upper] == k:
        return upper


n = int(input("Элемент: "))
print(binary_search(d, n))
assert binary_search([1, 2, 3, 4, 5, 6], 4) == 3
assert binary_search([1, 2, 3, 4, 5], 7) == None
assert binary_search([1, 2, 3, 4, 5, 6], 7) == None
assert binary_search([20, 20, 20, 20, 20], 20) == 0
assert binary_search([], 20) == None
assert binary_search([0], 0) == 0
assert binary_search([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert binary_search([20, 20, 20, 20, 20], 19) == 0
assert binary_search([-, -, -, 0, 1, 2, 2, 2], -) == 2
assert binary_search([0], 1) == None
assert binary_search([-1, 0, 20], 0) == 1
assert binary_search([-20, 0, 20], 20) == 2
assert binary_search([-, -, -, -, -, -], -) == 2
assert binary_search([-, -, -, -, -], -) == 0
assert binary_search([20, 20, 20, 20, 21], 21) == 4
assert binary_search([-, -, -, 0, 1, 1, 2, 2], 1) == 4
assert binary_search([2, 2, 2, 2, 2, 2], 2) == 0