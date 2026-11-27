def insertion_sort(arr):
    """Sort a list in ascending order using Insertion Sort."""
    result = arr.copy()  # keep the original unsorted array untouched
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        # shift larger elements one position to the right
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


full_name = "Alexander Baron"

# Build the unsorted array:
# - exclude symbols/spaces (letters only)
# - discard duplicate letters (case-insensitive)
unsorted_array = []
for ch in full_name.upper():
    if ch.isalpha() and ch not in unsorted_array:
        unsorted_array.append(ch)

sorted_array = insertion_sort(unsorted_array)

print("Unsorted array:", unsorted_array)
print("Sorted array:  ", sorted_array)
