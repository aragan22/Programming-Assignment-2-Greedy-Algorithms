Programming Assignment 2 – Greedy Algorithms
Cache Eviction Policy Simulator (FIFO, LRU, OPTFF)

Student: Aidan Ragan
Repository:
https://github.com/aragan22/Programming-Assignment-2-Greedy-Algorithms


------------------------------------------------------------
PROJECT DESCRIPTION
------------------------------------------------------------

This project implements and compares three cache eviction policies:

1. FIFO (First-In, First-Out)
2. LRU (Least Recently Used)
3. OPTFF (Belady’s Farthest-in-Future optimal offline algorithm)

The program reads a cache capacity and a sequence of requests from an
input file and simulates each policy on the same request sequence.
It then prints the number of cache misses for each policy.

The purpose of this assignment is to understand greedy strategies for
cache replacement and to empirically compare the performance of
different eviction algorithms.


------------------------------------------------------------
REPOSITORY STRUCTURE
------------------------------------------------------------

Programming-Assignment-2-Greedy-Algorithms/

src/
    cache_sim.py
    Main Python program that simulates FIFO, LRU, and OPTFF.

data/
    example.in
        Example input file

    file1.in
    file2.in
    file3.in
        Additional request sequences used for testing

tests/
    example.out
        Expected output for example.in

README.md / README.txt
    Instructions for running the program and written answers


------------------------------------------------------------
REQUIREMENTS
------------------------------------------------------------

Python 3.8 or newer

No external libraries are required. The program only uses Python's
standard library.


------------------------------------------------------------
INPUT FORMAT
------------------------------------------------------------

The program reads input from standard input with the following format:

k m
r1 r2 r3 ... rm

Where:

k = cache capacity (k ≥ 1)
m = number of requests
r1...rm = sequence of integer request IDs

Example:

3 10
1 2 3 1 2 4 1 2 3 4


------------------------------------------------------------
OUTPUT FORMAT
------------------------------------------------------------

The program prints the number of cache misses for each eviction policy
in the following format:

FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>

Example output:

FIFO  : 8
LRU   : 6
OPTFF : 5


------------------------------------------------------------
HOW TO RUN THE PROGRAM
------------------------------------------------------------

1. Navigate to the repository directory:

cd Programming-Assignment-2-Greedy-Algorithms

2. Run the simulator with an input file:

python3 src/cache_sim.py < data/example.in

Example:

python3 src/cache_sim.py < data/example.in

Expected output:

FIFO  : 8
LRU   : 6
OPTFF : 5


------------------------------------------------------------
ADDING NEW TEST FILES
------------------------------------------------------------

To test the program with a different request sequence:

1. Create a new input file in the data/ directory.

Example:

data/new_test.in

2. Add the request sequence using the required format.

3. Run the program:

python3 src/cache_sim.py < data/new_test.in


------------------------------------------------------------
ALGORITHM DESCRIPTIONS
------------------------------------------------------------

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
evicts the item whose next request occurs farthest in the future,
or that never appears again.

Because it knows the entire request sequence in advance, OPTFF produces
the minimum possible number of cache misses for any fixed sequence.


------------------------------------------------------------
REPRODUCING RESULTS
------------------------------------------------------------

To reproduce the example output:

python3 src/cache_sim.py < data/example.in

To test the other files:

python3 src/cache_sim.py < data/file1.in
python3 src/cache_sim.py < data/file2.in
python3 src/cache_sim.py < data/file3.in


------------------------------------------------------------
WRITTEN COMPONENT
------------------------------------------------------------

Question 1: Empirical Comparison

We used three nontrivial input files with at least 50 requests.

Input File | k | m  | FIFO | LRU | OPTFF
-----------------------------------------
File1      | 3 | 60 | 60   | 60  | 32
File2      | 3 | 54 | 19   | 11  | 11
File3      | 3 | 60 | 56   | 54  | 27

Does OPTFF have the fewest misses?

Yes. OPTFF has the smallest number of misses for every input sequence.
This is expected because OPTFF has full knowledge of the future request
sequence and always evicts the item whose next use occurs farthest in
the future. Because of this, it can always make the eviction decision
that minimizes future cache misses.

How does FIFO compare to LRU?

LRU generally performs better than FIFO when the request sequence has
temporal locality. In File2 and File3 we see that LRU produces fewer
misses than FIFO because it keeps recently used items in the cache.
FIFO simply removes the item that has been in the cache the longest,
which can sometimes remove items that will be used again very soon.
In File1 both algorithms perform poorly because the working set is
larger than the cache size and the sequence cycles repeatedly.


------------------------------------------------------------
Question 2: Bad Sequence for LRU (k = 3)
------------------------------------------------------------

Consider the sequence:

k = 3
1 2 3 1 2 4 1 2 3 4

LRU Simulation:

1 -> miss
2 -> miss
3 -> miss
1 -> hit
2 -> hit
4 -> miss (evict 3)
1 -> hit
2 -> hit
3 -> miss (evict 4)
4 -> miss (evict 1)

Total LRU misses = 6


OPTFF Simulation:

1 -> miss
2 -> miss
3 -> miss
1 -> hit
2 -> hit
4 -> miss

At this point the cache is {1,2,3}. Looking ahead in the sequence:

next(1) = 7
next(2) = 8
next(3) = 9

Since 3 is used farthest in the future, OPTFF evicts 3.

Continuing the simulation results in only 5 misses.

Total OPTFF misses = 5

Therefore:

LRU   = 6 misses
OPTFF = 5 misses

This shows that OPTFF can perform strictly better than LRU because LRU
only uses past information, while OPTFF uses the full future sequence
to make optimal eviction decisions.


------------------------------------------------------------
Question 3: Proof that OPTFF is Optimal
------------------------------------------------------------

Let OPTFF be Belady's Farthest-in-Future algorithm and let A be any
offline algorithm that knows the entire request sequence.

We prove that OPTFF never produces more misses than A using an
exchange argument.

Suppose algorithm A makes a different eviction choice than OPTFF
at some step when the cache is full. Let v_OPT be the page that
OPTFF evicts and v_A be the page that A evicts.

OPTFF chooses the page whose next request occurs farthest in the
future. This means that every other page in the cache will be used
sooner than v_OPT.

If we modify algorithm A so that it evicts v_OPT instead of v_A,
we can adjust the future behavior of A so that the total number
of misses does not increase. When v_A is requested again, A would
have missed anyway because it previously evicted v_A.

By repeatedly applying this swap argument, any optimal algorithm
can be transformed so that it makes the same eviction decisions
as OPTFF without increasing the number of misses.

Therefore no algorithm can produce fewer misses than OPTFF on any
fixed request sequence.

Thus OPTFF is optimal.


------------------------------------------------------------
NOTES
------------------------------------------------------------

All algorithms operate on the same request sequence to allow direct
comparison of cache misses.

The OPTFF implementation precomputes the next occurrence of each
request so that it can determine which cached item will be used
farthest in the future.

------------------------------------------------------------
