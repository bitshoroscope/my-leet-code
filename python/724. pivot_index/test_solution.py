from solution import Solution as sol

def test_middle():
  nums = [1, 7, 3, 6, 5, 6]
  res = 3
  assert sol.pivotIndex(sol, nums) == res

def test_no_sol():
  nums = [1,2,3]
  res = -1
  assert sol.pivotIndex(sol, nums) == res

def test_first():
  nums = [2,1,-1]
  res = 0
  assert sol.pivotIndex(sol, nums) == res
