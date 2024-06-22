import numpy as np

# Creating the state in base 10 for sake of simplicity
initial_state = np.array([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

"""
This function performs the three operations that make up a basic step.
"""
def basic_step(a, b, c, n, array):
    # Addition mod 16
    array[b] = (array[b] + array[c]) % 16
    # XOR 
    array[a] = array[a] ^ array[b]
    """
    As specificed in the question, rotate bits left 16, 12, and 8
    does not change a byte. Rotate left 7 bits is the same as 
    rotate right 1 bit. 
    """
    if (n == 7):
        if (array[a] % 2 == 1):
            array[a] = (array[a] >> 1) + 8
        else: 
            array[a] = array[a] >> 1


"""
This simple function performs four basic steps that make up a quarter round.
"""
def quarter_round(a, b, c, d, array):
    basic_step(d, a, b, 16, array)
    basic_step(b, c, d, 12, array)
    basic_step(d, a, b, 8, array)
    basic_step(b, c, d, 7, array)


"""
This function performs a double round, by performing a full round first on 
the columns of the state, and then on the diagonals of the state - the diagonals 
are illustrated clearly in my report.
"""
def double_round(array): 

    # Column round
    quarter_round(0, 4, 8, 12, array)

    # Display intermediate steps as required
    print("After one quarter round: \n", array.reshape((4, 4)), "\n")

    quarter_round(1, 5, 9, 13, array)
    quarter_round(2, 6, 10, 14, array)
    quarter_round(3, 7, 11, 15, array)

    # Display intermediate step
    print("After one round, before diagonal round: \n", array.reshape((4, 4)), "\n")

    # Diagonal round
    quarter_round(0, 5, 10, 15, array)
    quarter_round(1, 6, 11, 12, array)
    quarter_round(2, 7, 8, 13, array)
    quarter_round(3, 4, 9, 14, array)


"""
This function displays the intial state, performs one double round, 
and then displays the final state. 
"""
def encrypt(array):
    print("Initial state: \n", array.reshape((4, 4)), "\n")
    double_round(array)
    print("After a double round: \n", array.reshape((4, 4)), "\n")

encrypt(initial_state)

