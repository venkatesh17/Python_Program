"""
          1
         2 2
        3 3 3
       4 4 4 4
      5 5 5 5 5
     6 6 6 6 6 6
    7 7 7 7 7 7 7
   8 8 8 8 8 8 8 8
  9 9 9 9 9 9 9 9 9

          1
         22
        333
       4444
      55555
     666666
    7777777
   88888888
  999999999

          A
         BB
        CCC
       DDDD
      EEEEE
     FFFFFF
    GGGGGGG
   HHHHHHHH
  IIIIIIIII

          *
         **
        ***
       ****
      *****
     ******
    *******
   ********
  *********

"""


def pattern23():
    n = 10
    for i in range(1, n):
        # print(" "*(n-i), (str(i))*i, end=" ")
        # print(" " * (n - i), (str(i)+" ") * i)
        # print(" "*(n-i), (chr(64+i))*i, end=" ")
        print(" " * (n - i), (chr(64 + i)+" ") * i, end=" ")
        # print(" "*(n-i), "*"*i, end=" ")
        print()


