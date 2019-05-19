from z3 import *

a1 = 1
a2 = 3
a3 = 2
a4 = 9
a5 = 4
a6 = 0
a7 = 2
a8 = 7
a9 = 8
a10 = 4
a11 = 3
a12 = 4
a13 = 1
a14 = 9
a15 = 4
a16 = 6
a17 = 5
a18 = 3
a19 = -1
a20 = 4
a21 = 1
a22 = 4
a23 = 5
a24 = 3
a25 = 5


bA1 = Int('BA1')
bA2 = Int('BA2')
bA3 = Int('BA3')
bA4 = Int('BA4')
bA5 = Int('BA5')
bA6 = Int('BA6')
bA7 = Int('BA7')
bA8 = Int('BA8')
bA9 = Int('BA9')
bA10 = Int('BA10')
bA11 = Int('BA11')
bA12 = Int('BA12')
bA13 = Int('BA13')
bA14 = Int('BA14')
bA15 = Int('BA15')
bA16 = Int('BA16')
bA17 = Int('BA17')
bA18 = Int('BA18')
bA19 = Int('BA19')
bA20 = Int('BA20')
bA21 = Int('BA21')
bA22 = Int('BA22')
bA23 = Int('BA23')
bA24 = Int('BA24')
bA25 = Int('BA25')

bB1 = Int('BB1')
bB2 = Int('BB2')
bB3 = Int('BB3')
bB4 = Int('BB4')
bB5 = Int('BB5')
bB6 = Int('BB6')
bB7 = Int('BB7')
bB8 = Int('BB8')
bB9 = Int('BB9')
bB10 = Int('BB10')
bB11 = Int('BB11')
bB12 = Int('BB12')
bB13 = Int('BB13')
bB14 = Int('BB14')
bB15 = Int('BB15')
bB16 = Int('BB16')
bB17 = Int('BB17')
bB18 = Int('BB18')
bB19 = Int('BB19')
bB20 = Int('BB20')
bB21 = Int('BB21')
bB22 = Int('BB22')
bB23 = Int('BB23')
bB24 = Int('BB24')
bB25 = Int('BB25')

anA1 = (a1 * bA1 + a2 * bA6 + a3 * bA11 + a4 * bA16 + a5 * bA21) % 251
anA2 = (a1 * bA2 + a2 * bA7 + a3 * bA12 + a4 * bA17 + a5 * bA22) % 251
anA3 = (a1 * bA3 + a2 * bA8 + a3 * bA13 + a4 * bA18 + a5 * bA23) % 251
anA4 = (a1 * bA4 + a2 * bA9 + a3 * bA14 + a4 * bA19 + a5 * bA24) % 251
anA5 = (a1 * bA5 + a2 * bA10 + a3 * bA15 + a4 * bA20 + a5 * bA25) % 251

anA6 = (a6 * bA1 + a7 * bA6 + a8 * bA11 + a9 * bA16 + a10 * bA21) % 251
anA7 = (a6 * bA2 + a7 * bA7 + a8 * bA12 + a9 * bA17 + a10 * bA22) % 251
anA8 = (a6 * bA3 + a7 * bA8 + a8 * bA13 + a9 * bA18 + a10 * bA23) % 251
anA9 = (a6 * bA4 + a7 * bA9 + a8 * bA14 + a9 * bA19 + a10 * bA24) % 251
anA10 = (a6 * bA5 + a7 * bA10 + a8 * bA15 + a9 * bA20 + a10 * bA25) % 251

anA11 = (a11 * bA1 + a12 * bA6 + a13 * bA11 + a14 * bA16 + a15 * bA21) % 251
anA12 = (a11 * bA2 + a12 * bA7 + a13 * bA12 + a14 * bA17 + a15 * bA22) % 251
anA13 = (a11 * bA3 + a12 * bA8 + a13 * bA13 + a14 * bA18 + a15 * bA23) % 251
anA14 = (a11 * bA4 + a12 * bA9 + a13 * bA14 + a14 * bA19 + a15 * bA24) % 251
anA15 = (a11 * bA5 + a12 * bA10 + a13 * bA15 + a14 * bA20 + a15 * bA25) % 251

anA16 = (a16 * bA1 + a17 * bA6 + a18 * bA11 + a19 * bA16 + a20 * bA21) % 251
anA17 = (a16 * bA2 + a17 * bA7 + a18 * bA12 + a19 * bA17 + a20 * bA22) % 251
anA18 = (a16 * bA3 + a17 * bA8 + a18 * bA13 + a19 * bA18 + a20 * bA23) % 251
anA19 = (a16 * bA4 + a17 * bA9 + a18 * bA14 + a19 * bA19 + a20 * bA24) % 251
anA20 = (a16 * bA5 + a17 * bA10 + a18 * bA15 + a19 * bA20 + a20 * bA25) % 251

anA21 = (a21 * bA1 + a22 * bA6 + a23 * bA11 + a24 * bA16 + a25 * bA21) % 251
anA22 = (a21 * bA2 + a22 * bA7 + a23 * bA12 + a24 * bA17 + a25 * bA22) % 251
anA23 = (a21 * bA3 + a22 * bA8 + a23 * bA13 + a24 * bA18 + a25 * bA23) % 251
anA24 = (a21 * bA4 + a22 * bA9 + a23 * bA14 + a24 * bA19 + a25 * bA24) % 251
anA25 = (a21 * bA5 + a22 * bA10 + a23 * bA15 + a24 * bA20 + a25 * bA25) % 251

anB1 = (a1 * bB1 + a2 * bB6 + a3 * bB11 + a4 * bB16 + a5 * bB21) % 251
anB2 = (a1 * bB2 + a2 * bB7 + a3 * bB12 + a4 * bB17 + a5 * bB22) % 251
anB3 = (a1 * bB3 + a2 * bB8 + a3 * bB13 + a4 * bB18 + a5 * bB23) % 251
anB4 = (a1 * bB4 + a2 * bB9 + a3 * bB14 + a4 * bB19 + a5 * bB24) % 251
anB5 = (a1 * bB5 + a2 * bB10 + a3 * bB15 + a4 * bB20 + a5 * bB25) % 251
anB6 = (a6 * bB1 + a7 * bB6 + a8 * bB11 + a9 * bB16 + a10 * bB21) % 251
anB7 = (a6 * bB2 + a7 * bB7 + a8 * bB12 + a9 * bB17 + a10 * bB22) % 251
anB8 = (a6 * bB3 + a7 * bB8 + a8 * bB13 + a9 * bB18 + a10 * bB23) % 251
anB9 = (a6 * bB4 + a7 * bB9 + a8 * bB14 + a9 * bB19 + a10 * bB24) % 251
anB10 = (a6 * bB5 + a7 * bB10 + a8 * bB15 + a9 * bB20 + a10 * bB25) % 251
anB11 = (a11 * bB1 + a12 * bB6 + a13 * bB11 + a14 * bB16 + a15 * bB21) % 251
anB12 = (a11 * bB2 + a12 * bB7 + a13 * bB12 + a14 * bB17 + a15 * bB22) % 251
anB13 = (a11 * bB3 + a12 * bB8 + a13 * bB13 + a14 * bB18 + a15 * bB23) % 251
anB14 = (a11 * bB4 + a12 * bB9 + a13 * bB14 + a14 * bB19 + a15 * bB24) % 251
anB15 = (a11 * bB5 + a12 * bB10 + a13 * bB15 + a14 * bB20 + a15 * bB25) % 251
anB16 = (a16 * bB1 + a17 * bB6 + a18 * bB11 + a19 * bB16 + a20 * bB21) % 251
anB17 = (a16 * bB2 + a17 * bB7 + a18 * bB12 + a19 * bB17 + a20 * bB22) % 251
anB18 = (a16 * bB3 + a17 * bB8 + a18 * bB13 + a19 * bB18 + a20 * bB23) % 251
anB19 = (a16 * bB4 + a17 * bB9 + a18 * bB14 + a19 * bB19 + a20 * bB24) % 251
anB20 = (a16 * bB5 + a17 * bB10 + a18 * bB15 + a19 * bB20 + a20 * bB25) % 251
anB21 = (a21 * bB1 + a22 * bB6 + a23 * bB11 + a24 * bB16 + a25 * bB21) % 251
anB22 = (a21 * bB2 + a22 * bB7 + a23 * bB12 + a24 * bB17 + a25 * bB22) % 251
anB23 = (a21 * bB3 + a22 * bB8 + a23 * bB13 + a24 * bB18 + a25 * bB23) % 251
anB24 = (a21 * bB4 + a22 * bB9 + a23 * bB14 + a24 * bB19 + a25 * bB24) % 251
anB25 = (a21 * bB5 + a22 * bB10 + a23 * bB15 + a24 * bB20 + a25 * bB25) % 251

s = Solver()
s.add(bA1 > 31, bA1 <127 )
s.add(bA2 > 31, bA2 <127 )
s.add(bA3 > 31, bA3 <127 )
s.add(bA4 > 31, bA4 <127 )
s.add(bA5 > 31, bA5 <127 )
s.add(bA6 > 31, bA6 <127 )
s.add(bA7 > 31, bA7 <127 )
s.add(bA8 > 31, bA8 <127 )
s.add(bA9 > 31, bA9 <127 )
s.add(bA10 > 31, bA10 <127 )
s.add(bA11 > 31, bA11 <127 )
s.add(bA12 > 31, bA12 <127 )
s.add(bA13 > 31, bA13 <127 )
s.add(bA14 > 31, bA14 <127 )
s.add(bA15 > 31, bA15 <127 )
s.add(bA16 > 31, bA16 <127 )
s.add(bA17 > 31, bA17 <127 )
s.add(bA18 > 31, bA18 <127 )
s.add(bA19 > 31, bA19 <127 )
s.add(bA20 > 31, bA20 <127 )
s.add(bA21 > 31, bA21 <127 )
s.add(bA22 > 31, bA22 <127 )
s.add(bA23 > 31, bA23 <127 )
s.add(bA24 > 31, bA24 <127 )
s.add(bA25 > 31, bA25 <127 )

s.add(bB1 > 31, bB1 <127 )
s.add(bB2 > 31, bB2 <127 )
s.add(bB3 > 31, bB3 <127 )
s.add(bB4 > 31, bB4 <127 )
s.add(bB5 > 31, bB5 <127 )
s.add(bB6 > 31, bB6 <127 )
s.add(bB7 > 31, bB7 <127 )
s.add(bB8 > 31, bB8 <127 )
s.add(bB9 > 31, bB9 <127 )
s.add(bB10 > 31, bB10 <127 )
s.add(bB11 > 31, bB11 <127 )
s.add(bB12 > 31, bB12 <127 )
s.add(bB13 > 31, bB13 <127 )
s.add(bB14 > 31, bB14 <127 )
s.add(bB15 > 31, bB15 <127 )
s.add(bB16 > 31, bB16 <127 )
s.add(bB17 > 31, bB17 <127 )
s.add(bB18 > 31, bB18 <127 )
s.add(bB19 > 31, bB19 <127 )
s.add(bB20 > 31, bB20 <127 )
s.add(bB21 > 31, bB21 <127 )
s.add(bB22 > 31, bB22 <127 )
s.add(bB23 > 31, bB23 <127 )
s.add(bB24 > 31, bB24 <127 )
s.add(bB25 > 31, bB25 <127 )

s.add(anA1 == 234)
s.add(anA2 == 89)
s.add(anA3 == 41)
s.add(anA4 == 233)
s.add(anA5 == 126)
s.add(anA6 == 247)
s.add(anA7 == 120)
s.add(anA8 == 6)
s.add(anA9 == 187)
s.add(anA10 == 67)
s.add(anA11 == 236)
s.add(anA12 == 48)
s.add(anA13 == 63)
s.add(anA14 == 48)
s.add(anA15 == 70)
s.add(anA16 == 115)
s.add(anA17 == 222)
s.add(anA18 == 25)
s.add(anA19 == 247)
s.add(anA20 == 230)
s.add(anA21 == 142)
s.add(anA22 == 221)
s.add(anA23 == 195)
s.add(anA24 == 71)
s.add(anA25 == 243)

s.add(anB1 == 55)
s.add(anB2 == 62)
s.add(anB3 == 228)
s.add(anB4 == 192)
s.add(anB5 == 182)
s.add(anB6 == 98)
s.add(anB7 == 188)
s.add(anB8 == 55)
s.add(anB9 == 118)
s.add(anB10 == 79)
s.add(anB11 == 116)
s.add(anB12 == 203)
s.add(anB13 == 184)
s.add(anB14 == 187)
s.add(anB15 == 146)
s.add(anB16 == 25)
s.add(anB17 == 231)
s.add(anB18 == 181)
s.add(anB19 == 219)
s.add(anB20 == 197)
s.add(anB21 == 156)
s.add(anB22 == 164)
s.add(anB23 == 164)
s.add(anB24 == 32)
s.add(anB25 == 24)
print(s.check())
print(s.model())
