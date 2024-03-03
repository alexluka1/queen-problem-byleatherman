# Queen Problem

## Description

Common programming puzzle which invloves placing chess queens on an 8x8 chess board without any of the queen threatening each other until there is no space left, and finding the maximum number of queens.

Solved by just randomly placing queens until there is no space left to place them, repeating 1000 times and just assuming it has found the best solution. The solution of someone with few braincells atm (me).

## Solution

Done with Python, Numpy

Random Method:

- 8x8 chess board can be represtented as a 2d array
- Can place queen randomly, and get rid off all unavailable places, repeat until no spaces left
  - Record best number of places in array of coordinates
- Works well only because we know the optimal outcome

## Run It

- Relies on numpy
  - Can install using `pipenv`, as done here, or just using `pip`

Method 1 (pipenv):

- Install pipenv
- In terminal run `pipenv install` - this will install dependacies from Pipfile and Pipfile.lock
- In terminal run `pipenv shell` - this will activate the virtual environment
- In terminal run `python3 queenProblem.py` - this will run the Python script
  - If `python3` is not found try `python queenProblem.py`
  - If still have problem running script check if Python is installed properly

Method 2 (pip):

- In terminal run `pip install numpy` - install numpy on your computer
- In terminal run `python3 queenProblem.py` - this will run the Python script
  - If `python3` is not found try `python queenProblem.py`
  - If still have problem running script check if Python is installed properly
