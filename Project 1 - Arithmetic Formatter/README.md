Arithmetic Arranger
Overview
This project contains a Python function, arithmetic_arranger, that arranges and optionally solves a list of arithmetic problems (addition and subtraction). The problems are formatted vertically, and the function handles edge cases such as invalid operators, non-numeric inputs, and operand length limits.

Features
Supports Addition and Subtraction: The function accepts problems using the + and - operators.
Error Handling: Returns meaningful error messages for:
Too many problems (limit of 5).
Unsupported operators.
Non-digit characters in operands.
Operands longer than four digits.
Optional Answer Display: When the optional show_answers argument is set to True, the function also displays the results of the arithmetic operations.
