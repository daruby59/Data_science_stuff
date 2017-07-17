#
import copy
from fractions import Fraction
#
def makeIdentity(n):
        result = make2dList(n,n)
        for i in xrange(n):
            result[i][i] = 1
        return result
#
def multiplyMatrices(a, b):
    # confirm dimensions
    aRows = len(a)
    aCols = len(a[0])
    bRows = len(b)
    bCols = len(b[0])
    assert(aCols == bRows) 
    # belongs in a contract 
    rows = aRows
    cols = bCols
    # create the result matrix c = a*b
    c = make2dList(rows, cols)
    # now find each value in turn in the result matrix
    for row in xrange(rows):
        for col in xrange(cols):
            dotProduct = 0
            for i in xrange(aCols):
                dotProduct += a[row][i]*b[i][col]
            c[row][col] = dotProduct
    return c
#
def almostEqualMatrices(m1, m2):
    # verifies each element in the two matrices are almostEqual to each other
    # (and that the two matrices have the same dimensions).
    if (len(m1) != len(m2)): return False
    if (len(m1[0]) != len(m2[0])): return False
    for row in xrange(len(m1)):
        for col in xrange(len(m1[0])):
            if not almostEqual(m1[row][col], m2[row][col]):
                return False
    return True
#
def almostEqual(d1, d2):
    epsilon = 0.00001
    return abs(d1 - d2) < epsilon
#
def invertMatrix(m):
    n = len(m)
    assert(len(m) == len(m[0]))
    inverse = makeIdentity(n) 
    # this will BECOME the inverse eventually
    k = 0.0
    for col in xrange(n):
        # 1. make the diagonal contain a 1
        diagonalRow = col
        assert(m[diagonalRow][col] != 0) 
        # @TODO: actually, we could swap rows
        # here, or if no other row has a 0 in
        # this column, then we have a singular
        # (non-invertible) matrix.  Let's not
        # worry about that for now.  :-)
        # k = Fraction(1,m[diagonalRow][col])
        k = 1/(m[diagonalRow][col])
        m = multiplyRowOfSquareMatrix(m, diagonalRow, k)
        inverse = multiplyRowOfSquareMatrix(inverse, diagonalRow, k)
        # 2. use the 1 on the diagonal to make everything else
        #    in this column a 0
        sourceRow = diagonalRow
        for targetRow in xrange(n):
            if (sourceRow != targetRow):
                k = -m[targetRow][col]
                m = addMultipleOfRowOfSquareMatrix(m, sourceRow, k, targetRow)
                inverse = addMultipleOfRowOfSquareMatrix(inverse, sourceRow,k, targetRow)
    # that's it!
    return inverse
#
def testInvertMatrix():
    print "Testing invertMatrix...",
    print "\n"
    # a = [ [ 1, 2 ], [ 4, 5  ] ]
    # aInverse = invertMatrix(a)
    # identity = makeIdentity(len(a))
    # assert (almostEqualMatrices(identity, multiplyMatrices(a, aInverse)))
    # print "before: "+str(a)
    # a = [ [ 1, 2, 3], [ 2, 5, 7 ], [3, 4, 8 ] ]
    # aInverse = invertMatrix(a)
    # identity = makeIdentity(len(a))
    # assert (almostEqualMatrices(identity, multiplyMatrices(a, aInverse)))
    a = [ [25.0, 1.5, 4.6, 2.0],[6.6, 2.4, 1.5, 8.25],[4.5, 6.25, 3.5, 8.0],[5.0, 2.5, 9.75, 5.25]]
    aInverse = invertMatrix(a)
    identity = makeIdentity(len(a))
    # assert (almostEqualMatrices(identity, multiplyMatrices(a, aInverse)))
    print "Before: "+str(a)
    print "After: "+str(aInverse)
#
def multiplyRowOfSquareMatrix(m, row, k):
    n = len(m)
    rowOperator = makeIdentity(n)
    rowOperator[row][row] = k
    return multiplyMatrices(rowOperator, m)
#
def addMultipleOfRowOfSquareMatrix(m, sourceRow, k, targetRow):
    # add k * sourceRow to targetRow of matrix m
    n = len(m)
    rowOperator = makeIdentity(n)
    rowOperator[targetRow][sourceRow] = k
    return multiplyMatrices(rowOperator, m)
#
def make2dList(rows, cols):
    a=[]
    for row in xrange(rows): a += [[0]*cols]
    return a
#
#
def testdotproduct():
     x1 = [[1,1,1,1,1],[1,1,1,1,1]]
     x2 = [[1,0],[1,0],[1,0],[1,0],[1,0]]
     productx = multiplyMatrices(x1,x2)
     print productx
def main():
    testInvertMatrix()
    # testdotproduct()
#
if __name__ == "__main__":
    main()