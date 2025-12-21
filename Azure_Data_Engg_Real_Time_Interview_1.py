# Databricks notebook source
# MAGIC %md
# MAGIC ##### It contain question frorm 1 to 50

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question1 - Simple python program to check if string or number is palindrome or not by using predefine function like reverse, sorted and slicing method and without using predefine function

# COMMAND ----------

str = "gauravvaruag"
rev_str = str[::-1]

if str == rev_str:
    result = True
else:
    result = False


# COMMAND ----------

str1 = 'malayalam'

# Declare an empty string variable
revstr = ""

# Iterate string with for loop
for i in str1:
    revstr = i + revstr  # Append each character to the start of revstr

if str1 == revstr:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# COMMAND ----------

def is_palindrome(str1):
    w = ''  # Initialize w inside the function
    for char in str1:
        w = char + w
    return str1 == w

input_string = 'malayalam'
print(is_palindrome(input_string))  # Returns: True


# COMMAND ----------

str1 = 'malayalam'
result = ''.join(reversed(str1))
if str1 == result:
    print('palindrome')
else:
    print('no')

# COMMAND ----------

def is_palindrome(s):
    s = s.lower()
    return s == ''.join(reversed(s))

input_string = 'malayalam'
print(is_palindrome(input_string))  # Returns: True


# COMMAND ----------

def is_palindrome_using_reverse(s):
    reversed_str = ''.join(reversed(s))
    return s == reversed_str

def is_palindrome_using_sorted(s):
    sorted_str = ''.join(sorted(s))
    return s == sorted_str

def is_palindrome_using_slicing(s):
    return s == s[::-1]

def is_palindrome_without_predefined_functions(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

# Test the functions
input_str = input("Enter a string or number: ")

# Using reverse
print(f"Using reverse: {is_palindrome_using_reverse(input_str)}")

# Using sorted
print(f"Using sorted: {is_palindrome_using_sorted(input_str)}")

# Using slicing
print(f"Using slicing: {is_palindrome_using_slicing(input_str)}")

# Without using predefined functions
print(f"Without using predefined functions: {is_palindrome_without_predefined_functions(input_str)}")


# COMMAND ----------

def is_palindrome(input_str):
# Convert input to string
    input_str = str(input_str)
# Reverse the input string
    reversed_str = input_str[::-1]
# Compare the input string with the reversed string
    if input_str == reversed_str:
        return True
    else:
        return False
# Test the function
input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 2- We have L1 = [0,1,0,1,1,0] write program to make all 0 in left side and all 1 in right side

# COMMAND ----------

L= [0,1,0,1,1,0]
str = []
str1 = []
for i in L:
    if i ==0:
        str.append(i)
    else:
        str1.append(i)

modified_list = str + str1
print("Original List:", L)
print("Modified List:", modified_list)

# print(str.extend(str1)) 

# COMMAND ----------

L1 = [0, 1, 0, 1, 1, 0]

# Sort the list, with 0s coming first
L1.sort()

print("Modified List:", L1)


# COMMAND ----------

L1 = [0, 1, 0, 1, 1, 0]

# Create a new sorted list
sorted_list = sorted(L1)

print("Original List:", L1)
print("Modified List:", sorted_list)


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question3 - We have column as 'Name' and 'ID' in sql table, write a code in SQL to find the names whose name is having more than 5 characters

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create a sample table
# MAGIC CREATE TABLE YourTable (
# MAGIC     ID INT,
# MAGIC     Name VARCHAR(255)
# MAGIC );
# MAGIC
# MAGIC -- Insert some sample data
# MAGIC INSERT INTO YourTable (ID, Name) VALUES
# MAGIC (1, 'John'),
# MAGIC (2, 'Alice'),
# MAGIC (3, 'Bob'),
# MAGIC (4, 'Charlie'),
# MAGIC (5, 'David'),
# MAGIC (6, 'Eleanor'),
# MAGIC (7, 'Frank');
# MAGIC
# MAGIC -- Retrieve names with more than 5 characters
# MAGIC SELECT ID, Name
# MAGIC FROM YourTable
# MAGIC WHERE LENGTH(Name) > 5;  
# MAGIC
# MAGIC -- OR WHERE LEN(Name) > 5;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 4-  Difference among delete, truncate and drop

# COMMAND ----------

+------------+--------------------------+---------------------------------+----------------------------+
|            |          DELETE          |            TRUNCATE            |            DROP            |
+------------+--------------------------+---------------------------------+----------------------------+
| Purpose    | Remove specific rows     | Remove all rows                 | Remove entire table         |
|            | based on a condition.    | from a table.                   | and its structure.          |
+------------+--------------------------+---------------------------------+----------------------------+
| Behavior   | Deletes individual rows. | Removes all rows, but retains   | Deletes the entire table,    |
|            |                          | the table structure (columns,  | including columns,          |
|            |                          | constraints, indexes).          | constraints, indexes.       |
+------------+--------------------------+---------------------------------+----------------------------+
| Undo       | Can be rolled back        | Can't be rolled back.            | Can't be rolled back.        |
|            | (if within a transaction) |                               |                              |
+------------+--------------------------+---------------------------------+----------------------------+
| Performance| Generally slower than     | Faster than DELETE as it's a    | Faster than DELETE, but may  |
|            | TRUNCATE for large tables.| bulk operation.                 | require more resources than  |
|            |                          |                                 | TRUNCATE for large tables.   |
+------------+--------------------------+---------------------------------+----------------------------+
| Usage      | When you need to remove   | When you want to remove all      | When you want to remove the  |
|            | specific rows based on   | rows from a table without       | entire table and its         |
|            | a condition.              | affecting table structure.      | structure.                   |
+------------+--------------------------+---------------------------------+----------------------------+


# COMMAND ----------

DELETE FROM YourTable WHERE Condition; - We can use "Where" condition in delete statement
TRUNCATE TABLE YourTable;
DROP TABLE YourTable;

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question5-  What are Window function in SQL
# MAGIC Window functions in SQL are a category of functions that perform a calculation across a set of rows related to the current row within a query result set. These functions are applied to a "window" or a "partition" of rows defined by an OVER clause. Window functions are commonly used for analytical tasks and reporting. Here are some commonly used window functions:
# MAGIC
# MAGIC  1- ROW_NUMBER():
# MAGIC Assigns a unique number to each row within a partition of the result set.
# MAGIC SELECT
# MAGIC     ROW_NUMBER() OVER (ORDER BY column_name) AS row_num,
# MAGIC     column1, column2
# MAGIC FROM
# MAGIC     your_table;
# MAGIC
# MAGIC 2- RANK():Assigns a unique rank to each distinct row within a partition, with ties receiving the same rank.
# MAGIC SELECT
# MAGIC     RANK() OVER (ORDER BY column_name) AS rank,
# MAGIC     column1, column2
# MAGIC FROM
# MAGIC     your_table;
# MAGIC
# MAGIC 3- DENSE_RANK():Similar to RANK(), but without gaps between rank values for tied rows.
# MAGIC SELECT
# MAGIC     DENSE_RANK() OVER (ORDER BY column_name) AS dense_rank,
# MAGIC     column1, column2
# MAGIC FROM
# MAGIC     your_table;
# MAGIC
# MAGIC 4- SUM():Calculates the cumulative sum of a specified column within a window.
# MAGIC SELECT
# MAGIC     column1,
# MAGIC     column2,
# MAGIC     SUM(column3) OVER (ORDER BY column1) AS cumulative_sum
# MAGIC FROM
# MAGIC     your_table;
# MAGIC
# MAGIC 5- AVG():Calculates the average of a specified column within a window.
# MAGIC SELECT
# MAGIC     column1,
# MAGIC     column2,
# MAGIC     AVG(column3) OVER (PARTITION BY column1) AS average_per_group
# MAGIC FROM
# MAGIC     your_table;
# MAGIC   
# MAGIC 6-LEAD() and LAG():Access data from subsequent or previous rows within the result set.
# MAGIC SELECT
# MAGIC     column1,
# MAGIC     LEAD(column2) OVER (ORDER BY column1) AS next_value,
# MAGIC     LAG(column2) OVER (ORDER BY column1) AS previous_value
# MAGIC FROM
# MAGIC     your_table;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 6 - Write a code in SQL to print your name?

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Gaurav"

# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 7-  Write a program to print cube in python without using lambda function

# COMMAND ----------

def cube(a):
    c = a * a * a
    return c

result = cube(3)
print(result)


# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 8-  Write a program to print cube in python using lambda function

# COMMAND ----------

c = lambda a: a*a*a
print(c(3))  # or c(3)

# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 9-  Write a sample tuple, ('apple','orange') and add 'kiwi' into the tuple
# MAGIC **Note** - tuple is immutable so we cannot add value directly, first convert tuple into list and add the value then convert it back into tuple

# COMMAND ----------

a = ('apple', 'orange')
convert_to_lst = list(a)
convert_to_lst[1] = 'kiwi'
convert_back_to_tuple = tuple(convert_to_lst)
print(convert_back_to_tuple)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### use insert(index, element) to insert at specific index position

# COMMAND ----------

a = ('apple', 'orange')
convert_to_lst = list(a)

# Insert 'kiwi' at index 2
convert_to_lst.insert(2, 'kiwi')

convert_back_to_tuple = tuple(convert_to_lst)
print(convert_back_to_tuple)


# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 10-  Write a program to add number-10 into tuple using append() method?

# COMMAND ----------

tuple_a = (1,2,3,4)
convert_list = list(tuple_a)
convert_list.append(10)

convert_back_to_tuple = tuple(convert_list)
print(convert_back_to_tuple)

# COMMAND ----------

dict = {'brand':'tata', 'model':'nexon', 'color': 'white'}
dict.pop('model')
dict['color'] = 'red'
dict.update({'color':'red'})
dict['model'] = 'safari'
print(dict)

# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 11-  Write a program in python to print 1 to 5

# COMMAND ----------

i = 1
while i <6:
    print(i)
    i +=1

# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 12-  Write python program to print from 1 to 10 without using while loop?

# COMMAND ----------

number = range(10)
for i in number:
    print(i)

# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 13-  Write a program to print your name in python

# COMMAND ----------

def myfunction(fname):
    print('my name is:' + fname)
myfunction('gaurav')

# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 14-  Write a program in python using lambda to add 10 into the number randomly

# COMMAND ----------

x = lambda a: a+10
print(x(5))

# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 15-  Write a program in python using lambda to multiply two numbers

# COMMAND ----------

x = lambda a, b: a*b
print(x(5,6))


# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 16-  Write a program to squaring each element in the list?

# COMMAND ----------

listnum = [1,2,3,4]
newlist = []
for num in listnum:
    newlist.append(num*num)
print(newlist)

# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 17-  Write a python program to print square of number using function?

# COMMAND ----------

n = 5
def sq(n):
    return n*n

print(sq(n))

# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 18-  Write a python program to print square of number without using function?

# COMMAND ----------

n = 15
square = n * n
print(f"The square of {n} is {square}")


# COMMAND ----------

# Using Exponent Operator (**)
n = 15
square = n ** 2
print(f"The square of {n} is {square}")

# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 19-  Write python program to print even number from list?

# COMMAND ----------

my_list = [2, 7, 5, 64, 14]
def print_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print(num)

print_even_numbers(my_list)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Using a list comprehension:

# COMMAND ----------

def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# Example usage
my_list = [2, 7, 5, 64, 14]
even_nums = even_numbers(my_list)
print("Even numbers in the list:", even_nums)


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Using a lambda expression with filter:

# COMMAND ----------

def even_numbers_filter(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

# Example usage
my_list = [2, 7, 5, 64, 14]
even_nums = even_numbers_filter(my_list)
print("Even numbers in the list:", even_nums)


# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 20-  Write python program to print odd number from list?

# COMMAND ----------

def print_odd_numbers(lst):
    for num in lst:
        if num % 2 != 0:
            print(num, end=" ")

# Example usage
my_list = [2, 7, 5, 64, 14]
print_odd_numbers(my_list)


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Using a list comprehension:

# COMMAND ----------

def odd_numbers(lst):
    return [num for num in lst if num % 2 == 1]

# Example usage
my_list = [2, 7, 5, 64, 14]
odd_nums = odd_numbers(my_list)
print("Odd numbers in the list:", odd_nums)


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Using a lambda expression with filter:

# COMMAND ----------

def odd_numbers_filter(lst):
    return list(filter(lambda x: x % 2 != 0, lst))

# Example usage
my_list = [2, 7, 5, 64, 14]
odd_nums = odd_numbers_filter(my_list)
print("Odd numbers in the list:", odd_nums)


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 21/24 – How to convert array column into list of columns?
# MAGIC -To convert an array column into a list of columns in PySpark, you can use the **withColumn function along with the getItem() function**. 

# COMMAND ----------

from pyspark.sql.functions import col

# Sample data with an array column
data = [("Alice", [25, 30, 35]),
        ("Bob", [22, 28, 32]),
        ("Charlie", [30, 35, 40])]

columns = ["Name", "Scores"]

# Create a DataFrame
df = spark.createDataFrame(data, columns)

# Show the original DataFrame
print("Original DataFrame:")
df.show()

# Convert the array column into a list of columns
max_scores = 3  # Assuming the array has a fixed length

# Create new columns using withColumn and getItem
for i in range(max_scores):
    df = df.withColumn(f"Score_{i+1}", col("Scores").getItem(i))

# Drop the original array column
df = df.drop("Scores")

# Show the final DataFrame
print("\nDataFrame with List of Columns:")
df.show()


# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode

# Create a Spark session
spark = SparkSession.builder.appName("Example").getOrCreate()

# Sample data
data = [("John", ["Math", "Physics", "Chemistry"]),
        ("Alice", ["History", "English"]),
        ("Bob", ["Biology", "Physics"])]

# Define the schema
columns = ["Name", "Subjects"]
df = spark.createDataFrame(data, columns)
df.show()


# COMMAND ----------

# Explode the array column "Subjects" into separate rows
df_exploded = df.select(col("Name"), explode(col("Subjects")).alias("Subject"))

# Show the result
df_exploded.show(truncate=False)


# COMMAND ----------

import pyspark.sql.functions as F

# create a sample dataframe
data = [("A", [1, 2, 3]), ("B", [4, 5, 6]), ("C", [7, 8, 9])]
df = spark.createDataFrame(data, ["id", "array_col"])

# explode the array column to get a "long" format
df = df.withColumn("exploded", F.explode("array_col"))

# split the exploded column into separate columns
df = df.withColumn("name", F.split("exploded", "\\s+")[0])
df = df.withColumn("value", F.split("exploded", "\\s+")[1])

# pivot the data to get the desired output
df = df.groupBy("id").pivot("name").agg(F.first("value"))

# show the result
df.show()


# COMMAND ----------

import pyspark.sql.functions as F

# create a sample dataframe
data = [("A", 1, None), ("B", None, 2), ("C", 3, 4)]
df = spark.createDataFrame(data, ["id", "col1", "col2"])

# drop columns with null values
df = df.drop(*[col for col in df.columns if df.filter(F.col(col).isNull()).count() > 0])

# show the result
df.show()


# COMMAND ----------

# MAGIC %md
# MAGIC #####Question 22-  Write a python program to drop the columns with null values?

# COMMAND ----------

from pyspark.sql.functions import col

# Sample data with null values
data = [("Alice", 25, None, 150),
        ("Bob", None, 175, 200),
        ("Charlie", 30, 180, None)]

columns = ["Name", "Age", "Height", "Weight"]

# Create a DataFrame
df = spark.createDataFrame(data, columns)

# Show the original DataFrame
print("Original DataFrame:")
df.show()

# Drop columns with null values
df_filtered = df.drop(*[col_name for col_name in df.columns if df.filter(col(col_name).isNull()).count() > 0])

# Show the DataFrame after dropping columns with null values
print("\nDataFrame after dropping columns with null values:")
df_filtered.show()


# COMMAND ----------

# Define data and columns
data = [("Alice", 25, None, 150),
        ("Bob", None, 175, 200),
        ("Charlie", 30, 180, None)]

columns = ["Name", "Age", "Height", "Weight"]

# Create a DataFrame
df = spark.createDataFrame(data, columns)
df.show()
# Drop rows containing None values
df_cleaned = df.na.drop()

# Show the cleaned DataFrame
df_cleaned.show()


# COMMAND ----------

# Import necessary libraries
from pyspark.sql.functions import when

# Define data and columns
data = [("Alice", 25, None, 150),
        ("Bob", None, 175, 200),
        ("Charlie", 30, 180, None)]

columns = ["Name", "Age", "Height", "Weight"]

# Create a DataFrame
df = spark.createDataFrame(data, columns)
df.show()
# Replace None values with 'gaurav'
df_filled = df.fillna('gaurav')  # OR df_filled = df.na.fill('gaurav')

# Show DataFrame with None replaced with 'gaurav'
df_filled.show()


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 29- Suppose we have two column namely Country and Revenue, write a query in sql to keep one column always on top?

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Table creation query
# MAGIC CREATE TABLE RevenueData (
# MAGIC     Country VARCHAR(255),
# MAGIC     Revenue DECIMAL(10, 2)
# MAGIC );
# MAGIC
# MAGIC -- Insert some sample data
# MAGIC INSERT INTO RevenueData (Country, Revenue) VALUES
# MAGIC ('USA', 100000.00),
# MAGIC ('Canada', 75000.50),
# MAGIC ('UK', 120000.75),
# MAGIC ('Australia', 90000.25),
# MAGIC ('Germany', 110000.50);
# MAGIC select * from RevenueData;

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC -- Query to retrieve data with a specific country ('USA' in this example) always on top
# MAGIC SELECT Country, Revenue
# MAGIC FROM RevenueData
# MAGIC ORDER BY
# MAGIC     CASE
# MAGIC         WHEN Country = 'USA' THEN 0
# MAGIC         ELSE 1
# MAGIC     END,
# MAGIC     Country;

# COMMAND ----------

# MAGIC %sql   -- second method
# MAGIC -- Query to retrieve data with a specific country ('USA' in this example) always on top
# MAGIC SELECT Country, Revenue
# MAGIC FROM RevenueData
# MAGIC ORDER BY
# MAGIC     Country = 'USA' DESC,
# MAGIC     Country;

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 31- We have two columns namely 'Name' and 'Age' write a query in SQL to make the age bracket like age between 1 to 18 is 'young age', age between 19 to 30 is middle age and age between 31 to 60 is old age?

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Assuming you have a table named 'Person' with columns 'Name' and 'Age'
# MAGIC CREATE TABLE Person2 (
# MAGIC     Name VARCHAR(255),
# MAGIC     Age INT
# MAGIC );
# MAGIC
# MAGIC -- Insert some sample data
# MAGIC INSERT INTO Person2 (Name, Age) VALUES
# MAGIC ('John', 15),
# MAGIC ('Alice', 25),
# MAGIC ('Bob', 35),
# MAGIC ('Eva', 50),
# MAGIC ('Charlie', 60);
# MAGIC select * from Person2;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Query to create age brackets
# MAGIC SELECT
# MAGIC     Name,
# MAGIC     Age,
# MAGIC     CASE
# MAGIC         WHEN Age BETWEEN 1 AND 18 THEN 'Young Age'
# MAGIC         WHEN Age BETWEEN 19 AND 30 THEN 'Middle Age'
# MAGIC         WHEN Age BETWEEN 31 AND 60 THEN 'Old Age'
# MAGIC         ELSE 'Unknown Age Bracket'
# MAGIC     END AS AgeBracket
# MAGIC FROM Person2;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Assuming you have a table named 'Employee' with columns 'EmpID', 'Name', 'DeptID', and 'Strength'
# MAGIC CREATE TABLE Employee12 (
# MAGIC     EmpID INT,
# MAGIC     Name VARCHAR(255),
# MAGIC     DeptID INT,
# MAGIC     Strength VARCHAR(255)
# MAGIC );
# MAGIC
# MAGIC -- Insert some sample data
# MAGIC INSERT INTO Employee12 (EmpID, Name, DeptID, Strength) VALUES
# MAGIC (1, 'John', 101, 'Leadership'),
# MAGIC (2, 'Alice', 102, 'Hardworking'),
# MAGIC (3, 'Bob', 101, 'Responsible'),
# MAGIC (4, 'Eva', 102, 'Punctuality'),
# MAGIC (5, 'Charlie', 101, 'Self motivated'),
# MAGIC (6, 'David', 102, 'Quick learner'),
# MAGIC (7, 'Frank', 101, 'Listening');
# MAGIC select * from Employee12
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Query to concatenate 'Strength' values into a single column using GROUP_CONCAT (for MySQL)
# MAGIC SELECT
# MAGIC     EmpID,
# MAGIC     Name,
# MAGIC     DeptID,
# MAGIC     concat_ws(Strength) AS "Strength"
# MAGIC FROM Employee12
# MAGIC GROUP BY EmpID, Name, DeptID;

# COMMAND ----------

FROM pyspark.sql.functions IMPORT concat_ws, collect_list
spark.sql("""
    SELECT
        EmpID,
        Name,
        DeptID,
        concat_ws(',', collect_list(Strength)) AS Strength
    FROM Employee12
    GROUP BY EmpID, Name, DeptID;
""")


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 37 – Given two strings how would you know if they are anagram to each other?

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Method 1- By using sorted() method

# COMMAND ----------

# solve anagram using sorted method
# Example usage:
string1 = "Listen"
string2 = "Silent"

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.lower()
    str2 = str2.lower()

    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Method 2 - By using ordinal ascii method

# COMMAND ----------

# solve anagram problem using ordinal ascii method
def are_anagrams(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Initialize variables to store the sum of ordinal values
    sum1 = 0
    sum2 = 0

    # Calculate the sum of ordinal values for str1
    for char in str1:
        sum1 += ord(char)

    # Calculate the sum of ordinal values for str2
    for char in str2:
        sum2 += ord(char)

    # Check if the sums are equal
    if sum1 == sum2:
        print(f"{str1} and {str2} are anagrams.")
    else:
        print(f"{str1} and {str2} are not anagrams.")

# Example usage
string1 = "Race"
string2 = "Care"
are_anagrams(string1, string2)


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Method 3- By using sorted() method- complete code

# COMMAND ----------

str1 = "Race"
str2 = "Care"

# convert both the strings into lowercase
str1 = str1.lower()
str2 = str2.lower()

# check if length is same
if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")

else:
    print(str1 + " and " + str2 + " are not anagram.")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Method 4- By using sorted() method- shortcut method

# COMMAND ----------

def check(s1, s2):
     
    # the sorted strings are checked 
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.") 
    else:
        print("The strings aren't anagrams.")         
         
# driver code  
s1 ="listen"
s2 ="silent"
check(s1, s2)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Method 5- By using counter() method

# COMMAND ----------

from collections import Counter
 
# function to check if two strings are
# anagram or not
# driver code
s1 = "listen"
s2 = "silent"

def check(s1, s2):
   
    # implementing counter function
    if(Counter(s1) == Counter(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
 


check(s1, s2)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Method 6 - By using Dictionary

# COMMAND ----------

# Example usage
str1 = "listen"
str2 = "silent"

def is_anagram(str1, str2):
    # Create a dictionary to store the frequency of each character in str1
    dict_count = {}
    for char in str1:
        if char in dict_count:
            dict_count[char] += 1
        else:
            dict_count[char] = 1

    # Iterate over str2 and decrement the corresponding count in dict_count
    for char in str2:
        if char in dict_count:
            dict_count[char] -= 1
        else:
            return False

    # If all counts in dict_count are zero, the strings are anagrams
    for count in dict_count.values():
        if count != 0:
            return False
        
    return True

if is_anagram(str1, str2):
    print(str1, "and", str2, "are anagrams")
else:
    print(str1, "and", str2, "are not anagrams")


# COMMAND ----------

# solve anagram problem using ascii by gpt
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sum of ASCII values is the same for both strings
    return sum(ord(char) for char in str1) == sum(ord(char) for char in str2)

# Example usage:
string1 = "Listen"
string2 = "Silent"

if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 38- Two sum problem?

# COMMAND ----------

from typing import List

lst = [2,4,7,8]
target = 11

def twosum(lst, target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return [i, j]
            
print(twosum(lst,target))

# COMMAND ----------

from typing import List
def twosum(nums, target):
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Example usage:
numbers = [2, 7, 11, 15]
target_sum = 9
result = twoSum(numbers, target_sum)

if result:
    print(result)
else:
    print(target_sum)


# COMMAND ----------

def twosum(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]

n = [3, 1, 1, 2]
t = 5
print(twosum(n, t))

# The function then uses two nested loops (for i in range(length) and for j in range(i + 1, length)) to iterate over all pairs of indices (i, j) in the list nums. The inner loop (for j) starts from i + 1 to avoid duplicate pairs and to ensure that the order of indices in the result is in ascending order.

# Inside the inner loop, the function checks if the sum of the numbers at indices i and j in the list nums is equal to the target sum (if nums[i] + nums[j] == target).

# COMMAND ----------

def twosum(nums, target):

  # search first element in the array
  for i in range(len(nums) - 1):
      
    # search other element in the array
    for j in range(i + 1, len(nums)):

      # if these two elemets sum to pair_sum, print the pair
      if nums[i] + nums[j] == target:
        #print("Pair with sum", target,"is: (", nums[i],",",nums[j],")")
        print(nums[i],",",nums[j])
# Driver Code
nums = [2, 7, 11, 15]
target = 9

# Function call inside print
twosum(nums, target) 

# COMMAND ----------

from typing import List

def twoSum(nums: List[int], target: List[int]):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Example usage:
numbers = [2, 7, 11, 15]
target_sum = 9
result = twoSum(numbers, target_sum)

if result:
    print(f"The indices of the two numbers that add up to {target_sum} are: {result}")
else:
    print(f"No solution found for the target sum {target_sum}.")


# COMMAND ----------

# By using dictionary
def twosum(nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []
    # Example usage:
numbers = [2, 7, 11, 15]
target_sum = 9
result = twoSum(numbers, target_sum)

if result:
    print(result)
else:
    print(target_sum)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 38- Three sum problem?

# COMMAND ----------

from typing import List

lst = [2,4,6,7,8]
target = 12

def three_sum(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                if lst[i] + lst[j] + lst[k] == target:
                    return [i, j, k]
    return None

print(three_sum(lst, target))


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 27 - Two multiple problem?

# COMMAND ----------

from typing import List

lst = [2,4,7,8]
target = 28

def two_multi(lst, target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] * lst[j] == target:
                return [i, j]
            
print(two_multi(lst,target))

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 27/110- lst = [12,3,27,5,4,9,4] find the 3 numbers which will give 180 as multiplication of that 3 numbers in python?
# MAGIC ##### Three multi problem?

# COMMAND ----------

from typing import List

lst = [2,4,6,7,8]
target = 64

def three_multi(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                if lst[i] * lst[j] * lst[k] == target:
                    return [i, j, k]
    return None

print(three_multi(lst, target))

# COMMAND ----------

# Example usage
lst = [12, 3, 27, 5, 4, 9, 4]
target = 180

def find_three_numbers(lst, target):
    for i in range(len(lst) - 2):                         # for i in range(len(lst)):
        for j in range(i + 1, len(lst) - 1):              # for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):              # for k in range(j + 1, len(lst)):
                if lst[i] * lst[j] * lst[k] == target:
                    return [lst[i], lst[j], lst[k]]
    return None

result = find_three_numbers(lst, target)

if result:
    print(f"The three numbers are: {result}")
else:
    print("No three numbers found that multiply to 180.")


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 39 - Given a string, find the occurance of each character, str = "HelloWorld"

# COMMAND ----------

str = "HelloWorld"
char_count = {}
for i in str:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1
print(char_count)


# COMMAND ----------

# MAGIC %md
# MAGIC ###### ** By using counter **

# COMMAND ----------

from collections import Counter

state = "HelloWorld"
counts = Counter(state)

print("Occurrence of all characters in HelloWorld is", counts)


# COMMAND ----------

# MAGIC %md
# MAGIC **defaultdict** is a class in the Python collections module that provides a default value for the dictionary keys. This can be particularly useful when you want to initialize a dictionary with default values for keys that have not been seen before. It helps avoid the need to explicitly check whether a key exists in the dictionary before performing operations.

# COMMAND ----------

from collections import defaultdict

inp_str = "GeeksforGeeks"

# Frequency dictionary
char_count = defaultdict(int)

for i in inp_str:
    char_count[i] += 1

# Printing result
print("Occurrence of all characters in GeeksforGeeks is:\n", dict(char_count))



# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 39- Write a simple python program to sort the array and merge it, arr1 = [7,5,1,10,9] and arr2 = [3,8,2,6,4]

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Method 1- by using sort() method

# COMMAND ----------

def merge_and_sort(arr1, arr2):
    # Combine both arrays
    arr3 = arr1 + arr2

    # Sort the combined array
    arr3.sort()

    return arr3

# Example usage
arr1 = [7, 5, 1, 10, 9]
arr2 = [3, 8, 2, 6, 4]

merged_sorted_array = merge_and_sort(arr1, arr2)
print("Merged and sorted array:", merged_sorted_array)


# COMMAND ----------

# MAGIC %md
# MAGIC #####Method 2- by using sorted() method

# COMMAND ----------

arr1 = [7, 5, 1, 10, 9]
arr2 = [3, 8, 2, 6, 4]

# Sort the arrays
sorted_arr1 = sorted(arr1)
sorted_arr2 = sorted(arr2)

# Merge the sorted arrays
merged_array = sorted_arr1 + sorted_arr2

print("Merged and sorted array:", merged_array)


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Method 3 by using extend() function

# COMMAND ----------

arr1 = [7, 5, 1, 10, 9]
arr2 = [3, 8, 2, 6, 4]

# Sort arr1 in-place
arr1.sort()

# Extend arr1 with the elements of arr2 and sort it
arr1.extend(arr2)
arr1.sort()

print("Merged and sorted array:", arr1)


# COMMAND ----------

# MAGIC %md
# MAGIC #####Method 3-  without using inbuilt function

# COMMAND ----------

arr1 = [7,5,1,10,9]
arr2 = [3,8,2,6,4]

def merge_sorted_arrays(arr1, arr2):
  merged_array = []
  i = 0
  j = 0
  while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
      merged_array.append(arr1[i])
      i += 1
    else:
      merged_array.append(arr2[j])
      j += 1

  # Add the remaining elements from the longer array
  if i < len(arr1):
    merged_array.extend(arr1[i:])
  elif j < len(arr2):
    merged_array.extend(arr2[j:])

  return merged_array

# Sort the arrays first
arr1.sort()
arr2.sort()

# Merge the sorted arrays
merged_array = merge_sorted_arrays(arr1, arr2)

print(merged_array)


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 40- How to create table partition in few column in SQL and Pyspark?

# COMMAND ----------

# MAGIC %sql
# MAGIC --1.Create the Base Table:
# MAGIC CREATE TABLE sales (
# MAGIC     order_id INT,
# MAGIC     customer_id INT,
# MAGIC     order_date DATE,
# MAGIC     amount DECIMAL(10,2)
# MAGIC );
# MAGIC -- 2.Add Data to the Partitioned Table:
# MAGIC INSERT INTO sales (order_id, customer_id, order_date, amount)
# MAGIC VALUES (1234, 5678, '2023-10-01', 100.00);
# MAGIC
# MAGIC -- 3.Partition the Table by Order Date:
# MAGIC ALTER TABLE sales
# MAGIC PARTITION BY (order_date);
# MAGIC

# COMMAND ----------

from pyspark.sql.functions import col
# 1. create dataframe
data = [{"order_id": 1234, "customer_id": 5678, "order_date": "2023-10-01", "amount": 100.00}]
df = spark.createDataFrame(data)

# 2.Partition the DataFrame:
df = df.repartition(4)
df = df.write.partitionBy(col("order_date")).format("parquet").save("partitioned_sales")


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 41 – Find the sum of all positive and negative numbers of given table?

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE your_table (
# MAGIC   ID INT
# MAGIC );
# MAGIC
# MAGIC INSERT INTO your_table (ID) VALUES
# MAGIC   (5),
# MAGIC   (-3),
# MAGIC   (8),
# MAGIC   (-2),
# MAGIC   (10),
# MAGIC   (-7),
# MAGIC   (4);
# MAGIC select * from your_table;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   SUM(CASE WHEN ID > 0 THEN ID ELSE 0 END) AS sum_positive,
# MAGIC   SUM(CASE WHEN ID < 0 THEN ID ELSE 0 END) AS sum_negative
# MAGIC FROM your_table;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE numbers (
# MAGIC     id INT,
# MAGIC     value INT
# MAGIC );
# MAGIC
# MAGIC INSERT INTO numbers (id, value) VALUES
# MAGIC (1, 5),
# MAGIC (2, -3),
# MAGIC (3, 8),
# MAGIC (4, -2),
# MAGIC (5, 10);
# MAGIC
# MAGIC -- Sum of positive numbers
# MAGIC SELECT
# MAGIC     SUM(CASE WHEN value > 0 THEN value ELSE 0 END) AS sum_positive
# MAGIC FROM numbers;
# MAGIC
# MAGIC -- Sum of negative numbers
# MAGIC SELECT
# MAGIC     SUM(CASE WHEN value < 0 THEN value ELSE 0 END) AS sum_negative
# MAGIC FROM numbers;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from numbers

# COMMAND ----------

# MAGIC %sql
# MAGIC select sum(id) as ID from numbers where id>0
# MAGIC union all
# MAGIC select sum(id) as ID from numbers where id<0

# COMMAND ----------

# MAGIC %sql
# MAGIC select sum(value) as Value from numbers where id>0
# MAGIC union all
# MAGIC select sum(value) as value from numbers where id<0

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 42  We have two table namely table1 and table2, the id column in table1 is 10,20,30,40,50 and id column in table2 contain 10,30,50, write a query in SQL to find out the record which are not common in both?

# COMMAND ----------

# MAGIC %sql -- by using left join
# MAGIC CREATE TABLE table1 (
# MAGIC     id INT
# MAGIC     -- Other columns...
# MAGIC );
# MAGIC
# MAGIC CREATE TABLE table2 (
# MAGIC     id INT
# MAGIC     -- Other columns...
# MAGIC );
# MAGIC
# MAGIC INSERT INTO table1 (id) VALUES (10), (20), (30), (40), (50);
# MAGIC INSERT INTO table2 (id) VALUES (10), (30), (50);
# MAGIC
# MAGIC -- Find records that are not common in both tables
# MAGIC SELECT t1.id
# MAGIC FROM table1 t1
# MAGIC LEFT JOIN 
# MAGIC table2 t2 ON t1.id = t2.id
# MAGIC WHERE t2.id IS NULL
# MAGIC
# MAGIC UNION
# MAGIC
# MAGIC SELECT t2.id
# MAGIC FROM table1 t1
# MAGIC RIGHT JOIN table2 t2 ON t1.id = t2.id
# MAGIC WHERE t1.id IS NULL;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### -- by using except method

# COMMAND ----------

# MAGIC %sql  
# MAGIC SELECT *
# MAGIC FROM table1
# MAGIC EXCEPT
# MAGIC SELECT *
# MAGIC FROM table2;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### by using not in operator

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT id
# MAGIC FROM table1
# MAGIC WHERE id NOT IN (SELECT id FROM table2)
# MAGIC UNION ALL
# MAGIC SELECT id
# MAGIC FROM table2
# MAGIC WHERE id NOT IN (SELECT id FROM table1);
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### by using full outer join

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COALESCE(t1.id, t2.id) AS id
# MAGIC FROM table1 t1
# MAGIC FULL OUTER JOIN table2 t2 ON t1.id = t2.id
# MAGIC WHERE t1.id IS NULL OR t2.id IS NULL;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 47 - Write simple python program to check the parentheses check?

# COMMAND ----------

def isValid(s):
    # Create an empty stack
    stack = []
    # Define the mapping of parentheses
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            stack.append(char)
        elif len(stack) == 0 or stack.pop() != mapping[char]:
            return False

    return not stack

# Example usage:
input_string = "(({}))"
result = isValid(input_string)

if result:
    print("Parentheses are balanced.")
else:
    print("Parentheses are not balanced.")


# COMMAND ----------

s = "(({}))"
def isValid(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')

    return len(s) == 0

result = isValid(s)

if result:
    print("Parentheses are balanced.")
else:
    print("Parentheses are not balanced.")


# COMMAND ----------

def isValid(s):
        while '()' in s or '[]'in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')
            if len(s) !=0:
                return False
            else:
                return True

# Example usage:
input_string = "(({}))"
result = isValid(input_string)

if result:
    print("Parentheses are balanced.")
else:
    print("Parentheses are not balanced.")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Question 50 - We have sorted array arr = [3,6,8,12,15] write a simple program in python to add 7 in correct location?

# COMMAND ----------

def insert_into_sorted_array(arr, new_element):
    for i in range(len(arr)):
        if arr[i] > new_element:
            arr.insert(i, new_element)
            break
    else:
        arr.append(new_element)

# Example usage:
sorted_array = [3, 6, 8, 12, 15]
new_element = 7

insert_into_sorted_array(sorted_array, new_element)

print("Updated Sorted Array:", sorted_array)


# COMMAND ----------

# MAGIC %md
# MAGIC #####  Approach #2 : Another way to insert an element into a sorted list is to use the built-in sorted() function.

# COMMAND ----------

lst = [1, 2, 4]
n = 3

def insert(lst, n):
  # Insert the element into the list
  lst.append(n)
  # Sort the list
  sorted_list = sorted(lst)
  return sorted_list
 
print(insert(lst, n))
#This code is contributed by Edula Vinay Kumar Reddy

# COMMAND ----------

# MAGIC %md
# MAGIC #####  Approach #3 : Python comes with a bisect module whose purpose is to find a position in list where an element needs to be inserted to keep the list sorted. 

# COMMAND ----------

# Python3 program to insert 
# an element into sorted list
import bisect 
 
def insert(list, n):
    bisect.insort(list, n) 
    return list
 
# Driver function
list = [1, 2, 4]
n = 3
 
print(insert(list, n))