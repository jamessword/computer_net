import matplotlib.pyplot as plt

num1 = 0B0110011001100000
num2 = 0B0101010101010101
num3 = 0B1000111100001100
numtest = 0B1111111111111111
udplist = [num1, num2, num3]


def UDPCheck(list):
    result = 0
    for number in list:
        result = (result + number) % 0b10000000000000000 + (result + number) // 0b10000000000000000
    return format(result ^ 0b1111111111111111, '016b')   #Roll back after overflow


x=[num2,num1,num3]
y=[UDPCheck([num2,numtest]),UDPCheck([num1,numtest]),UDPCheck([num3,numtest])]
plt.plot(x,y)
plt.show()
print("checksum is " + UDPCheck(udplist))


