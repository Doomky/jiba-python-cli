# jiba-python-cli

The goal of the project is to implement a bistromatic calculator in Python.

## How to use

The command line is composed of two parts:
- default argument
- options (optional)

Ex:
- -b 10 -n infix "1 + 1"
- -b 10 -n rpn "+ 1 1"
- -b 2 -n infix "1 + 1"
- -b 2 -n rpn "+ 1 1"

###Default argument
When using the command send the calculation as an argument 

###Options
When using the command line, the following options can be added to commands

####Notations
Specify the notation: --notation/-n NOTATION<br/>
NOTATION can be: infix or rpn. default is infix.

####Base
Specify the base used in the operation: --base/-b BASE<br/>
BASE can be an integer. default is 10.

## How does it work
#### IO
The calculation is sent as string argument.<br/>
Ex: "1 + 1"
#### Parsing input
Input is parsed and token (numbers or operators: addition, subtraction, multiplication, division, braces) are created from calculation.
Tokens are stored in a queue used later on.<br/>
Ex: t('1'), t('+'), t('1')
#### RPN Transform
To ensure fast and efficient compute, token queue has to be in RPN (reverse polish notation) so the notation is forced to RPN.<br/>
Ex: t('+'), t('1'), t('1')
#### RPN Compute
Using the token queue the result is computed by reading tokens. 
Ex: t('2')
#### Operations
When read, operations pick numbers (or result of operation) to compute themselves.
#### Displaying output
Finally, result is displayed on stdout.