lines = ['one', 'two', 'three']
with open('t1.txt', 'w') as f:
    for line in lines:
        f.write('\nString '+ line)
    print('Done')