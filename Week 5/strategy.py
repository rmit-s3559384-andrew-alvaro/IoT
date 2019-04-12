# Reference: https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_strategy.htm
# Adopted for learning pursposes only.
import types

class StrategyExample:
   def __init__(self, func = None):
      self.name = "Strategy Example 0"
      self.execute = func

   def go(self):
      if(self.execute is not None):
         self.execute(self)
      else:
         print(self.name)

def execute_replacement1(self):
   print(self.name + " from execute 1")

def execute_replacement2(self):
   print(self.name + " from execute 2")

if __name__ == "__main__":
   strategy0 = StrategyExample()

   strategy1 = StrategyExample(execute_replacement1)
   strategy1.name = "Strategy Example 1"

   strategy2 = StrategyExample(execute_replacement2)
   strategy2.name = "Strategy Example 2"

   strategy0.go()
   strategy1.go()
   strategy2.go()
