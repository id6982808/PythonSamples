'''
リスト内包表記
Created on 2022/09/19

@author: nayuf
'''

def list_test():
    dict = {'a':'test_a', 'b':'test_b'}
    print(dict)
    
    dict2 = {i : key + dict[key] for i, key in enumerate(dict)}
    print(dict2)
