def selection_sort(number_list):
	for i in range(0, len(number_list)-1):
		min = i
		for min_pos in range(i+1, len(number_list)):
			if (number_list[min_pos] < number_list[min]):
				min = min_pos
		number_list[i],number_list[min] = number_list[min],number_list[i]
	return number_list


#test run
if __name__ == "__main__":
	number_list = [3,1,5,3,2,5,8,2,9,6,12,53,75,22,83,123,12123]
	print (selection_sort(number_list))