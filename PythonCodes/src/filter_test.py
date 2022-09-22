'''
Created on 2022/09/22

@author: nayuf
'''

def is_odd(n):
    return (n % 2) == 1

def filter_test(f, data_in):
    data_out = filter(f, data_in)
    return data_out
