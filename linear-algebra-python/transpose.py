#!/usr/bin/python3.9



import numpy as np


def main():
    A = np.array([[2, 3], [5, 7], [11, 13]])
    B = np.array([[1, 3], [2, 1]])
    print(A)
    print(B)

    AB_transpose = A.dot(B).T
    BA_transpose = B.T.dot(A.T)

    print(AB_transpose == BA_transpose)

if __name__ == "__main__":
    main()
