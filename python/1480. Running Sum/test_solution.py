from solution import Solution as sol

def test_solution():
  nums = [1,2,3,4]
  assert [1,3,6,10] == sol.runningSum(sol, nums)

  nums = [1,1,1,1,1]
  assert [1,2,3,4,5] == sol.runningSum(sol, nums)

  nums = [3, 1, 2, 10, 1]
  assert [3,4,6,16,17] == sol.runningSum(sol, nums)
