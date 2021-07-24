#!/usr/bin/python


import numpy as np



def making_intern_product():
    escalar = 5.679
    vector = np.array([2,3])
    matrix = np.array([[1,2],[3,4],[5,6]])
    print(matrix * vector)



    # make product intern with the dot function
    print(matrix.dot(vector))


def matrix_product_intern():

    matrix_a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    matrix_b = np.array([[2,3],[5,7],[11,13]])


    try:

        # in this case as the matrix a is applied the matrix b
        # both has the similar dims in A = (4,3) and B = (3,2)
        print(matrix_a.dot(matrix_b))

        # in the other hand as the value B = (3,2) and A = (4,3)
        # The dimensions for the product aren's the same value
        print(matrix_b.dot(matrix_a))
    except Exception as e:
        print(str(e))


def matrix_properties():

    # a_value = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    # b_value = np.array([[2,3],[5,7],[11,13]])
    
    a_value = np.array([[2,3],[5,7],[11,13]])
    b_value = np.array([[1,3],[2,1]])
    c_value = np.array([[3,1],[4,2]])
    abc_value = a_value.dot(b_value.dot(c_value))
    bca_value = a_value.dot(b_value).dot(c_value)
    print(abc_value == bca_value)





def main():
    # making_intern_product()
    # matrix_product_intern()
    matrix_properties()

if __name__ == "__main__":
    main()
