class Solution:
    def addBinary(self, a: str, b: str) -> str:

        '''
        100
        110
        answer:
        1010
        '''
        res = ""
        # return bin(int(a, 2) + int(b, 2))[2:]

        # converts the str to its decimal int format
        # test case 
        # a 11 = 2^1 + 2^0 = 3 
        # b 1 = 2^0 = 1 

        a1=int(a,2)
        b1=int(b,2)


        print(a1)
        print(b1)

        # adds the values together
        sum1=a1+b1
        # turns it back into binary format
        print(bin(sum1))
        # splice the string to get the 0b out of the string
        return bin(sum1)[2:]
