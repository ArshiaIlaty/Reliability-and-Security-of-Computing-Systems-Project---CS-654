P = [5, 1]
prime = 17
a = 2
b = 2

def gcdExtended(a, b):
     if a == 0:
          return b, 0, 1
     gcd, x1, y1 = gcdExtended(b % a, a)
     x = y1 - (b // a) * x1
     y = x1
     return gcd, x, y

def double_point(point: list):
     x = point[0]
     y = point[1]

     s = ((3*(x**2)+a) * (gcdExtended(2*y, prime)[1])) % prime

     newx = (s**2 - x - x) % prime
     newy = (s * (x - newx) - y) % prime

     return [newx, newy]

def add_points(P: list, Q: list):
     x1 = P[0]
     y1 = P[1]
     x2 = Q[0]
     y2 = Q[1]

     s = ((y2 - y1) * ((gcdExtended(x2-x1, prime))[1] % prime)) % prime

     newx = (s**2 - x1 - x2) % prime
     newy = (s * (x1 - newx) - y1) % prime

     return [newx, newy]

Q = P
index = 2
while True:
     if Q[0] == P[0] and Q[1] == P[1]:
          print("doubling")
          Q = double_point(P)
     else:
          print("adding")
          Q = add_points(Q, P)

     if index == 12 :
          break

     print(f"{index}P = {Q}")
     index += 1