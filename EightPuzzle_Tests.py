##8-puzzle test cases. Note that times are on a different machine.
##

from eightPuzzle import *

se = SearchEngine('astar', 'full')

# Test Group 1
eightPuzzle_set_goal([1, 2, 3, 8, 0, 4, 7, 6, 5])
# Easy
s2 = eightPuzzle("START", 0, [1, 3, 4, 8, 6, 2, 7, 0, 5])

print("===========Test 1, EASY, ASTAR, h_MHDist==============")
se.search(s2, eightPuzzle_goal_fn, h_MHDist)

# Master solution Results (edited)

# Search Successful! Solution cost = 5
# Solution Path:
# Action= "START", S0, g-value = 0, (Initial State)
#  ==>  Action= "Blank-Up", S1, g-value = 1, (From S0)
#  ==>  Action= "Blank-Right", S6, g-value = 2, (From S1)
#  ==>  Action= "Blank-Up", S9, g-value = 3, (From S6)
#  ==>  Action= "Blank-Left", S12, g-value = 4, (From S9)
#  ==>  Action= "Blank-Down", S13, g-value = 5, (From S12)
# Search time = 0.0, nodes expanded = 12, states generated = 16, states cycle check pruned = 4
#
print("======================================================")

print("===========Test 1, EASY, ASTAR, h_misplacedTiles======")
se.search(s2, eightPuzzle_goal_fn, h_misplacedTiles)

# Master solution Results (edited)
# ============================
# Search Successful! Solution cost = 5
# Solution Path:
# Action= "START", S0, g-value = 0, (Initial State)
#  ==>  Action= "Blank-Up", S1, g-value = 1, (From S0)
#  ==>  Action= "Blank-Right", S6, g-value = 2, (From S1)
#  ==>  Action= "Blank-Up", S12, g-value = 3, (From S6)
#  ==>  Action= "Blank-Left", S15, g-value = 4, (From S12)
#  ==>  Action= "Blank-Down", S16, g-value = 5, (From S15)
# ----------------------------
# Search time = 0.03125, nodes expanded = 14, states generated = 19, states cycle check pruned = 5

print("======================================================")

# Medium 1
s3 = eightPuzzle("START", 0, [2, 8, 1, 0, 4, 3, 7, 6, 5])

print("===========Test 1, MEDIUM 1, ASTAR, h_MHDist==============")
se.search(s3, eightPuzzle_goal_fn, h_MHDist)

# Master solution Results (edited)
# Search Successful! Solution cost = 9
# Solution Path:
# Action= "START", S19, g-value = 0, (Initial State)
#  ==>  Action= "Blank-Up", S2, g-value = 1, (From S19)
#  ==>  Action= "Blank-Right", S7, g-value = 2, (From S2)
#  ==>  Action= "Blank-Right", S9, g-value = 3, (From S7)
#  ==>  Action= "Blank-Down", S11, g-value = 4, (From S9)
#  ==>  Action= "Blank-Left", S15, g-value = 5, (From S11)
#  ==>  Action= "Blank-Left", S19, g-value = 6, (From S15)
#  ==>  Action= "Blank-Up", S21, g-value = 7, (From S19)
#  ==>  Action= "Blank-Right", S24, g-value = 8, (From S21)
#  ==>  Action= "Blank-Down", S25, g-value = 9, (From S24)
# ----------------------------
# Search time = 0.0, nodes expanded = 19, states generated = 28, states cycle check pruned = 9

print("======================================================")

print("===========Test 1, MEDIUM 1, ASTAR, h_misplacedTiles======")
se.search(s3, eightPuzzle_goal_fn, h_misplacedTiles)

# Master solution Results (edited)
# Search Successful! Solution cost = 9, Goal state:
# Solution Path:
# Action= "START", S19, g-value = 0, (Initial State)
#  ==>  Action= "Blank-Up", S2, g-value = 1, (From S19)
#  ==>  Action= "Blank-Right", S5, g-value = 2, (From S2)
#  ==>  Action= "Blank-Right", S11, g-value = 3, (From S5)
#  ==>  Action= "Blank-Down", S30, g-value = 4, (From S11)
#  ==>  Action= "Blank-Left", S34, g-value = 5, (From S30)
#  ==>  Action= "Blank-Left", S38, g-value = 6, (From S34)
#  ==>  Action= "Blank-Up", S54, g-value = 7, (From S38)
#  ==>  Action= "Blank-Right", S57, g-value = 8, (From S54)
#  ==>  Action= "Blank-Down", S58, g-value = 9, (From S57)
# ----------------------------
# Search time = 0.03125, nodes expanded = 41, states generated = 61, states cycle check pruned = 20

print("======================================================")

# Medium 2
s4 = eightPuzzle("START", 0, [2, 8, 1, 4, 6, 3, 0, 7, 5])

print("===========Test 1, MEDIUM 2, ASTAR, h_MHDist==============")
se.search(s4, eightPuzzle_goal_fn, h_MHDist)

# Master solution Results (edited)
# Search Successful! Solution cost = 12
# Solution Path:
# Action= "START", S61, g-value = 0, (Initial State)
#  ==>  Action= "Blank-Right", S2, g-value = 1, (From S61)
#  ==>  Action= "Blank-Up", S3, g-value = 2, (From S2)
#  ==>  Action= "Blank-Left", S9, g-value = 3, (From S3)
#  ==>  Action= "Blank-Up", S21, g-value = 4, (From S9)
#  ==>  Action= "Blank-Right", S42, g-value = 5, (From S21)
#  ==>  Action= "Blank-Right", S44, g-value = 6, (From S42)
#  ==>  Action= "Blank-Down", S46, g-value = 7, (From S44)
#  ==>  Action= "Blank-Left", S50, g-value = 8, (From S46)
#  ==>  Action= "Blank-Left", S54, g-value = 9, (From S50)
#  ==>  Action= "Blank-Up", S56, g-value = 10, (From S54)
#  ==>  Action= "Blank-Right", S59, g-value = 11, (From S56)
#  ==>  Action= "Blank-Down", S60, g-value = 12, (From S59)

# ----------------------------
# Search time = 0.015625, nodes expanded = 42, states generated = 63, states cycle check pruned = 21


print("======================================================")

print("===========Test 1, MEDIUM 2, ASTAR, h_misplacedTiles======")
se.search(s4, eightPuzzle_goal_fn, h_misplacedTiles)

# Master solution Results (edited)
# Search Successful! Solution cost = 12
# Solution Path:
# Action= "START", S61, g-value = 0, (Initial State)
#  ==>  Action= "Blank-Right", S2, g-value = 1, (From S61)
#  ==>  Action= "Blank-Up", S3, g-value = 2, (From S2)
#  ==>  Action= "Blank-Left", S9, g-value = 3, (From S3)
#  ==>  Action= "Blank-Up", S19, g-value = 4, (From S9)
#  ==>  Action= "Blank-Right", S39, g-value = 5, (From S19)
#  ==>  Action= "Blank-Right", S61, g-value = 6, (From S39)
#  ==>  Action= "Blank-Down", S105, g-value = 7, (From S61)
#  ==>  Action= "Blank-Left", S109, g-value = 8, (From S105)
#  ==>  Action= "Blank-Left", S113, g-value = 9, (From S109)
#  ==>  Action= "Blank-Up", S162, g-value = 10, (From S113)
#  ==>  Action= "Blank-Right", S165, g-value = 11, (From S162)
#  ==>  Action= "Blank-Down", S166, g-value = 12, (From S165)

# ----------------------------
# Search time = 0.015625, nodes expanded = 110, states generated = 169, states cycle check pruned = 59


print("======================================================")

# Hard
s5 = eightPuzzle("START", 0, [5, 6, 7, 4, 0, 8, 3, 2, 1])

print("===========Test 1, HARD, ASTAR, h_MHDist==============")
se.search(s5, eightPuzzle_goal_fn, h_MHDist)

# Master solution Results (edited)
# Search Successful! Solution cost = 30
# Solution Path:
# Action= "START", S169, g-value = 0, (Initial State)
#  ==>  Action= "Blank-Up", S2, g-value = 1, (From S169)
#  ==>  Action= "Blank-Right", S20, g-value = 2, (From S2)
#  ==>  Action= "Blank-Down", S22, g-value = 3, (From S20)
#  ==>  Action= "Blank-Down", S58, g-value = 4, (From S22)
#  ==>  Action= "Blank-Left", S62, g-value = 5, (From S58)
#  ==>  Action= "Blank-Left", S75, g-value = 6, (From S62)
#  ==>  Action= "Blank-Up", S137, g-value = 7, (From S75)
#  ==>  Action= "Blank-Up", S6263, g-value = 8, (From S137)
#  ==>  Action= "Blank-Right", S6266, g-value = 9, (From S6263)
#  ==>  Action= "Blank-Right", S6268, g-value = 10, (From S6266)
#  ==>  Action= "Blank-Down", S6270, g-value = 11, (From S6268)
#  ==>  Action= "Blank-Down", S6272, g-value = 12, (From S6270)
#  ==>  Action= "Blank-Left", S6276, g-value = 13, (From S6272)
#  ==>  Action= "Blank-Left", S6279, g-value = 14, (From S6276)
#  ==>  Action= "Blank-Up", S6296, g-value = 15, (From S6279)
#  ==>  Action= "Blank-Up", S6299, g-value = 16, (From S6296)
#  ==>  Action= "Blank-Right", S6302, g-value = 17, (From S6299)
#  ==>  Action= "Blank-Right", S6304, g-value = 18, (From S6302)
#  ==>  Action= "Blank-Down", S6306, g-value = 19, (From S6304)
#  ==>  Action= "Blank-Down", S6308, g-value = 20, (From S6306)
#  ==>  Action= "Blank-Left", S6312, g-value = 21, (From S6308)
#  ==>  Action= "Blank-Left", S6315, g-value = 22, (From S6312)
#  ==>  Action= "Blank-Up", S6320, g-value = 23, (From S6315)
#  ==>  Action= "Blank-Up", S6323, g-value = 24, (From S6320)
#  ==>  Action= "Blank-Right", S6326, g-value = 25, (From S6323)
#  ==>  Action= "Blank-Right", S6328, g-value = 26, (From S6326)
#  ==>  Action= "Blank-Down", S6330, g-value = 27, (From S6328)
#  ==>  Action= "Blank-Down", S6332, g-value = 28, (From S6330)
#  ==>  Action= "Blank-Left", S6336, g-value = 29, (From S6332)
#  ==>  Action= "Blank-Up", S6337, g-value = 30, (From S6336)

# ----------------------------
# Search time = 0.265625, nodes expanded = 3769, states generated = 6340, states cycle check pruned = 2571
# ======================================================


print("======================================================")

print("===========Test 1, HARD, ASTAR, h_misplacedTiles======")
se.search(s5, eightPuzzle_goal_fn, h_misplacedTiles)

# Master solution Results (edited)
# Search Successful! Solution cost = 30
# Solution Path:
# Action= "START", S169, g-value = 0, (Initial State)
#  ==>  Action= "Blank-Up", S2, g-value = 1, (From S169)
#  ==>  Action= "Blank-Right", S15, g-value = 2, (From S2)
#  ==>  Action= "Blank-Down", S21, g-value = 3, (From S15)
#  ==>  Action= "Blank-Down", S36, g-value = 4, (From S21)
#  ==>  Action= "Blank-Left", S100, g-value = 5, (From S36)
#  ==>  Action= "Blank-Left", S191, g-value = 6, (From S100)
#  ==>  Action= "Blank-Up", S305, g-value = 7, (From S191)
#  ==>  Action= "Blank-Up", S515, g-value = 8, (From S305)
#  ==>  Action= "Blank-Right", S890, g-value = 9, (From S515)
#  ==>  Action= "Blank-Right", S1570, g-value = 10, (From S890)
#  ==>  Action= "Blank-Down", S2836, g-value = 11, (From S1570)
#  ==>  Action= "Blank-Down", S4515, g-value = 12, (From S2836)
#  ==>  Action= "Blank-Left", S6288, g-value = 13, (From S4515)
#  ==>  Action= "Blank-Left", S9636, g-value = 14, (From S6288)
#  ==>  Action= "Blank-Up", S15602, g-value = 15, (From S9636)
#  ==>  Action= "Blank-Up", S25286, g-value = 16, (From S15602)
#  ==>  Action= "Blank-Right", S45957, g-value = 17, (From S25286)
#  ==>  Action= "Blank-Right", S68645, g-value = 18, (From S45957)
#  ==>  Action= "Blank-Down", S104765, g-value = 19, (From S68645)
#  ==>  Action= "Blank-Down", S149740, g-value = 20, (From S104765)
#  ==>  Action= "Blank-Left", S205195, g-value = 21, (From S149740)
#  ==>  Action= "Blank-Left", S271742, g-value = 22, (From S205195)
#  ==>  Action= "Blank-Up", S321613, g-value = 23, (From S271742)
#  ==>  Action= "Blank-Up", S321616, g-value = 24, (From S321613)
#  ==>  Action= "Blank-Right", S321619, g-value = 25, (From S321616)
#  ==>  Action= "Blank-Right", S321621, g-value = 26, (From S321619)
#  ==>  Action= "Blank-Down", S321623, g-value = 27, (From S321621)
#  ==>  Action= "Blank-Down", S321625, g-value = 28, (From S321623)
#  ==>  Action= "Blank-Left", S321629, g-value = 29, (From S321625)
#  ==>  Action= "Blank-Up", S321630, g-value = 30, (From S321629)

# ----------------------------
# Search time = 7.125, nodes expanded = 145727, states generated = 321633, states cycle check pruned = 176270
# ======================================================

print("======================================================")

# Test Group 2
eightPuzzle_set_goal([1, 2, 3, 4, 5, 6, 7, 8, 0])
se.set_strategy('astar')

# Hard
s9 = eightPuzzle("START", 0, [3, 6, 0, 5, 7, 8, 2, 1, 4])

print("===========Test 2, HARD, ASTAR, h_MHDist======")
se.search(s9, eightPuzzle_goal_fn, h_MHDist)

# Master solution Results (edited)
# Search Successful! Solution cost = 20
# Solution Path:
# Action= "START", S144, g-value = 0, (Initial State)
#  ==>  Action= "Blank-Left", S2, g-value = 1, (From S144)
#  ==>  Action= "Blank-Left", S5, g-value = 2, (From S2)
#  ==>  Action= "Blank-Down", S6, g-value = 3, (From S5)
#  ==>  Action= "Blank-Down", S8, g-value = 4, (From S6)
#  ==>  Action= "Blank-Right", S12, g-value = 5, (From S8)
#  ==>  Action= "Blank-Right", S14, g-value = 6, (From S12)
#  ==>  Action= "Blank-Up", S88, g-value = 7, (From S14)
#  ==>  Action= "Blank-Up", S91, g-value = 8, (From S88)
#  ==>  Action= "Blank-Left", S94, g-value = 9, (From S91)
#  ==>  Action= "Blank-Left", S97, g-value = 10, (From S94)
#  ==>  Action= "Blank-Down", S98, g-value = 11, (From S97)
#  ==>  Action= "Blank-Down", S100, g-value = 12, (From S98)
#  ==>  Action= "Blank-Right", S104, g-value = 13, (From S100)
#  ==>  Action= "Blank-Up", S105, g-value = 14, (From S104)
#  ==>  Action= "Blank-Up", S109, g-value = 15, (From S105)
#  ==>  Action= "Blank-Left", S114, g-value = 16, (From S109)
#  ==>  Action= "Blank-Down", S115, g-value = 17, (From S114)
#  ==>  Action= "Blank-Down", S117, g-value = 18, (From S115)
#  ==>  Action= "Blank-Right", S121, g-value = 19, (From S117)
#  ==>  Action= "Blank-Right", S123, g-value = 20, (From S121)

# ----------------------------
# Search time = 0.078125, nodes expanded = 79, states generated = 125, states cycle check pruned = 46
# ======================================================


print("======================================================")

print("===========Test 2, HARD, ASTAR, h_misplacedTiles======")
se.search(s9, eightPuzzle_goal_fn, h_misplacedTiles)

# Master solution Results (edited)
# Search Successful! Solution cost = 20
# Solution Path:
# Action= "START", S144, g-value = 0, (Initial State)
#  ==>  Action= "Blank-Left", S2, g-value = 1, (From S144)
#  ==>  Action= "Blank-Left", S8, g-value = 2, (From S2)
#  ==>  Action= "Blank-Down", S18, g-value = 3, (From S8)
#  ==>  Action= "Blank-Down", S41, g-value = 4, (From S18)
#  ==>  Action= "Blank-Right", S81, g-value = 5, (From S41)
#  ==>  Action= "Blank-Right", S159, g-value = 6, (From S81)
#  ==>  Action= "Blank-Up", S312, g-value = 7, (From S159)
#  ==>  Action= "Blank-Up", S401, g-value = 8, (From S312)
#  ==>  Action= "Blank-Left", S404, g-value = 9, (From S401)
#  ==>  Action= "Blank-Left", S407, g-value = 10, (From S404)
#  ==>  Action= "Blank-Down", S577, g-value = 11, (From S407)
#  ==>  Action= "Blank-Down", S1030, g-value = 12, (From S577)
#  ==>  Action= "Blank-Right", S1680, g-value = 13, (From S1030)
#  ==>  Action= "Blank-Up", S3024, g-value = 14, (From S1680)
#  ==>  Action= "Blank-Up", S4942, g-value = 15, (From S3024)
#  ==>  Action= "Blank-Left", S4947, g-value = 16, (From S4942)
#  ==>  Action= "Blank-Down", S4948, g-value = 17, (From S4947)
#  ==>  Action= "Blank-Down", S4950, g-value = 18, (From S4948)
#  ==>  Action= "Blank-Right", S4954, g-value = 19, (From S4950)
#  ==>  Action= "Blank-Right", S4956, g-value = 20, (From S4954)

# ----------------------------
# Search time = 0.171875, nodes expanded = 2957, states generated = 4958, states cycle check pruned = 2001
# ======================================================


print("======================================================")
