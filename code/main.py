# 没想到有啥好写的题材，就随意敲一些吧
class hilichurl():
    def __init__(self, name):
        self.name = name
        print(self.name, ": hi!")

    def say(self, words):
        print(self.name, words)


class obtuse_hilichurl(hilichurl):
    def obtuse(self):
        print(self.name, ": i am obtuse's hilichurl.", end="\n")

    def congratulate(self,*x):
        num=len(x)
        print(x[0]+x[1]+self.name,"our %d hilichurl 祝您新春快乐！"%(num+1),sep=",",end=" ")

one = hilichurl("one")
two = hilichurl("two")
one.say(": Olah a,Muhe ye!")
two.say(": Mosi Mita La.")
one.say(": Celi dada,mimi nunu.")
three = obtuse_hilichurl("three")
three.obtuse()
three.say(": i wish you have a best day!")
three.congratulate("one","two")