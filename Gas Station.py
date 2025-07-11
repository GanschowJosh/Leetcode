from typing import List

class Solution:
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    num_stations = len(gas)
    total_gas = 0
    curr_tank = 0
    valid = 0

    for i in range(num_stations):
      curr_gas = gas[i] - cost[i]
      curr_tank += curr_gas
      total_gas += curr_gas

      if curr_tank < 0:
        valid = i + 1
        curr_tank = 0

    return -1 if total_gas < 0 else valid


sol = Solution()
print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print(sol.canCompleteCircuit([2,3,4], [3,4,3]))
print(sol.canCompleteCircuit([1,1,1], [1,1,1]))