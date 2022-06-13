import time
import random
import inspect

class WulthModel:

    def bubble_sort(self, nums: list):
        """
        Bubble Sort function

        Bubble Sort is the simplest sorting algorithm that works by 
        repeatedly swapping the adjacent elements if they are in the 
        wrong order
        
        This algorithm is not suitable for large data sets as its average 
        and worst case time complexity is quite high

        Keyword arguments:
        nums <list> - List of numbers for sort

        """
        swapped = True
        while swapped:
            swapped = False
            for index in range(len(nums)-1):
                if nums[index] > nums[index+1]:
                    nums[index], nums[index+1] = nums[index+1], nums[index]
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
        nums <list> - List of numbers for sort
        
        """
        for index in range(len(nums)):
            min_index = index
            for sub_index in range(index + 1, len(nums)):
                if nums[sub_index] < nums[min_index]:
                    min_index = sub_index
            
            nums[index], nums[min_index] = nums[min_index], nums[index]
        
        return nums
    
    def insertion_sort(self, nums: list):
        """
        Insertion Sort function

        Insertion sort is a simple sorting algorithm that works similar to the way you sort 
        playing cards in your hands

        The array is virtually split into a sorted and an unsorted part. Values from the unsorted 
        part are picked and placed at the correct position in the sorted part

        Keyword arguments:
        nums <list> - List of numbers for sort
        
        """
        for index in range(1 , len(nums)):
            item_to_insert = nums[index]
            sub_index = index - 1
            while sub_index >= 0 and nums[sub_index] > item_to_insert:
                nums[sub_index+1] = nums[sub_index]
                sub_index -= 1
            nums[sub_index+1] = item_to_insert
        
        return nums
    
    def get_source_code(self, function_name: str):
        """
        For get source code of function
        
        Keyword arguments:
        function_name <str> - Name of function

        """
        func = self.__getattribute__(function_name)

        print(inspect.getsource(func))
    
    def get_doc(self, function_name: str):
        """
        For get documentation of function
        
        Keyword arguments:
        function_name <str> - Name of function

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
        function_name <str> - Name of function
        max_degree <int> - Max degree for numbers in test lists
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

