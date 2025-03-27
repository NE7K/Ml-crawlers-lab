# nunu = {
#   'q' : 'eat',
#   'w' : 'snowball'
# }
# garen = {
#   'q' : 'strike',
#   'w' : 'courage'
# }

# 오브젝트 한줄컷 기계
class Hero:
    def __init__(self, 구멍):
        self.q = 구멍
        self.w = 'snowball'
    
    def hello(self):
        print('hello')
        
omg = Hero('구멍띠')
print(omg.q)
omg.hello()