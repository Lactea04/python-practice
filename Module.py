#Module.py



#def add(a,b):
#    return a+b

#def sub(a, b):
#    return a - b


#module로 Module을 가져왔을 때 print가 실행되는 것을 방지 (파일을 직접 실행했을 때만 print 출력)ㅑㅡ
#if __name__ == "__main__":
#    print(add(3, 6))
#    print(sub(9, 3))


class math():
    def __init__(self):
        self.pi = 3.141592653589793
        self.r = 0

    def solu(self, r):
        self.r = r
        circle_side = self.pi*self.r**2

        return (circle_side)

    def add(self, a, b):
        return a + b

