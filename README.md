# jiba-python-cli

The goal of the project is to implement a bistromatic calculator in Python.

## How to use

The command line is composed of two parts:
- default argument = the calculation(s) (at least one)
- options (optional)

Those information can be seen by showing the help with :

    python main.py --help


### Some examples

1) No base specified :

       python main.py -n infix "(10 - 4) / 2"

    Output :
    
       Selected Notation: infix
       Selected Base: 10
       Calculation(s): ('(10 - 4) / 2',)
       Result: 3

2) Multiple calculations in reverse polish notation :

       python main.py -b 10 -n rpn "7 8 *" "7 3 - 4 8 + 2 * / 1 -"
       
    Output :
    
       Selected Notation: rpn
       Selected Base: 10
       Calculation(s): ('7 8 *', '7 3 - 4 8 + 2 * / 1 -')
       Result: 56
       Result: 12
   
3) Base 2 and multiple calculations :
    
       python main.py -b 2 "01 + 10" "10 * 1"
       
   Output :
   
       Selected Notation: infix
       Selected Base: 2
       Calculation(s): ('01 + 10', '10 * 1')
       Result: 11
       Result: 10

4) Base 2 and calculation in reverse polish notation :

       python main.py -b 2 -n rpn "101 11 +"
    
   Output :
   
       Selected Notation: rpn
       Selected Base: 2
       Calculation(s): ('101 11 +',)
       Result: 1000

### Default argument

When using the command line, send the calculation(s) as argument 

### Options

When using the command line, the following options can be added :

#### Notation

Specify the notation :

    --notation NOTATION

or :

    -n NOTATION

NOTATION can be: `infix` or `rpn` (default is `infix`).

#### Base

Specify the base used in the calculation :

    --base BASE
    
or :

    -b BASE

BASE must be: an integer between `2` and `10` (default is `10`).

## How does it work

Here, we will take a simple example: `1 + 1`

### IO

The calculation is sent as a string argument.  
Ex : "1 + 1"

### Parsing input

Input is parsed and tokens (numbers, parenthesis or operators: addition, subtraction, multiplication, division, power) are created from the calculation.  
Tokens are stored in a stack used later on.     
Ex :

|       |        |          |        |
| ----- | :----: | :------: | :----: |
| Token |  '1'   |   '+'    |  '1'   | 
| Type  | number | addition | number |

### RPN Transform

To ensure fast and efficient compute, the token stack has to be in RPN (reverse polish notation) so the notation is forced to RPN.  
Ex :

|       |        |        |          |
| ----- | :----: | :----: | :------: |
| Token |  '1'   |  '1'   |   '+'    | 
| Type  | number | number | addition |

### RPN Compute

Using the token stack, the result is computed by reading tokens.  
Ex :

|       |        |
| ----- | :----: |
| Token |  '2'   |
| Type  | number |

### Operations

When reading the tokens, it's the operations that pick numbers (or the result of a calculation) to compute themselves.

### Displaying output

Finally, the result(s) of the calculation(s) is(are) displayed on stdout with a recap of the option(s) and calculation(s) passed.  
Ex :

    Selected Notation: infix
    Selected Base: 10
    Calculation(s): ('1 + 1',)
    Result: 2
