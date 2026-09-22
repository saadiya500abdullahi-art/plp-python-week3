# Week 3 Assignment on Conditions and Loops

## Files Included
- **grade_reporter.py** - Loops through scores list [72, 45, 90, 61, 38], assigns grades (A>=80, B>=70, C>=50, F<50), counts passed/failed and calculates average.
- **bug_hunt.py** - Fixed while-loop program that sums 1 to 5 to get 15.
- **README.md** - Assignment documentation.

## How It Works
The grade_reporter uses for loop and if-elif-else to check each score.

## The Hardest Bug
The hardest bug was the logic bug count < 5 vs count <= 5 because there was no error message, it just gave 10. I knew something was wrong because the expected output was 15 but the program printed 10, so I checked the loop condition and range.
