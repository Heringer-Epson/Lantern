#Homework 1 –read about and practice matrix operations in R 
#Tutorial: http://www.philender.com/courses/multivariate/notes/matr.html
#https://www.statmethods.net/advstats/matrix.html

#Define matrices.

#3x2 matrix
mat1 = matrix (
  c(1,2,3,4,5,6),
  nrow=3,
  ncol=2,
  byrow=TRUE)

#2x3 matrix
mat2 = matrix (
  c(1,2,1,2,1,2),
  nrow=2,
  ncol=3,
  byrow=FALSE)

#print('Stored matrices:')
#print('mat1 = ')
#print(mat1)
#print('mat2 = ')
#print(mat2)

#Basic operations:
#print(is.matrix(mat1))
#print(dim(mat1))
#print(nrow(mat1))

#Operation: Sum
#print(mat1 + 10)

#Operation: multiplication by scalar.
#print(mat1 * 5)

#Operation: multiplication between matrices.
#print(mat1 %*% mat2)
#print(mat2 %*% mat1)

#Operation: transpose matrix.
#print(t(mat1))
#print(t(mat2))

#Operation: sum of matrices:
#print(mat1 + t(mat2))

#Common vectors:
zeros = matrix(0,3,1)
ones = matrix(1,3,1)
#print(zeros)
#print(ones)

#Matrix inversion:
A = matrix(c(4,4,-2,2,6,2,2,8,4),3,3)
#print(A)
#print(solve(A))
#print(det(A))

matA = qr(A) #?? Function whose an attribute is the rank?
#print(matA$rank)

#Useful operations:
#print(colSums(A)) 
#print(rowSums(A)) 
#print(sum(A))
#print(rowMeans(A)) 
#print(mean(A))

#Concatenation:
B1 = matrix(c(1,1,1,1),2,2)
B2 = matrix(c(2,2,2,2),2,2)
print(B1)
print(B2)

print(cbind(B1,B2))
print(rbind(B1,B2))
