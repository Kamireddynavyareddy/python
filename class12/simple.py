class parent:
    def m1(self):
        print("parent m1")
    def m2(self):
        print("parent m2")
    def m3(self):
        print("parent m3")
class child(parent):
    def m3(self):
        print("child class m3 method")
c1=child()
c1=m1()
c1=m2()
c1=m3()