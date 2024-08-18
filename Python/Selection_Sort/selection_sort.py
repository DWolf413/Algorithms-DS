class SelectionSort():
    def find_smallest(self, arr):

        # Store the smallest value
        smallest = arr[0]
        # Stores de index of the smallest value
        smallest_index = 0


        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i

        return smallest_index

    def selection_sort_book(self, arr):

        newArr = []

        # Copy array before mutating
        copiedArr = list(arr)

        for i in range(len(copiedArr)):
            smallest = self.find_smallest(copiedArr)
            newArr.append(copiedArr.pop(smallest))

        return newArr

if __name__ == "__main__":

    print("Comienzo desde main")
    ss = SelectionSort()
    my_list = [5,3,6,2,10]

    print(ss.selection_sort_book(my_list))