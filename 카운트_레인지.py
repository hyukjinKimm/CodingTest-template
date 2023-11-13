# 값이 특정 범위에 속하는 데이터의 개수 구하기
from bisect import bisect_left, bisect_right


# left_value <= x <= right_value
def count_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index