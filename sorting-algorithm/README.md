# Assessment 3.7: Sorting Algorithms

Sorts the letters of the full name **Alexander Baron** using **Insertion Sort**.

## Algorithm

1. Start with the full name "Alexander Baron".
2. Convert it to uppercase so "A" and "a" count as the same letter.
3. Create an empty list called `unsorted_array`.
4. For each character in the name: if it is a letter and is not already in the list, add it. Spaces and symbols are skipped, and duplicate letters are discarded.
5. Copy `unsorted_array` into a new list, `sorted_array`.
6. Insertion Sort: starting at the second element, take the current element (the key). Compare it with the elements to its left, shifting each larger one one position to the right. Insert the key into the gap.
7. Repeat step 6 until the last element is processed.
8. Display both `unsorted_array` and `sorted_array`.

## Output

```
Unsorted array: ['A', 'L', 'E', 'X', 'N', 'D', 'R', 'B', 'O']
Sorted array:   ['A', 'B', 'D', 'E', 'L', 'N', 'O', 'R', 'X']
```

## Run

```
python main.py
```
