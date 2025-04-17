class grand parent:
    def m1(self):
        print("grand parent m1")
        def m2(self):
            print("grand parent m2")
            def m3(self):
                print("grand parent m3")
class parent(grand parent):
    def m2(self):
        print("parent m2")
        def m3(slef):
            print("parent m3")
class child(parent):