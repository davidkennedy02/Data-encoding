from collections import Counter 
import re 

"""
Reading the ciphertext from the file, converting all 
characters to lowercase, and removing all new-line characters - 
finally, storing the cleaned ciphertext in a string, ciphertext.
"""
with open("ciphertext.txt", "r") as file: 
    ciphertext = file.read().lower().replace("\n", "")


"""
Reading an arbitrary collection of English text from a file, 
removing all non-standard english characters, converting the 
text to lowercase, removing all new-line characters, and finally 
storing the cleaned text in a string, traintext.

Note: the arbitrary collection of text was taken from 
https://studres.cs.st-andrews.ac.uk/2021_2022/CS3302/Practicals/P1/train.txt

"""
# Getting general text for analysis
with open("train.txt", "r") as file:
    traintext = file.read()
    traintext = re.sub("[^a-zA-Z ]+", "", traintext)
    traintext = traintext.lower().replace("\n", "")


# Constructing a list of characters in ciphertext in order of frequency
analysedCipher = [x[0] for x in Counter(ciphertext).most_common()]

# Constructing a list of characters in traintext in order of frequency
analysedTrain = [x[0] for x in Counter(traintext).most_common()]

# Used to compare final key with original - no practical use 
originalAnalysedTrain = [x[0] for x in Counter(traintext).most_common()]


# -------------------------------------
"""
This function attempts to 'crack the code' by substituting the symbols
in the ciphertext with the corresponding symbols in the plaintext. 
This is used in conjunction with the function below to gradually 
improve our substitution key, until the plaintext is eventually returned.
"""
def crackTheCode():
    # Display conversion key 
    print(analysedCipher)
    print(analysedTrain)

    # Substitute letters 
    message = ""
    for letter in ciphertext:
        message += analysedTrain[analysedCipher.index(letter)]

    # Display decoded message 
    print(message + "\n")
# -------------------------------------


# -------------------------------------
"""
This simple function swaps two elements in an array, and returns the 
amended array. 
"""
def swapItemsInList(list, i, j):
    # Swap elements
    list[i], list[j] = list[j], list[i]
    return list
# -------------------------------------


"""
I have documented the process I undertook below, including the redundancy 
in natural English language I utilised. 

All in all, I had to amend my key seven times in order to correctly decrypt 
the ciphertext. 
"""

crackTheCode()

# Swap n and r - first word is most likely 'when'
analysedTrain = swapItemsInList(analysedTrain, 6, 8)
crackTheCode()

# Swap c and f - 'one oc the cirst'
analysedTrain = swapItemsInList(analysedTrain, 16, 11)
crackTheCode()

# Swap p and y - 'one of the first yoints'
analysedTrain = swapItemsInList(analysedTrain, 15, 18)
crackTheCode()

# Swap m and v - 'mariety or submariety'
analysedTrain = swapItemsInList(analysedTrain, 14, 21)
crackTheCode()

# Swap d and l - 'inliviluads'
analysedTrain = swapItemsInList(analysedTrain, 10, 12)
crackTheCode()

# Swap m and g - 'when we cogpare the individuals'
analysedTrain = swapItemsInList(analysedTrain, 17, 21)
crackTheCode()

# Swap k and g - 'they kenerally differ'
analysedTrain = swapItemsInList(analysedTrain, 21, 22)
crackTheCode()

# A comparison between the original key used to attempt to decrypt the ciphertext, and the final key 
print("----------------------\nComparing original key to final key: \n", originalAnalysedTrain, "\n", analysedTrain, "\n")