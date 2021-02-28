# faxreader

A machine read account number from paper and create an input file that seems like this below.
A file conteins many account numbers.
  _  _     _  _  _  _  _ 
| _| _||_||_ |_   ||_||_|
||_  _|  | _||_|  ||_| _|

Each entries 4 lines long, and each line consist 27 characters.
The first 3 lines of each entry contain an account number that build written with pipes (|) and underscores(_) signs.
and the fourth line is empty.
Each account number has 9 digit (0-9).
A file contains about 500 entries

## Task 1: parse the account numbers

Account numbers should also be verified.
d1 = first digit, d2 = second digit etc.

checksum calculation: (d1+2*d2+3*d3+…+9*d9) mod 11 = 0

## Tasl 2: Calculate checksum for all account number
Create a report file, every line containing an account number.
Unidentified chars should be '?'.
ERR word means wrong account number.
ILL word means not recognizable account number.

457508000

664371495 ERR

86110??36 ILL

## Task 3: Create report file.