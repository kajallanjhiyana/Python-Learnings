Question 1: enumerate (Two Sum style)

Given a list nums and a target, return the indices of the two numbers that add up to target. Assume exactly one solution exists.

python
nums = [2, 7, 11, 15], target = 9   # expected: [0, 1]

Constraints:

Use enumerate, not range(len(nums)).
Do it in one pass (O(n)), using a dictionary.

Follow-up: how would you print the results 1-indexed, without adding + 1 anywhere? (Hint: enumerate has a second argument.)

Question 2: zip (three parts)

(a) Predict the output (don’t run it first):

python
a = [1, 2, 3, 4]
b = ["x", "y", "z"]
z = zip(a, b)
print(list(z))
print(list(z))

Why does the second line print what it does?

(b) Without using range or indexing with i, write a function is_sorted(nums) that returns True if the list is sorted in ascending order. (Hint: pair each element with the one after it.)

(c) Given a matrix [[1, 2, 3], [4, 5, 6]], transpose it to [[1, 4], [2, 5], [3, 6]] using zip and the * unpacking operator.

Question 3: Word index map

Given a list of words, return a dictionary mapping each word to the list of indices where it appears.

python
words = ["a", "b", "a", "c", "b", "a"]
# expected: {"a": [0, 2, 5], "b": [1, 4], "c": [3]}

Constraints:

Use enumerate.
Do it in one pass.
Solve it twice: once with if key in dict and once with dict.setdefault or collections.defaultdict. Which do you prefer, and why?

Question 4: First unique character

Return the index of the first non-repeating character in a string, or -1 if there isn’t one.

python
"leetcode"      # 0
"loveleetcode"  # 2
"aabb"          # -1

Constraints:

Use enumerate in the final pass to return the index.
Aim for O(n) time.

Follow-up (a classic pitfall): what is wrong with this code, and why?

python
nums = [1, 2, 3, 4, 5, 6]
for i, n in enumerate(nums):
    if n % 2 == 0:
        nums.pop(i)
print(nums)

Predict the output before running it, then explain why it isn’t [1, 3, 5].

zip

Question 3: Longest common prefix

Given a list of strings, return their longest common prefix.

python
["flower", "flow", "flight"]  # "fl"
["dog", "racecar", "car"]     # ""

Constraints:

Use zip(*strs).
No nested index-based loops.
Think about what zip(*strs) does when the strings have different lengths, and why that helps you here.

Question 4: Leaderboard

You have two lists:

python
names  = ["Asha", "Ravi", "Meera", "Kabir"]
scores = [82, 95, 70, 95]

(a) Build a dictionary {name: score} using zip.

(b) Print the names sorted by score from highest to lowest, without using indices. If scores tie, sort alphabetically by name. (Hint: sorted accepts a key that can return a tuple, and you can negate numbers.)

(c) What happens if names has 4 items and scores has only 3? Show two ways to handle it:

itertools.zip_longest with a fillvalue
zip(..., strict=True) (Python 3.10+). When would you want this one?