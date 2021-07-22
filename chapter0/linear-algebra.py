#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def math_process():

    tensor = np.array([
        [[1,2,3],[4,5,6],[6,7,8]],
        [[11,12,13],[14,15,16],[17,18,19]],
        [[21,22,23],[24,25,26],[27,28,29]]
        ])

    tensor_2 = np.array([
        [[0,0,0],[0,0,0],[0,0,0]],
        [[128,128,128],[128,128,128],[128,128,128]],
        [[255,255,255],[255,255,255],[255,255,255]]
        ])


    print(np.array([
        [0,0,0],[1,1,2],[3,3,3]
        ]))
    print(tensor)
    plt.imshow(tensor, interpolation = "nearest")
    plt.imshow(tensor_2, interpolation = "nearest")
    plt.show()


def shape_forming():
    escalar = 5.679
    vector = np.array([1,2,3])
    matrix = np.array([[1,2,3],[3,4,5],[6,7,8]])
    """tensor = np.array([
        [[1,2,3],[4,5,6],[6,7,8]],
        [[11,12,13],[14,15,16],[17,18,19]],
        [[21,22,23],[24,25,26],[27,28,29]]
    ])"""

    tensor = np.array([
        [[1,2,3],[4,5,6],[6,7,8]],
        [[14,15,16],[17,18,19],[0,0,0]],
        [[21,22,23],[24,25,26],[27,28,29]]
    ])

    
    try:
        print(escalar.shape)
    except Exception as e:
        print(str(e))
    
    print(tensor)
    print("vector shape: ",vector.shape)
    print("matrix shape: ", matrix.shape)
    print("tensor shape: ", tensor.shape)


def math_matrix():
    # transposition and matrix sum
    escalar = 5.679
    vector = np.array([1,2,3])
    matrix = np.array([[1,2,3],[3,4,5],[6,7,8]])
    tensor = np.array([
        [[1,2,3],[4,5,6],[6,7,8]],
        [[11,12,13],[14,15,16],[17,18,19]],
        [[21,22,23],[24,25,26],[27,28,29]]
    ])

    """tensor = np.array([
        [[1,2,3],[4,5,6],[6,7,8]],
        [[14,15,16],[17,18,19],[0,0,0]],
        [[21,22,23],[24,25,26],[27,28,29]]
    ])"""

    
    try:
        print(escalar.shape)
    except Exception as e:
        print(str(e))
    
    print(tensor)
    print(tensor.T)
    print(matrix)
    print(matrix.T)

def main():
    # math_process()
    # shape_forming()
    math_matrix()

if __name__ == "__main__":
    main()



