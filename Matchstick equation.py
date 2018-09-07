'''
Matchstick equation
'''
class Matchstick:
    def compute_equation(self, number):
        '''
        Input: int
        number of sticks
        Output: str
        satisfied equations
        '''
        # how many sticks needed to form correspond number
        num_dict = {0 : 6, 1 : 2, 2 : 5,
                    3 : 5, 4 : 4, 5 : 5,
                    6 : 6, 7 : 3, 8 : 7,
                    9 : 6}
        # add and equal symbols both need two sticks
        add, equal = 2, 2

        num_sticks = number - add - equal

        # form equation a+b=c
        count = 0
        for a in range(100):
            for b in range(100):
                for c in range(100):
                    if a+b == c:
                        if a > 9:
                            num_a = num_dict[a%10] + num_dict[a//10]
                        else:
                            num_a = num_dict[a]
                        if b > 9:
                            num_b = num_dict[b%10] + num_dict[b//10]
                        else:
                            num_b = num_dict[b]
                        if c > 9:
                            num_c = num_dict[c%10] + num_dict[c//10]
                        else:
                            num_c = num_dict[c]
                        if num_a + num_b + num_c == num_sticks:
                            print("%d + %d = %d" %(a,b,c))
                            count += 1
        print("The number of total: %d" %(count))

if __name__ == '__main__':
    ME = Matchstick()
    number = input("Please input matchsticks limit number: ")
    ME.compute_equation(int(number))
