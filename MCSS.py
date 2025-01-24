import random

def random_vector(size):
    """
    Generates a vector of 1000 elements with random positive and negative integers
    """
    vector = []
    for _ in range(size):
        vector.append(random.randint(-100, 100))
    return vector

def MCSS(a):
    """
    Finds the maximum contiguous subsequence sum in a vector.
    """
    
    largest = 0
    acc = 0
    i = 0
    start = 0
    end = 0

    
    for j in range(len(a)):
        acc += a[j]
        
        if acc > largest :
            largest = acc
            start, end = i, j
            
        elif acc < 0:
            i = j + 1
            acc = 0
    
    return largest, start, end

# Generating a vector of 1000 random integers
vector = random_vector(1000)


# Finding the maximum contiguous subsequence sum along with indices
max_sum, start_index, end_index = MCSS(vector)


# Print the results
print("The maximum contiguous subsequence sum is:", max_sum)
print("It starts at index:", start_index)
print("It ends at index:", end_index)
