"""*
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""


def print_pattern(n):
    for i in range(n):  # Loop from 0 to n-1 (total n rows)
        print(" " * (n - i - 1) + "* " * (i + 1))  # Print spaces and stars


print_pattern(5)  # Call the function with n = 5
