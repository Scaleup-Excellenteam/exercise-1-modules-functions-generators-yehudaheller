def interleave(*params):
    iterators = [iter(x) for x in params] # save first of the object in index 0 and first in index 1 etc'....
                                         # when the it removed (in line 13 after the except) we return to line 2
                                         # and read the nexts indexs ( secound in param that in index 1 and secound in the parm in index 2 etc')

    # print(next(iterators[2]))
    # print(next(iterators[2]))

    while iterators: # in first "next" save a,1,!
        for it in iterators:
            try:
                yield next(it)
            except StopIteration:
                iterators.remove(it) # remove the itrator, so the while not continue anymore


print(list(interleave('abc', [1, 2, 3], ('!', '@', '#'))))