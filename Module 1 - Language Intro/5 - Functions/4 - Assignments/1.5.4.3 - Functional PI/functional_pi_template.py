import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
    # set variables from Gauss_Legendre algorithm
    a = 1
    b = 1 / math.sqrt(2)
    t = 1 / 4
    p = 1

    for i in range(1, 10):

        a_1 = (a + b) / 2
        b_1 = math.sqrt(a * b)
        t_1 = t - (p * ((a_1 - a) ** 2))
        p_1 = 2 * p
        a, b, t, p = a_1, b_1, t_1, p_1
    # change this so an actual value is returned
    return ((a + b) ** 2) / (4 * t)




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
