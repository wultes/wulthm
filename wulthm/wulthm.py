import time
import random
import inspect

class WulthModel:
    def heapify(self, nums: list, heap_size: int, root_index: int):
        """
        Additional support function for heap_sort

        Keyword arguments:
        - nums <list> - List of numbers
        - heap_size <int> - Len list if numbers
        - root_index <int> - Index number in list of numbers
        """
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        # If the left_child of the root is a valid index and the element is greater 
        # than the current largest, update the largest element
        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        #Same for the right_child
        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child
        
        # If the largest element is no longer the root, they are swapped
        if largest != root_index:
            nums[root_index], nums[largest] = nums[largest], nums[root_index]
            self.heapify(nums, heap_size, largest)

    def merge(self, left_list: list, right_list: list):
        """
        Additional support function for merge_sort

        Keyword arguments:
        - left_list <list> - Left part of list for sorting
        - right_list <list> - Right part of list for sorting
        """
        sorted_list = []
        left_list_index = right_list_index = 0
        left_list_length, right_list_length = len(left_list), len(right_list)

        for _ in range(left_list_length + right_list_length):
            # Compare the first elements at the beginning of each list
            # If the first element of the left sublist is less than, add it
            # into a sorted array
            if left_list_index < left_list_length and right_list_index < right_list_length:
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1

                # If the first element of the right sublist is less than, add it
                # into a sorted array
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1

            # If the end of the left list is reached, the elements of the right list
            # add to sorted array
            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
            
            # If the end of the left list is reached, the elements of the right list
            # add to sorted array
            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

        return sorted_list

    def bubble_sort(self, nums: list):
        """
        Bubble Sort function

        Bubble Sort is the simplest sorting algorithm that works by 
        repeatedly swapping the adjacent elements if they are in the 
        wrong order
        
        This algorithm is not suitable for large data sets as its average 
        and worst case time complexity is quite high

        Keyword arguments:
        - nums <list> - List of numbers for sort

        """
        # Set swapped to True so the loop will run at least once
        swapped = True
        while swapped:
            swapped = False
            for index in range(len(nums)-1):
                if nums[index] > nums[index+1]:
                    # Change elements
                    nums[index], nums[index+1] = nums[index+1], nums[index]
                    # Set swapped to True for the next iteration
                    swapped = True

        return nums
    
    def selection_sort(self, nums: list):
        """
        Selection Sort function

        The selection sort algorithm sorts an array by repeatedly finding 
        the minimum element (considering ascending order) from unsorted part 
        and putting it at the beginning. The algorithm maintains two subarrays 
        in a given array

        1) The subarray which is already sorted

        2) Remaining subarray which is unsorted. In every iteration of selection sort, 
        the minimum element (considering ascending order) from the unsorted subarray 
        is picked and moved to the sorted subarray

        Keyword arguments:
        - nums <list> - List of numbers for sort
        
        """
        for index in range(len(nums)):
            # Initially, we consider the first element to be the smallest
            min_index = index
            # Reassembly of unsorted elements
            for sub_index in range(index + 1, len(nums)):
                if nums[sub_index] < nums[min_index]:
                    min_index = sub_index
            
            #Minimal element change with first element
            nums[index], nums[min_index] = nums[min_index], nums[index]
        
        return nums
    
    def insertion_sort(self, nums: list):
        """
        Insertion Sort function

        Insertion sort is a simple sorting algorithm that works similar to the way you sort 
        playing cards in your hands

        The array is virtually split into a sorted and an unsorted part

        Values from the unsorted part are picked and placed at the correct 
        position in the sorted part

        Keyword arguments:
        - nums <list> - List of numbers for sort
        
        """
        # We start sorting from the second element, 
        # because the first element is considered to be already sorted
        for index in range(1 , len(nums)):
            item_to_insert = nums[index]
            sub_index = index - 1
            # Elements of the sorted segment are moved forward 
            # if they are larger than the element to be inserted
            while sub_index >= 0 and nums[sub_index] > item_to_insert:
                nums[sub_index+1] = nums[sub_index]
                sub_index -= 1
            # Insert element
            nums[sub_index+1] = item_to_insert
        
        return nums

    def heap_sort(self, nums: list):
        """
        Heap Sort function

        A comparison based sorting technique based on a Binary Heap data structure 
        
        It is similar to selection sort where we first find the maximum element and 
        place the maximum element at the end. We repeat the same process for the remaining element

        Keyword arguments:
        - nums <list> - List of numbers for sort

        Additional functions:
        - heapify
        """
        nums_len = len(nums)
        for index in range(nums_len, -1, -1):
            self.heapify(nums, nums_len, index)

        for index in range(nums_len - 1, 0, -1):
            nums[index], nums[0] = nums[0], nums[index]
            self.heapify(nums, index, 0)
        
        return nums

    def merge_sort(self, nums: list):
        """
        Merge Sort function

        Merge Sort is a Divide and Conquer algorithm
        
        It divides input array in two halves, 
        calls itself for the two halves and then merges the two sorted halves
        
        The merge() function is used for merging two halves

        Keyword arguments:
        - nums <list> - List of numbers for sort

        Additional functions:
        - merge
        """
        if len(nums) <= 1:
            return nums
        
        # To find the middle of the list, use division without a remainder
        # Indexes must be integer
        mid = len(nums) // 2

        left_list = self.merge_sort(nums[:mid])
        right_list = self.merge_sort(nums[mid:])

        return self.merge(left_list, right_list)

    
    def get_source_code(self, function_name: str):
        """
        For get source code of function
        
        Keyword arguments:
        - function_name <str> - Name of function

        """
        func = self.__getattribute__(function_name)

        print(inspect.getsource(func))
    
    def get_doc(self, function_name: str):
        """
        For get documentation of function
        
        Keyword arguments:
        - function_name <str> - Name of function

        """
        func = self.__getattribute__(function_name)

        print(inspect.getdoc(func))
    
    def get_functions(self):
        """
        For get list of functions
        
        """
        functions = inspect.getmembers(self, predicate=inspect.ismethod)
        for func in functions:
            print(func[0])


    def test_sort_function(self, function_name: str, max_degree: int):
        """
        For testing functions

        Testing shows:
            - Input Data
            - Output Data
            - Job time

        Keyword arguments:
        - function_name <str> - Name of function
        - max_degree <int> - Max degree for numbers in test lists
                           Usage: random.randint(0, 10 ** max_degree)

        Warning: You can use this function only for testing SORT functions by numbers

        """

        func = self.__getattribute__(function_name)        
        
        random_args = {
            "10 random numbers": [random.randint(0, 10 ** max_degree) for _ in range(10)],
            "100 random number": [random.randint(0, 10 ** max_degree) for _ in range(100)],
            "1000 random numbers": [random.randint(0, 10 ** max_degree) for _ in range(1000)]
        }

        for args in random_args:
            start_time = time.time()

            print(f"{args}")
            print(f"Input Data: {random_args[args]}")
            
            result = func(random_args[args])

            print(f"Output Data: {result}")

            end_time = time.time()
            time_delta = (end_time - start_time) * 1000 

            print(f"Job time: {time_delta}ms.")

wulthm = WulthModel()

