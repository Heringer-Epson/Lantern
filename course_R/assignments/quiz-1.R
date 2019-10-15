#Quizz #1
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Please find trace of inverse of the following matrix rounded to integer number
#9    4    7
#2    5    8
#3    6    9

#To solve this problem you will need to find out:

#- how to define a matrix in R
#- how to find inverse matrix in R
#- what is matrix trace
#- how to extract diagonal elements from a matrix
#- how to sum up all elements of a vector.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Define a function to compute the trace of a matrix.
get_trace = function(M) {
    sum(diag(M))
}

#3x2 matrix
M = matrix (
  c(9,4,7,2,5,8,3,6,9),
  nrow=3,
  ncol=3,
  byrow=TRUE)

M_inv = solve(M)

#Verify that M x M_inv gives an identity matrix.
#print(M %*% M_inv)

#Compute the trace of the inverse matrix.
M_inv_tr = get_trace(M_inv)
print(round(M_inv_tr))
