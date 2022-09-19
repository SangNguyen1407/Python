from __future__ import annotations

from collections.abc import Iterator
from typing import Any

def merge_list(left_sublist, right_sublist):
	i,j = 0,0
	result = []

	while i < len(left_sublist) and j < len(right_sublist):
		if left_sublist[i] <= right_sublist[j]:
			result.append(left_sublist[i])
			i += 1
		else:
			result.append(right_sublist[j])
			j += 1

	if i < len(left_sublist):
		result += left_sublist[i:]

	if j < len(right_sublist):
		result += right_sublist[j:]

	return result


def merge_sort(input_list):
	#if list contains only 1 element return it
	if len(input_list) <= 1:
		return input_list
	else:
		midpoint = int(len(input_list)/2)
		left_sublist = merge_sort(input_list[:midpoint])
		right_sublist = merge_sort(input_list[midpoint:])
		return merge_list(left_sublist, right_sublist)

#test run
if __name__ == "__main__":
	number_list = [3,1,5,3,2,5,8,2,9,6,12,53,75,22,83,123,12123]
	print (merge_sort(number_list))