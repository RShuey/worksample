#quadratic plugin, or how ever you spell that.
#plugins are structured to function as libraries
#as well.  They serve a dual purpose.

#problem format:
#(x + a)(x + b)      <- answer
#x^2 + (ab)(x) + ab  <- question

import random

class quadratic():
    def __init__(self):
        self.zeroA = random.randint(-9, 9)
        self.zeroB = random.randint(-9, 9)

    #legitimate variables
    __zeroA = 0
    __zeroB = 0
    
    #Fget the first zero
    def ZAget(self):
        return self.__zeroA
    #Fset the first zero
    def ZAset(self, setto):
        if setto == 0:
            self.__zeroA = 1
        else:
            self.__zeroA = setto

    #Fget the second zero
    def ZBget(self):
        return self.__zeroB
    #Fset the second zero
    def ZBset(self, setto):
        if setto == 0:
            self.__zeroB = 1
        else:
            self.__zeroB = setto

    #defigning the properties for the variables
    zeroA = property(fget = ZAget, fset = ZAset)
    zeroB = property(fget = ZBget, fset = ZBset)

    #problem for the student to read
    def problem(self):
        out  = "Find the zeros in this quadratic.  Show all work\n<br>"
        out += "x^2 + " + str(self.zeroA + self.zeroB) + "x + " + str(self.zeroA * self.zeroB)
        return out
    #worked solution of the teacher
    def solution(self):
        out  = self.problem() + "\n<br>\n<br>\n<br>" #we probably want to know the original problem first
        out += "x^2 + " + str(self.zeroA + self.zeroB) + "x + " + str(self.zeroA * self.zeroB) + "\n<br>"
        out += "x^2 + [(" + str(self.zeroA) + ")+(" + str(self.zeroB) + ")]x (" + str(self.zeroA) + ")(" + str(self.zeroB) + ")\n<br>"
        out += "(x + " + str(self.zeroA) + ")(x + " + str(self.zeroB) + ") \n<br>"
        out += "x has the zeros " + str(self.zeroA * -1) + " and " + str(self.zeroB * -1) + "."
        return out

def main():
    question = quadratic()
    print(question.problem() + "|||" + question.solution())
    exit(0)

main()
