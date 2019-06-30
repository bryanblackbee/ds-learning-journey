 McKinney (2017). Python for Data Analysis, 2nd Edition
=========
**Notes**

# Chapter 4 - NumPy Basics: Arrays and Vectorized Computation

## 4.1 The NumPy ndarray: A Multidimensional Array Object
### Declaring arrays

1. Creating arrays with `list`s
2. Creating arrays with all zeros using `np.zeros()`
3. Creating arrays with all ones using `np.ones()`
4. Creating arrays with ranges using `np.arange()`

### Manipulating arrays

1. Changing datatypes of arrays
2. Addition & Subtraction
3. Multiplication & Division with a scalar
4. Boolean comparision

### Basic Indexing and Slicing

1. Slicing a 1D array like a list
2. Slicing a 2D array
3. Slicing using Boolean arrays
4. Slicing using conditions (1 condition & multiple conditions)

### Reshaping, Transposing Arrays, Swapping Axes

1. Use `.reshape()` to change the dimensions of an array
2. Using `.transpose()` and `.T` to swap axes

## 4.2 Universal Functions: Fast Element-Wise Array Functions

 * Mathematical functions like  `square`, `sqrt`, `exp`, `abs`
 * Simple transformations like `sign`, `ceil`, `floor`
 * Using `maximum`, `minimum`, `floor_divide`
 * Using `modf`
 
## 4.3 Array-Oriented Programming with Arrays
### Expressing Conditional Logic as Array Operations
### Mathematical and Statistical Methods
 * `np.sum()` function for arrays
 * `np.mean()` function for arrays
 * `np.cumsum()` function for arrays
 
### Methods for Boolean Arrays
 * Using `np.sum()` on arrays containg Booleans
 
### Sorting
 * Sort an array inplace using `np.sort(arr)`
 
### Unique and Test of Membership
 * Use `np.unique()` to find unique values in an array.
 * Use `np.in1d()` to find if a value exists in another array.
 
## 4.5 Linear Algebra
 * Use `np.dot(arr1, arr2)` to get matrix products
 * Use `inv` to get the inverse of a matrix
 * Use `diag()` to get the diagonal of a square matrix, `det()` to find the determinant of the square matrix and `trace()` to get the trace of a square matrix

## 4.6 Pseudorandom Number Generation
 * Using `normal` to draw from a standard normal distribution
 * Using `binomial` to draw from a binomial distribution
 * Using `rand` to draw from a uniform (-1,1) distribution
 * Using `randint` to draw from a series of numbers in a range, with equal chance of getting any
 * Using `uniform` to draw from a uniform \[0,1) distribution
 * Simulating a random walk
 
# Chapter 5 - Getting Started with `pandas`

## 5.1 Introduction to `pandas` Data Structures
### Series
### DataFrame
### Index Objects

## 5.2 Essential Functionality
 * Re-indexing
 * Dropping entries from an Axis
 * Indexing, selection and filtering
 * Arithmetic and Data Alignment
 * Function Application and Mapping
 * Sorting and Ranking