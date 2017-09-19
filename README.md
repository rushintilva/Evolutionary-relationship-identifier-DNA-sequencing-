# Evolutionary-relationship-identifier-DNA-sequencing-

It is the python program which can be used by scientists to automatically find the evolutionary relation between two species with any number of indel(Indel is a molecular biology term for an insertion or deletion of bases in the genome of an organism).

Let,  x be the number of characters in inputted DNA sequence.
      y be the number of maximum indels.
      n be the number of total permutations(time of execution is dependent on n).

y (∑) a = 1 is summation a=1 to y

n = 1 + y (∑) (a = 1) [(x + 1)*(x + 2)*(x + 3)...(x + a)]

