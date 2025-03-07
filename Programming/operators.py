def arithmatic_operators():
    A = 10
    B = 20
    return f"A + B = {A+B}, A - B = {A-B}, A X B = {A*B}, A / B = {A/B}"


def inc_dec_operators():
    A = 10
    B = 20
    [print(i, end=' ') for i in range(A)]
    return f'A before increment {A}, A after increment {A+1}, B before decrement {B}, B after decrement {B+1}'


def equals_or_not():
    A = 10
    B = 10
    if A == B:
        return "A and B are equals"
    else:
        return "A and B are not equals"


def relational_operators():
    A = 10
    if A > 10:
        return "A is greater than ten"
    else:
        return "A is less than ten"


def smaller_or_larger():
    A = 10
    B = 20
    if A > B:
        return "A is larger than B"
    else:
        return "A is smaller than B"


print(arithmatic_operators())
print(inc_dec_operators())
print(equals_or_not())
print(relational_operators())
print(smaller_or_larger())
