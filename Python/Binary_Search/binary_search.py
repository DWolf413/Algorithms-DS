class BinarySearch():

    def binary_search_book(self, arr, item):

        # Low and high keep tack of wich part of the list you'll search in
        low = 0
        high = len(arr)-1

        # While you haven't narrowed it down to one element
        while low <= high:

            # Check the middle element
            mid = (low + high)//2
            guess = arr[mid]

            # Found the item
            if guess == item:
                return mid

            # The guess was too high
            elif guess > item:
                high = mid-1

            # The guess was too low
            else:
                low = mid+1

        # The item doesn't exit
        return None


if __name__ == "__main__":
    # We must initialize the class to use the methods of this class

    print("Comienzo desde main")
    bs = BinarySearch()
    my_list = [1, 3, 5, 7, 9]

    print(bs.binary_search_book(my_list, 3))  # => 1

    # 'None' means nil in Python. We use to indicate that the item wasn't found.
    print(bs.binary_search_book(my_list, -1))  # => None