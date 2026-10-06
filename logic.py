def feedback(code, guess):
    exact = 0
    partial = 0

    remaining_code = []
    remaining_guess = []

    for c, g in zip(code, guess):
        if c == g:
            exact += 1
        else:
            remaining_code.append(c)
            remaining_guess.append(g)

    for g in remaining_guess:
        if g in remaining_code:
            partial += 1
            remaining_code.remove(g)

    return exact, partial