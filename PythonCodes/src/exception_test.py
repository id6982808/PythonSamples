"""
exception test
"""

def test():
    param = {'x':1000, 'z':0}
    try:
        x = param['x']
        y = param['y']
        z = x / y
        print(z)
    except KeyError as e:
        print('処理に必要なデータが存在しません')
        print(type(e), str(e))
    except ZeroDivisionError as e:
        print('除数に0が指定されました')
    except:
        print('原因不明のエラーが発生しました')

class ParamError(Exception):
    pass

def sample(num):
    if type(num) != int:
        raise ParamError('パラメータが不正です')
    
    return num * 10
