count = 1
total = 0
# BUG: Missing colon after while condition caused SyntaxError
# BUG: while count < 5 stops at 4, so sum is 10 not 15. Fixed to count <= 5 to include 5
while count <= 5:
    total = total + count
    count = count + 1
# BUG: Can't concatenate string and int with +. Fixed by using f-string to print int total
print(f"Sum of 1 to 5 is: {total}")
