def sigma(i, n, f):
    total = 0    
    while n>=i:
        total += f(i)
        i+=1
    return total
    

def run(start, end, f):
    if type(start) is int and type(end) is int:
        return sigma(start, end, f)
    
    else:
        return 'start and end must be integers and start <= end'




if __name__ == '__main__':
    print(run(1,3, lambda x: 2*x+1))