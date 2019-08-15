McKinney (2017). Python for Data Analysis, 2nd Edition
=========

## Chapter 4 - NumPy Basics: Arrays and Vectorized Computation

### 4.1 The NumPy ndarray: A Multidimensional Array Object
#### Declaring arrays

1. Creating arrays with `list`s
2. Creating arrays with all zeros using `np.zeros()`
3. Creating arrays with all ones using `np.ones()`
4. Creating arrays with ranges using `np.arange()`

#### Manipulating arrays

1. Changing datatypes of arrays
2. Addition & Subtraction
3. Multiplication & Division with a scalar
4. Boolean comparision

#### Basic Indexing and Slicing

1. Slicing a 1D array like a list
2. Slicing a 2D array
3. Slicing using Boolean arrays
4. Slicing using conditions (1 condition & multiple conditions)

#### Reshaping, Transposing Arrays, Swapping Axes

1. Use `.reshape()` to change the dimensions of an array
2. Using `.transpose()` and `.T` to swap axes

### 4.2 Universal Functions: Fast Element-Wise Array Functions

 * Mathematical functions like  `square`, `sqrt`, `exp`, `abs`
 * Simple transformations like `sign`, `ceil`, `floor`
 * Using `maximum`, `minimum`, `floor_divide`
 * Using `modf`
 
### 4.3 Array-Oriented Programming with Arrays
#### Expressing Conditional Logic as Array Operations
#### Mathematical and Statistical Methods
 * `np.sum()` function for arrays
 * `np.mean()` function for arrays
 * `np.cumsum()` function for arrays
 
#### Methods for Boolean Arrays
 * Using `np.sum()` on arrays containg Booleans
 
#### Sorting
 * Sort an array inplace using `np.sort(arr)`
 
#### Unique and Test of Membership
 * Use `np.unique()` to find unique values in an array.
 * Use `np.in1d()` to find if a value exists in another array.
 
### 4.5 Linear Algebra
 * Use `np.dot(arr1, arr2)` to get matrix products
 * Use `inv` to get the inverse of a matrix
 * Use `diag()` to get the diagonal of a square matrix, `det()` to find the determinant of the square matrix and `trace()` to get the trace of a square matrix
 * Determination of an eigenvector and some calculations

### 4.6 Pseudorandom Number Generation
 * Using `normal` to draw from a standard normal distribution
 * Using `binomial` to draw from a binomial distribution
 * Using `rand` to draw from a uniform (-1,1) distribution
 * Using `randint` to draw from a series of numbers in a range, with equal chance of getting any
 * Using `uniform` to draw from a uniform \[0,1) distribution
 * Simulating a random walk
 
## Chapter 5 - Getting Started with `pandas`

### 5.1 Introduction to `pandas` Data Structures
#### Series
#### DataFrame
#### Index Objects

### 5.2 Essential Functionality
 * Re-indexing
 * Dropping entries from an Axis
 * Indexing, selection and filtering
 * Arithmetic and Data Alignment
 * Function Application and Mapping
 * Sorting and Ranking
 
### 5.3 Summarizing and Computing Descriptive Statistics 

#### Common Functions
 * `df.sum()`
 * `df.idxmax()`
 * `df.idxmin()`
 * `df.cumsum()`
 * `df.describe()`
 
#### Correlation and Covariance
 * `Series.corr(Series)`
 * `Series.cov(Series)`
 
#### Unique Values, Value Counts, and Membership
 * `Series.unique()`
 * `Series.value_counts()`
 * `Series.isin()`
 
## Chapter 6 - Data Loading, Storage, and File Formats

### 6.1 Reading and Writing Data in Text Format
 * Reading text files
 * Writing data to text format
 * Working with Delimited Formats
 * JSON Data

### 6.2 Binary Data Formats
 * Reading Microsoft Excel Files

### 6.3 Interacting with Web APIs
 * Using `requests` to call an API
 * Writing JSON results to a JSON file

## Chapter 7 - Data Cleaning and Preparation

### 7.1 Handling Missing Data
 * Identifying missing data using `.isnull()` and `.notnull()`
 * Using `.dropna()` to remove rows with missing values
 * Using `.fillna()` to impute rows or cells with missing values 

### 7.2 Data Transformation
 * identifying & removing duplicates
 * using `.map()` to map values from a domain to another
 * using `.apply()` to pass a `Series` or `DataFrame` to a function
 * replacing values
 * renaming axis indices
 * Discretisation and Binning
 * Detecting and Filtering Outliers
 * Permutation and Random Sampling
 * Computing Indicator / Dummy Variables

### 7.3 String Transformation

**String functions** NOTE: Demo is in Lazada Project

 * `str.count()`, `str.startswith()`, `str.endswith()`
 * `str.join(list)`
 * `str.find()`
 * `str.replace()`, `str.strip()`
 * `str.split(delimiter)`
 * `str.lower()`, `str.upper()`
 
**`re` functions** NOTE: Demo is in Lazada Project

 * `re.compile(pattern)`
 * `re.split(pattern, str)` / `regex.split(str)`
 * `re.findall(pattern, str)` / `regex.find(str)`
 * `re.match(pattern, str)` and `re.search(pattern, str)`
 * `re.sub(pattern, substitution, string)`
 * `m.group(0)` to find substring
 
**String functions in `pandas`**

 * `Series.str.contains(s)`
 * `Series.str.findall(p)`
 * `Series.str.match(p)`
 * `Series.str.split(p)`
 * `Series.str.replace(p, y)`
 
## Chapter 8 - Data Wrangling: Join, Combine, and Reshape

### 8.1 Hierarchical Index

 * Identifying and extracting the index of a `df`.
 * Filtering for values using the outer and inner index of a `Series`
 * Using `.unstack()` and `.stack()` to work between `Series` and `DataFrame` objects
 * Extracting and modifying indices for rows and columns using `df.index.names` and `df.columns.names` respectively
 * Using `df.swaplevel()` to interchange index columns
 * Using `df.sort_index(level)` sort a `df` using index columns
 * Using `df.set_index()` to make a column the index and `df.reset_index()` for its reverse operation
 
### 8.2 Combining and Merging Datasets

 * Merging dataframes using `df1.merge(df2)` or `pd.merge(df1, df2)` with parameters
 * Using different flavours of `how` when merging, including `left`, `right`, `inner` and `outer` 
 * using parameters when merging to determine columns (and indices) to merge on, incluing `on`, `left_on`, `right_on`, `left_index=True` and `right_index=True`
 * modifying columns when column names overlap using `lsuffix` and `rsuffix`
 * Merging on indices using `df1.join(df2)`
 * Stacking `df`s below each other using `pd.concat([df1, df2])` (or horizontally using `axis=1` parameter)
 * Overlaying 2 `df`s together to fill in missing values using `df1.combine_first(df2)`
 
### 8.3 Reshaping and Pivoting

 * Looking at `.stack()` and `.unstack()` to transform datasets
 * Using `df.pivot()` to transform data in "long format" to a dataset with set columns
 * Using `df.melt()` to data with named columns to "long format"
 
## Chapter 10 - Data Aggregation and Group Operations

### 10.1 `GroupBy` Mechanics

 * Understand a `GroupBy` object divides a dataset into keys and their associated chunks, based on the column / `np.array` used
 * Performing `GroupBy` on one and multiple keys
 * Attach a function on a `GroupBy` object to obtain descriptive statistics of different slices of a dataset
 * Iterating through a `GroupBy` object for single-key slicing and multi-key slicing
 
### 10.2 Data Aggregation

 * Use optimised `groupby` functions to aggregate data, including `count()`, `sum()`, `mean()`, `std()`, `var()`, `min()`, `max()`
 * Use `Series` functions to aggregate data e.g. `quantile()`, `describe()` and use custom functions to aggregate data
 * Perform multiple aggregation functions simultaneously on one column, or a group of 2 or more columns
 * Perform different aggregation functions simultaneously on a group of columns using a `dict()`

### 10.3 Apply: General split-apply-combine

 * Use `groupby()` with a function that returns a chunk of data to apply to each group within the dataset
 * Use `groupby()` with a function to calculate summary statistics across all groups in a dataset
 
### 10.4 Pivot Tables and Cross-Tabulation

 * Understand and explain the generation and use of pivot tables
 * Create a pivot table using `df.pivot_table()`
 * Use the `margin` parameter to obtain group totals
 * Use `pd.crosstab(df)` to obtain frequncies within a subgroup
