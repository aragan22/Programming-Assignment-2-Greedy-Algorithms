Programming Assignment 2 – Greedy Algorithms Cache Eviction Policy
Simulator (FIFO, LRU, OPTFF)

Student: Aidan Ragan Repository:
https://github.com/aragan22/Programming-Assignment-2-Greedy-Algorithms

  ---------------------
  PROJECT DESCRIPTION
  ---------------------

This project implements and compares three cache eviction policies:

1.  FIFO (First-In, First-Out)
2.  LRU (Least Recently Used)
3.  OPTFF (Belady’s Farthest-in-Future optimal offline algorithm)

The program reads a cache capacity and a sequence of requests from an
input file and simulates each policy on the same request sequence. It
then prints the number of cache misses for each policy.

The purpose of this assignment is to understand greedy strategies for
cache replacement and to empirically compare the performance of
different eviction algorithms.

  ----------------------
  REPOSITORY STRUCTURE
  ----------------------

Programming-Assignment-2-Greedy-Algorithms/

src/ cache_sim.py Main Python program that simulates FIFO, LRU, and
OPTFF.

data/ example.in Example input file.

    file1.in
    file2.in
    file3.in
    Additional request sequences used for testing.

tests/ example.out Expected output for example.in.

README.md / README.txt Instructions for running the program.

  --------------
  REQUIREMENTS
  --------------

Python 3.8 or newer

No external libraries are required. The program only uses Python’s
standard library.

  --------------
  INPUT FORMAT
  --------------

The program reads input from standard input with the following format:

k m r1 r2 r3 … rm

Where:

k = cache capacity (k >= 1) m = number of requests r1…rm = sequence of
integer request IDs

Example:

3 10 1 2 3 1 2 4 1 2 3 4

  ---------------
  OUTPUT FORMAT
  ---------------

The program prints the number of cache misses for each eviction policy
in the following format:

FIFO : LRU : OPTFF :

Example output:

FIFO : 8 LRU : 6 OPTFF : 5

  ------------------------
  HOW TO RUN THE PROGRAM
  ------------------------

1.  Navigate to the repository directory:

cd Programming-Assignment-2-Greedy-Algorithms

2.  Run the simulator with an input file:

python3 src/cache_sim.py < data/example.in

Example:

python3 src/cache_sim.py < data/example.in

Expected output:

FIFO : 8 LRU : 6 OPTFF : 5

  -----------------------
  ADDING NEW TEST FILES
  -----------------------

To test the program with a different request sequence:

1.  Create a new input file in the data/ directory.

Example:

data/new_test.in

2.  Add the request sequence using the required format.

3.  Run the program:

python3 src/cache_sim.py < data/new_test.in

  ------------------------
  ALGORITHM DESCRIPTIONS
  ------------------------

FIFO (First-In First-Out)

The FIFO algorithm evicts the item that has been in the cache the
longest. It does not consider how frequently or recently an item was
used.

LRU (Least Recently Used)

The LRU algorithm evicts the item whose most recent access time is the
oldest. This algorithm exploits temporal locality by keeping recently
used items in the cache.

OPTFF (Belady’s Farthest-in-Future)

OPTFF is the optimal offline algorithm. When the cache is full, it
evicts the item whose next request occurs farthest in the future, or
that never appears again.

Because it knows the entire request sequence in advance, OPTFF produces
the minimum possible number of cache misses for any fixed sequence.

  ---------------------
  REPRODUCING RESULTS
  ---------------------

To reproduce the example output:

python3 src/cache_sim.py < data/example.in

To test other files:

python3 src/cache_sim.py < data/file1.in python3 src/cache_sim.py <
data/file2.in python3 src/cache_sim.py < data/file3.in

  -------
  NOTES
  -------

All algorithms operate on the same request sequence to allow direct
comparison of cache misses.

The OPTFF implementation precomputes the next occurrence of each request
so that it can determine which cached item will be used farthest in the
future.

------------------------------------------------------------------------
