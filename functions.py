from tokenizer import Token, TokenType

g = "Hello, World!"
w = "Hello World"
b = "0123456789"
o = "123456789"
a = "abcdefghijklmnopqrstuvwxyz"
u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = 10
d = 16
e = 256
f = 32768
h = 65536
i = 2048
j = 4906
k = 1024
l = 128
n = -1
p0 = 10
p1 = 16
p2 = 256
p3 = 32768
p4 = 65536
p5 = 2048
p6 = 4906
p7 = 1024
p8 = 128


def add(a1, a2):
    """Add two numbers"""
    return Token(TokenType.NUMBER, a1.value + a2.value)
