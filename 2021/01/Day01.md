# Summary of Day 1

After reading the instructions, I thought, "this is going to be easy!"

I initially had `[number for number in puzzle.input_data.split('\n')]` as my list of numbers.

What's wrong with this?

String comparison is not the same as integer comparison. Both will yield the same result if all of the numbers contain the same number of digits.

This is a problem for the input data we are given though! Do you see why?  
What happens with string comparison to this segment of the data?

```
994
1017
1018
1015
1025
1007
987
975
973
979
978
1000
999
1000
1003
1009
1010
997
998
997
998
1002
```

Step through each and compare

```
number  as String       as int
994     ----------      ----------
1017    decreasing!     increasing
1018    increasing      increasing
1015    decreasing      decreasing
1025    increasing      increasing
1007    decreasing      decreasing
987     increasing!     decreasing
975     decreasing      decreasing
973     decreasing      decreasing
979     increasing      increasing
978     decreasing      decreasing
1000    decreasing!     increasing
999     increasing!     decreasing
1000    decreasing!     increasing
1003    increasing      increasing
1009    increasing      increasing
1010    increasing      increasing
997     increasing!     decreasing
998     increasing      increasing
997     decreasing      decreasing
998     increasing      increasing
1002    decreasing!     increasing
```
