Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
--------------------------------------------
- For example, Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
  - Return: ["AAAAACCCCC", "CCCCCAAAAA"].

Solution (Time = O(n)) 
--------------------------------------------
- Use a dictionary, walk through the 'text' and try to add each 10-digit word to the dictionary (O(10n) is the time complexity assuming dictionary is O(1))
- If the word already occurs in the dicitonary, we've found a duplicate, just maintain a list of such words in a list (output_list)
- Once we reach the end of the 'text', output_list has the answer
