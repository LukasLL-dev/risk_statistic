#probability for a specific value to be the highest
def single(dots, value, dices):
    p = (value**dices - (value - 1)**dices)/dots**dices
    return p
#probability for a specific value to be the highest in dim place
def probability(dots, value, dices, dim):
    if dim==1:
        return single(dots, value, dices)
    elif (dim>dices):
        return 0
    else:
        k = value
        sum_prob = 0
        while k < dots+1:
            p = single(dots, k, dices)
            d = 2
            while d < dim+1:
                p = p*(value**(dices-d+1)-(value-1)**(dices-d+1))/k**(dices-d+1)
                d += 1
            sum_prob = sum_prob + p
            k += 1
        if (dots < 1) or (value > dots) or (value < 0) or (dices < 0) or (dim < 0):
            print('rethink your variables!')
        return sum_prob

#probability to lose in a specific dim
def p_lose_i(dots, dices_attack, dices_defend, dim):
    p_lose = 0
    k = 1
    while k < (dots + 1):
        l = k
        sum_of_p = 0
        while l < (dots + 1):
            sum_of_p = sum_of_p + probability(dots, l, dices_defend, dim)
            l += 1
        p_lose = p_lose+sum_of_p*probability(dots, k, dices_attack, dim)
        k += 1
    if (dots < 1) or (dices_attack < 0) or (dices_defend < 0) or (dim < 0):
        print('rethink your variables!')
    return p_lose
#probability to lose an army
def expected_lose(dots, dices_attack, dices_defend):
    expect=0
    dimension = 1
    while dimension < dices_defend+1:
        expect = expect + p_lose_i(dots, dices_attack, dices_defend, dimension)
        dimension += 1
    if (dots < 1) or (dices_attack < 0) or (dices_defend < 0):
        print('rethink your variables!')
    return expect




#probability to lose in a specific dim
def p_win_i(dots, dices_attack, dices_defend, dim):
    p_lose = 0
    k = 1
    while k < (dots + 1):
        l = k+1
        sum_of_p = 0
        while l < (dots + 1):
            sum_of_p = sum_of_p + probability(dots, l, dices_attack, dim)
            l += 1
        p_lose = p_lose+sum_of_p*probability(dots, k, dices_defend, dim)
        k += 1
    if (dots < 1) or (dices_attack < 0) or (dices_defend < 0) or (dim < 0):
        print('rethink your variables!')
    return p_lose
#probability to lose an army
def expected_win(dots, dices_attack, dices_defend):
    expect=0
    dimension = 1
    while dimension < dices_defend+1:
        expect = expect + p_win_i(dots, dices_attack, dices_defend, dimension)
        dimension += 1
    if (dots < 1) or (dices_attack < 0) or (dices_defend < 0):
        print('rethink your variables!')
    return expect
