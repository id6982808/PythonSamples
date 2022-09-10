'''
Created on 2022/09/10

@author: nayuf

エントリポイント　と　メイン関数
'''

# pathに対象ソースディレクトリを追加しないとimportできない
import sys
sys.path.append('.')

import calltest

"""
 Main 関数
"""
def main():
    #print(sys.path)
    
    # calltest 関数を呼び出し
    calltest.call_02()

"""
 エントリポイント
"""
if __name__ == '__main__':
    main()
