import numpy as np
import multiprocessing as mp
#importing the necessary modules, `numpy` and `multiprocessing`, which are used for numerical operations and parallel processing, respectively.

def calculate_sum(array):
    partial_sum = np.sum(array)
    return partial_sum

#The function `calculate_sum(array)` is defined, which takes an array as input, calculates the sum of its elements using `numpy`'s `sum` function, and returns the partial sum.

if __name__ == '__main__':
    num_processes = mp.cpu_count()  
    print("Enter size of array")
    array_size = int(input()) 
    array = np.arange(1, array_size + 1)  
    print("Input Array:", array)
    chunk_size = array_size // num_processes
    chunks = [array[i:i+chunk_size] for i in range(0, array_size, chunk_size)]
    
    
    #The `if _name_ == '_main_':` condition checks whether the script is being run directly or being imported as a module.
    #The number of available processes or threads is determined using `mp.cpu_count()` and stored in the variable `num_processes`
    #The user is prompted to enter the size of the array.
    #he input array is created using `numpy`'s `arange` function, starting from 1 and ending at the specified size.
    #The array is divided into equal chunks, based on the number of processes available. Each chunk contains a portion of the original array.

    
    # Calculate partial sums using OpenMP
    with mp.Pool(processes=num_processes) as pool:
        partial_sums = pool.map(calculate_sum, chunks)


    #A `Pool` object is created using `multiprocessing.Pool` with the number of processes set to `num_processes`. This allows parallel processing of the chunks.
    #The `pool.map` function is used to apply the `calculate_sum` function to each chunk in parallel. It divides the chunks among the available processes and returns the partial sums.
    #The intermediate partial sums calculated by different processes are displayed, showing which process calculated which partial sum.


    
    for i, partial_sum in enumerate(partial_sums):
        print(f"Process {i}: Partial Sum = {partial_sum}")
        
    #The final sum is calculated by summing up the partial sums using `numpy`'s `sum` function.


   
    total_sum = np.sum(partial_sums)

    print("Total Sum:", total_sum)
    #The total sum is printed.

