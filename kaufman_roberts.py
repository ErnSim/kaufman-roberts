M = 2
V = 3
t = [1, 2]
a = [0.4, 1]


def calc_x(V, M, a, t):
    x = [1] * (V + 1)
    for n in range(1, V+1):
        sum = 0
        for i in range(0, M):
            if n >= t[i]:
                sum += a[i] * t[i] * x[n - t[i]]
        x[n] = sum / n
    return x


def calc_p0(x):
    sum = 0
    for item in x:
        sum += item
    return 1 / sum


def calc_pn(x, V, M, a, t):
    P = [1] * (V + 1)
    P[0] = calc_p0(x)
    for n in range(1, V+1):
        sum = 0
        for i in range(0, M):
            if n >= t[i]:
                sum += a[i] * t[i] * P[n - t[i]]
        P[n] = sum / n
    return P


def calc_bn(P, V, t, i=1):
    sum = 0
    for n in range(V - t[i - 1] + 1, V + 1):
        sum += P[n]
    return sum


def calc_all(V, t, a, M):
    x = calc_x(V, M, a, t)
    P = calc_pn(x, V, M, a, t)
    b1 = calc_bn(P, V, t)
    b2 = calc_bn(P, V, t, i=2)

    print('x: ' + str(x))
    print('P: '+ str(P))
    print('b1: ' + str(b1))
    print('b2: ' + str(b2))


print('\nObliczenia dla M = {}, V = {}, t = {}, a = {}\n'.format(M, V, t, a))
calc_all(V, t, a,  M)
print('\n')