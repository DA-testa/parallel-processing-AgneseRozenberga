# python3

def parallel_processing(n, m, data):
    output = []
    paralelaisproces = [0] * n
    for i in range (m):
        pirmie=paralelaisproces.index(min(paralelaisproces))
        sakums= paralelaisproces[pirmie]
        paralelaisproces[pirmie] = data[i] +paralelaisproces[pirmie]
        output.append((pirmie, sakums) ) 
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = map(int, input(). split())
    m = map(int, input(). split())


    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list (map(int, input(). split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for pirmie,sakums in result:
        print(pirmie, sakums)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
