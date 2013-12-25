from bicycle import * 

map15_uniform = [
    ['loc0', 'loc1', 'loc2', 'loc3', 'loc4', 'loc5', 'loc6',
     'loc7', 'loc8', 'loc9', 'loc10', 'loc11', 'loc12', 
     'loc13', 'loc14'],
     [['loc0', 'loc1', 30], ['loc0', 'loc2', 30], ['loc0', 'loc3', 30],
      ['loc0', 'loc4', 30], ['loc0', 'loc5', 30], ['loc0', 'loc6', 30],
      ['loc0', 'loc7', 30], ['loc0', 'loc8', 30], ['loc0', 'loc9', 30],
      ['loc0', 'loc10', 30], ['loc0', 'loc11', 30], ['loc0', 'loc12', 30],
      ['loc0', 'loc13', 30], ['loc0', 'loc14', 30], ['loc1', 'loc2', 30],
      ['loc1', 'loc3', 30], ['loc1', 'loc4', 30], ['loc1', 'loc5', 30],
      ['loc1', 'loc6', 30], ['loc1', 'loc7', 30], ['loc1', 'loc8', 30],
      ['loc1', 'loc9', 30], ['loc1', 'loc10', 30], ['loc1', 'loc11', 30],
      ['loc1', 'loc12', 30], ['loc1', 'loc13', 30], ['loc1', 'loc14', 30],
      ['loc2', 'loc3', 30], ['loc2', 'loc4', 30], ['loc2', 'loc5', 30],
      ['loc2', 'loc6', 30], ['loc2', 'loc7', 30], ['loc2', 'loc8', 30],
      ['loc2', 'loc9', 30], ['loc2', 'loc10', 30], ['loc2', 'loc11', 30],
      ['loc2', 'loc12', 30], ['loc2', 'loc13', 30], ['loc2', 'loc14', 30],
      ['loc3', 'loc4', 30], ['loc3', 'loc5', 30], ['loc3', 'loc6', 30],
      ['loc3', 'loc7', 30], ['loc3', 'loc8', 30], ['loc3', 'loc9', 30],
      ['loc3', 'loc10', 30], ['loc3', 'loc11', 30], ['loc3', 'loc12', 30],
      ['loc3', 'loc13', 30], ['loc3', 'loc14', 30], ['loc4', 'loc5', 30],
      ['loc4', 'loc6', 30], ['loc4', 'loc7', 30], ['loc4', 'loc8', 30],
      ['loc4', 'loc9', 30], ['loc4', 'loc10', 30], ['loc4', 'loc11', 30],
      ['loc4', 'loc12', 30], ['loc4', 'loc13', 30], ['loc4', 'loc14', 30],
      ['loc5', 'loc6', 30], ['loc5', 'loc7', 30], ['loc5', 'loc8', 30],
      ['loc5', 'loc9', 30], ['loc5', 'loc10', 30], ['loc5', 'loc11', 30],
      ['loc5', 'loc12', 30], ['loc5', 'loc13', 30], ['loc5', 'loc14', 30],
      ['loc6', 'loc7', 30], ['loc6', 'loc8', 30], ['loc6', 'loc9', 30],
      ['loc6', 'loc10', 30], ['loc6', 'loc11', 30], ['loc6', 'loc12', 30],
      ['loc6', 'loc13', 30], ['loc6', 'loc14', 30], ['loc7', 'loc8', 30],
      ['loc7', 'loc9', 30], ['loc7', 'loc10', 30], ['loc7', 'loc11', 30],
      ['loc7', 'loc12', 30], ['loc7', 'loc13', 30], ['loc7', 'loc14', 30],
      ['loc8', 'loc9', 30], ['loc8', 'loc10', 30], ['loc8', 'loc11', 30],
      ['loc8', 'loc12', 30], ['loc8', 'loc13', 30], ['loc8', 'loc14', 30],
      ['loc9', 'loc10', 30], ['loc9', 'loc11', 30], ['loc9', 'loc12', 30],
      ['loc9', 'loc13', 30], ['loc9', 'loc14', 30], ['loc10', 'loc11', 30],
      ['loc10', 'loc12', 30], ['loc10', 'loc13', 30], ['loc10', 'loc14', 30],
      ['loc11', 'loc12', 30], ['loc11', 'loc13', 30], ['loc11', 'loc14', 30],
      ['loc12', 'loc13', 30], ['loc12', 'loc14', 30], ['loc13', 'loc14', 30]]]

jobs5 = [['Job0', 'loc2', 12.00, 'loc11', [13.00, 30]],
         ['Job1', 'loc3', 11.00, 'loc14', [12.00, 30]],
         ['Job2', 'loc12', 10.00, 'loc8', [11.00, 30]],
         ['Job3', 'loc10', 9.00, 'loc7', [10.00, 30]],
         ['Job4', 'loc14', 8.00, 'loc6', [9.00, 30]],
         ['Job5', 'loc10', 7.00, 'loc8', [8.00, 30]]]


jobs5a = [['Job0', 'loc2', 7.00, 'loc11', [7.15, 30], [7.30, 15]],
          ['Job1', 'loc3', 7.15, 'loc14', [7.30, 60], [7.45, 30]],
          ['Job2', 'loc12', 7.45, 'loc8', [8.00, 120], [8.15, 60]],
          ['Job3', 'loc10', 8.00, 'loc7', [8.15, 240], [8.30, 120]],
          ['Job4', 'loc14', 8.15, 'loc6', [8.30, 480], [8.45, 240]],
          ['Job5', 'loc10', 8.30, 'loc8', [8.45, 960], [9.00, 480]]]


jobs5b = [['Job0', 'loc2', 7.00, 'loc11', [7.15, 30], [7.30, 15]],
          ['Job1', 'loc3', 7.15, 'loc14', [7.30, 60], [7.45, 30]],
          ['Job2', 'loc12', 7.45, 'loc8', [8.00, 120], [8.15, 60]],
          ['Job3', 'loc10', 8.00, 'loc7', [8.15, 240], [8.30, 120]],
          ['Job4', 'loc14', 8.15, 'loc6', [8.30, 480], [8.45, 240]],
          ['Job5', 'loc10', 8.30, 'loc8', [8.45, 960], [9.00, 480]]]

jobs2 = [['Job0', 'loc2', 7.00, 'loc11', [7.30, 60]],
         ['Job1', 'loc3', 7.00, 'loc14', [7.30, 120]]]

jobsimpos =[['Job0', 'loc2', 7.00, 'loc11', [7.30, 60]],
           ['Job1', 'loc3', 7.00, 'loc14', [7.30, 120]],
           ['Job2', 'loc6', 18.45, 'loc7', [19.00, 300]]]
map2parts = [
    ['loc0', 'loc1', 'loc2', 'loc3', 'loc4', 'loc5'],
    [['loc0', 'loc1', 10], ['loc0', 'loc2', 10], ['loc0', 'loc3', 240],
     ['loc0', 'loc4', 240], ['loc0', 'loc5', 240], ['loc1', 'loc2', 10],
     ['loc1', 'loc3', 240], ['loc1', 'loc4', 240], ['loc1', 'loc5', 240],
     ['loc2', 'loc3', 240], ['loc2', 'loc4', 240], ['loc2', 'loc5', 240],
     ['loc3', 'loc4', 10], ['loc3', 'loc5', 10], ['loc4', 'loc5', 10]]]

jobs4 = [['Job0', 'loc0', 7.00, 'loc1', [7.15, 30], [7.30, 15]],
         ['Job1', 'loc1', 7.15, 'loc2', [7.30, 30], [7.45, 15]],
         ['Job2', 'loc3', 7.00, 'loc4', [7.15, 60], [7.30, 5]],
         ['Job3', 'loc4', 7.15, 'loc3', [7.30, 60], [7.45, 5]]]


randm = [['loc0', 'loc1', 'loc2', 'loc3', 'loc4', 'loc5', 'loc6', 'loc7', 'loc8', 'loc9', 'loc10', 'loc11', 'loc12', 'loc13', 'loc14', 'loc15', 'loc16', 'loc17', 'loc18', 'loc19', 'loc20', 'loc21', 'loc22', 'loc23', 'loc24'], [['loc0', 'loc1', 39], ['loc0', 'loc2', 26], ['loc0', 'loc3', 25], ['loc0', 'loc4', 36], ['loc0', 'loc5', 32], ['loc0', 'loc6', 46], ['loc0', 'loc7', 28], ['loc0', 'loc8', 8], ['loc0', 'loc9', 25], ['loc0', 'loc10', 32], ['loc0', 'loc11', 31], ['loc0', 'loc12', 24], ['loc0', 'loc13', 46], ['loc0', 'loc14', 28], ['loc0', 'loc15', 9], ['loc0', 'loc16', 28], ['loc0', 'loc17', 12], ['loc0', 'loc18', 15], ['loc0', 'loc19', 13], ['loc0', 'loc20', 26], ['loc0', 'loc21', 39], ['loc0', 'loc22', 4], ['loc0', 'loc23', 34], ['loc0', 'loc24', 42], ['loc1', 'loc2', 42], ['loc1', 'loc3', 18], ['loc1', 'loc4', 11], ['loc1', 'loc5', 21], ['loc1', 'loc6', 7], ['loc1', 'loc7', 21], ['loc1', 'loc8', 37], ['loc1', 'loc9', 14], ['loc1', 'loc10', 12], ['loc1', 'loc11', 15], ['loc1', 'loc12', 43], ['loc1', 'loc13', 19], ['loc1', 'loc14', 21], ['loc1', 'loc15', 44], ['loc1', 'loc16', 17], ['loc1', 'loc17', 45], ['loc1', 'loc18', 27], ['loc1', 'loc19', 44], ['loc1', 'loc20', 27], ['loc1', 'loc21', 2], ['loc1', 'loc22', 34], ['loc1', 'loc23', 13], ['loc1', 'loc24', 8], ['loc2', 'loc3', 24], ['loc2', 'loc4', 33], ['loc2', 'loc5', 24], ['loc2', 'loc6', 48], ['loc2', 'loc7', 44], ['loc2', 'loc8', 33], ['loc2', 'loc9', 34], ['loc2', 'loc10', 44], ['loc2', 'loc11', 28], ['loc2', 'loc12', 3], ['loc2', 'loc13', 38], ['loc2', 'loc14', 22], ['loc2', 'loc15', 20], ['loc2', 'loc16', 26], ['loc2', 'loc17', 18], ['loc2', 'loc18', 34], ['loc2', 'loc19', 16], ['loc2', 'loc20', 46], ['loc2', 'loc21', 41], ['loc2', 'loc22', 25], ['loc2', 'loc23', 46], ['loc2', 'loc24', 49], ['loc3', 'loc4', 11], ['loc3', 'loc5', 8], ['loc3', 'loc6', 25], ['loc3', 'loc7', 25], ['loc3', 'loc8', 27], ['loc3', 'loc9', 12], ['loc3', 'loc10', 21], ['loc3', 'loc11', 6], ['loc3', 'loc12', 25], ['loc3', 'loc13', 21], ['loc3', 'loc14', 4], ['loc3', 'loc15', 28], ['loc3', 'loc16', 3], ['loc3', 'loc17', 28], ['loc3', 'loc18', 21], ['loc3', 'loc19', 27], ['loc3', 'loc20', 29], ['loc3', 'loc21', 18], ['loc3', 'loc22', 21], ['loc3', 'loc23', 23], ['loc3', 'loc24', 25], ['loc4', 'loc5', 10], ['loc4', 'loc6', 15], ['loc4', 'loc7', 28], ['loc4', 'loc8', 37], ['loc4', 'loc9', 16], ['loc4', 'loc10', 20], ['loc4', 'loc11', 6], ['loc4', 'loc12', 35], ['loc4', 'loc13', 12], ['loc4', 'loc14', 11], ['loc4', 'loc15', 39], ['loc4', 'loc16', 9], ['loc4', 'loc17', 40], ['loc4', 'loc18', 28], ['loc4', 'loc19', 38], ['loc4', 'loc20', 33], ['loc4', 'loc21', 9], ['loc4', 'loc22', 32], ['loc4', 'loc23', 22], ['loc4', 'loc24', 19], ['loc5', 'loc6', 26], ['loc5', 'loc7', 33], ['loc5', 'loc8', 35], ['loc5', 'loc9', 20], ['loc5', 'loc10', 27], ['loc5', 'loc11', 6], ['loc5', 'loc12', 26], ['loc5', 'loc13', 15], ['loc5', 'loc14', 4], ['loc5', 'loc15', 33], ['loc5', 'loc16', 7], ['loc5', 'loc17', 33], ['loc5', 'loc18', 29], ['loc5', 'loc19', 31], ['loc5', 'loc20', 37], ['loc5', 'loc21', 19], ['loc5', 'loc22', 29], ['loc5', 'loc23', 29], ['loc5', 'loc24', 29], ['loc6', 'loc7', 27], ['loc6', 'loc8', 44], ['loc6', 'loc9', 21], ['loc6', 'loc10', 18], ['loc6', 'loc11', 21], ['loc6', 'loc12', 49], ['loc6', 'loc13', 19], ['loc6', 'loc14', 26], ['loc6', 'loc15', 51], ['loc6', 'loc16', 23], ['loc6', 'loc17', 52], ['loc6', 'loc18', 34], ['loc6', 'loc19', 51], ['loc6', 'loc20', 33], ['loc6', 'loc21', 7], ['loc6', 'loc22', 42], ['loc6', 'loc23', 18], ['loc6', 'loc24', 9], ['loc7', 'loc8', 22], ['loc7', 'loc9', 13], ['loc7', 'loc10', 9], ['loc7', 'loc11', 27], ['loc7', 'loc12', 44], ['loc7', 'loc13', 39], ['loc7', 'loc14', 29], ['loc7', 'loc15', 36], ['loc7', 'loc16', 26], ['loc7', 'loc17', 39], ['loc7', 'loc18', 13], ['loc7', 'loc19', 38], ['loc7', 'loc20', 5], ['loc7', 'loc21', 23], ['loc7', 'loc22', 24], ['loc7', 'loc23', 9], ['loc7', 'loc24', 19], ['loc8', 'loc9', 23], ['loc8', 'loc10', 29], ['loc8', 'loc11', 33], ['loc8', 'loc12', 31], ['loc8', 'loc13', 48], ['loc8', 'loc14', 31], ['loc8', 'loc15', 17], ['loc8', 'loc16', 30], ['loc8', 'loc17', 20], ['loc8', 'loc18', 10], ['loc8', 'loc19', 21], ['loc8', 'loc20', 20], ['loc8', 'loc21', 38], ['loc8', 'loc22', 8], ['loc8', 'loc23', 30], ['loc8', 'loc24', 39], ['loc9', 'loc10', 10], ['loc9', 'loc11', 14], ['loc9', 'loc12', 34], ['loc9', 'loc13', 27], ['loc9', 'loc14', 16], ['loc9', 'loc15', 31], ['loc9', 'loc16', 13], ['loc9', 'loc17', 33], ['loc9', 'loc18', 13], ['loc9', 'loc19', 32], ['loc9', 'loc20', 17], ['loc9', 'loc21', 15], ['loc9', 'loc22', 21], ['loc9', 'loc23', 12], ['loc9', 'loc24', 17], ['loc10', 'loc11', 21], ['loc10', 'loc12', 44], ['loc10', 'loc13', 31], ['loc10', 'loc14', 25], ['loc10', 'loc15', 40], ['loc10', 'loc16', 21], ['loc10', 'loc17', 42], ['loc10', 'loc18', 18], ['loc10', 'loc19', 41], ['loc10', 'loc20', 15], ['loc10', 'loc21', 14], ['loc10', 'loc22', 29], ['loc10', 'loc23', 2], ['loc10', 'loc24', 10], ['loc11', 'loc12', 29], ['loc11', 'loc13', 15], ['loc11', 'loc14', 6], ['loc11', 'loc15', 34], ['loc11', 'loc16', 3], ['loc11', 'loc17', 34], ['loc11', 'loc18', 25], ['loc11', 'loc19', 33], ['loc11', 'loc20', 32], ['loc11', 'loc21', 14], ['loc11', 'loc22', 27], ['loc11', 'loc23', 23], ['loc11', 'loc24', 23], ['loc12', 'loc13', 40], ['loc12', 'loc14', 23], ['loc12', 'loc15', 17], ['loc12', 'loc16', 27], ['loc12', 'loc17', 15], ['loc12', 'loc18', 33], ['loc12', 'loc19', 13], ['loc12', 'loc20', 45], ['loc12', 'loc21', 42], ['loc12', 'loc22', 24], ['loc12', 'loc23', 46], ['loc12', 'loc24', 50], ['loc13', 'loc14', 19], ['loc13', 'loc15', 48], ['loc13', 'loc16', 18], ['loc13', 'loc17', 48], ['loc13', 'loc18', 40], ['loc13', 'loc19', 47], ['loc13', 'loc20', 44], ['loc13', 'loc21', 17], ['loc13', 'loc22', 43], ['loc13', 'loc23', 32], ['loc13', 'loc24', 27], ['loc14', 'loc15', 29], ['loc14', 'loc16', 4], ['loc14', 'loc17', 29], ['loc14', 'loc18', 25], ['loc14', 'loc19', 28], ['loc14', 'loc20', 33], ['loc14', 'loc21', 19], ['loc14', 'loc22', 24], ['loc14', 'loc23', 27], ['loc14', 'loc24', 28], ['loc15', 'loc16', 31], ['loc15', 'loc17', 3], ['loc15', 'loc18', 23], ['loc15', 'loc19', 4], ['loc15', 'loc20', 35], ['loc15', 'loc21', 44], ['loc15', 'loc22', 12], ['loc15', 'loc23', 41], ['loc15', 'loc24', 48], ['loc16', 'loc17', 31], ['loc16', 'loc18', 23], ['loc16', 'loc19', 30], ['loc16', 'loc20', 30], ['loc16', 'loc21', 16], ['loc16', 'loc22', 24], ['loc16', 'loc23', 23], ['loc16', 'loc24', 24], ['loc17', 'loc18', 26], ['loc17', 'loc19', 2], ['loc17', 'loc20', 38], ['loc17', 'loc21', 45], ['loc17', 'loc22', 14], ['loc17', 'loc23', 43], ['loc17', 'loc24', 50], ['loc18', 'loc19', 26], ['loc18', 'loc20', 12], ['loc18', 'loc21', 28], ['loc18', 'loc22', 12], ['loc18', 'loc23', 19], ['loc18', 'loc24', 28], ['loc19', 'loc20', 38], ['loc19', 'loc21', 44], ['loc19', 'loc22', 15], ['loc19', 'loc23', 43], ['loc19', 'loc24', 49], ['loc20', 'loc21', 29], ['loc20', 'loc22', 24], ['loc20', 'loc23', 14], ['loc20', 'loc24', 24], ['loc21', 'loc22', 35], ['loc21', 'loc23', 16], ['loc21', 'loc24', 10], ['loc22', 'loc23', 30], ['loc22', 'loc24', 38], ['loc23', 'loc24', 10]]]

randjbs5 = [['Job0', 'loc22', 7.52, 'loc23', [7.57, 43], [8.31, 33]], ['Job1', 'loc8', 10.43, 'loc5', [11.56, 27], [12.05, 20], [12.15, 7]], ['Job2', 'loc22', 14.13, 'loc16', [15.41, 31], [17.35, 14]], ['Job3', 'loc13', 13.07, 'loc20', [13.32, 28], [15.11, 17], [16.12, 3]], ['Job4', 'loc6', 15.26, 'loc14', [16.17, 30], [16.35, 5]]]

randjbs10 = [['Job0', 'loc16', 10.22, 'loc19', [10.32, 29], [10.42, 11]], ['Job1', 'loc13', 8.4, 'loc2', [9.52, 27], [10.27, 2]], ['Job2', 'loc24', 9.32, 'loc7', [11.1, 42]], ['Job3', 'loc14', 10.09, 'loc8', [11.51, 31], [12.02, 7]], ['Job4', 'loc2', 11.26, 'loc3', [11.48, 45]], ['Job5', 'loc11', 9.28, 'loc0', [11.25, 32], [12.45, 17], [14.06, 9]], ['Job6', 'loc11', 12.16, 'loc1', [14.15, 33], [14.27, 28], [15.21, 12]], ['Job7', 'loc15', 9.2, 'loc13', [10.19, 32], [11.5, 8], [12.59, 3]], ['Job8', 'loc8', 12.31, 'loc21', [12.37, 25], [14.19, 5]], ['Job9', 'loc1', 8.33, 'loc23', [9.15, 25], [10.49, 7]]]

randjbs15 = [['Job0', 'loc7', 12.59, 'loc3', [14.44, 33], [15.14, 8]], ['Job1', 'loc12', 9.46, 'loc24', [9.55, 41]], ['Job2', 'loc15', 10.04, 'loc19', [10.14, 27], [11.41, 9]], ['Job3', 'loc12', 13.24, 'loc21', [14.55, 28], [16.35, 16], [17.44, 4]], ['Job4', 'loc23', 15.17, 'loc15', [15.27, 36], [16.33, 22], [17.16, 11]], ['Job5', 'loc8', 10.39, 'loc22', [11.55, 29]], ['Job6', 'loc16', 10.54, 'loc18', [11.42, 26], [13.13, 1]], ['Job7', 'loc16', 10.44, 'loc8', [12.27, 28], [12.51, 22], [12.56, 1]], ['Job8', 'loc12', 12.5, 'loc19', [14.0, 34]], ['Job9', 'loc15', 7.3, 'loc10', [8.58, 28], [9.37, 12]], ['Job10', 'loc5', 13.24, 'loc23', [14.03, 42], [15.16, 17]], ['Job11', 'loc2', 16.29, 'loc15', [17.16, 45], [18.23, 27], [18.43, 22]], ['Job12', 'loc8', 14.09, 'loc22', [15.22, 45]], ['Job13', 'loc21', 12.44, 'loc24', [13.36, 36], [14.25, 17]], ['Job14', 'loc11', 7.33, 'loc12', [8.3, 25], [10.15, 10], [11.17, 5]]]

s0 = make_start_state(map15_uniform, jobs5)
deliveries = solve(s0)
print "========================Deliveries:========================="
print deliveries
print "============================================================"

s0 = make_start_state(map15_uniform, jobs5a)
deliveries = solve(s0)
print "========================Deliveries:========================="
print deliveries
print "============================================================"

s0 = make_start_state(map15_uniform, jobs5b)
deliveries = solve(s0)
print "========================Deliveries:========================="
print deliveries
print "============================================================"

s0 = make_start_state(map15_uniform, jobs2)
deliveries = solve(s0)
print "========================Deliveries:========================="
print deliveries
print "============================================================"

s0 = make_start_state(map15_uniform, jobsimpos)
deliveries = solve(s0)
print "========================Deliveries:========================="
print deliveries
print "============================================================"

s0 = make_start_state(map2parts, jobs4)
deliveries = solve(s0)
print "========================Deliveries:========================="
print deliveries
print "============================================================"

s0 = make_start_state(randm, randjbs5)
deliveries = solve(s0)
print "========================Deliveries:========================="
print deliveries
print "============================================================"

s0 = make_start_state(randm, randjbs10)
deliveries = solve(s0)
print "========================Deliveries:========================="
print deliveries
print "============================================================"

s0 = make_start_state(randm, randjbs15)
deliveries = solve(s0)
print "========================Deliveries:========================="
print deliveries
print "============================================================"




