from enum import Enum, auto

class BinaryResult(Enum):
  MOVE_LEFT = auto()
  OK = auto()
  MOVE_RIGHT = auto()

class EqualityConditional:
  def __init__(self, condition_value):
    self.equal_to = condition_value

  def check(self, checked_value):
    if checked_value < self.equal_to:
      return BinaryResult.MOVE_RIGHT
    elif checked_value == self.equal_to:
      return BinaryResult.OK
    elif checked_value > self.equal_to:
      return BinaryResult.MOVE_LEFT

class LimiterConditional:
  def __init__(self, sum_limiter):
    self.limiter = sum_limiter

  def check(self, current_upper_bound):
    nth_sum = self._calculate_nth_sum_of_progression(current_upper_bound)
    n_plus_1st_sum = self._calculate_nth_sum_of_progression(current_upper_bound + 1)

    if nth_sum < self.limiter and n_plus_1st_sum < self.limiter:
      return BinaryResult.MOVE_RIGHT
    elif nth_sum <= self.limiter and n_plus_1st_sum > self.limiter:
      return BinaryResult.OK
    elif nth_sum > self.limiter:
      return BinaryResult.MOVE_LEFT
    elif n_plus_1st_sum == self.limiter:
      return BinaryResult.MOVE_RIGHT

  def _calculate_nth_sum_of_progression(self, element_count):
    last_element = element_count
    first_element = 1
    sum_of_progression = element_count * ((first_element + last_element) // 2)
    if (first_element + last_element) % 2 != 0:
      sum_of_progression += (first_element + last_element) // 2

    return sum_of_progression