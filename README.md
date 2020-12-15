# jiba-python-cli

The goal of the project is to implement a bistromatic calculator in Python.

## IO

### Parsing input

### Displaying output

## Compute

### Operations


TokenQueue:
  - tokenQueue: queue\<token>
  - getNextNumber(): Number (throw exception)

Token:
  - toString(): string
  - compute(): Number

Number(Token):
  - digits: list\<int>
  - sign: boolean
  - isZero(): boolean
  - compute(): Number

Operator(Token):
  - compute(): Number
    
Addition(Operator):
  - ...
  
...

input -> token list -> reverse polish notation -> token list -> compute -> token (number) -> output

4e5 => 4 * 10 ^ 5 => * ^ 10 5 4

(7 - 5) * ... => * - 7 5 ...