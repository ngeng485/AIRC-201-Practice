def hello_name(name: str) -> str:
    """
    Returns a greeting string "Hello, {name}!"
    """
    return f"Hello, {name}!"

def calculate_area(length: float, width: float) -> float:
    """
    Returns the area of a rectangle given its length and width.
    """
    return length * width

def sum_to_n(n: int) -> int:
    """
    Returns the sum of all integers from 1 to n (inclusive).
    """
    return n * (n + 1) // 2

def list_sum(numbers: list[int]) -> int:
    """
    Returns the sum of all numbers in the given list.
    """
    return sum(numbers)

def filter_even(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the even numbers from the input list.
    """
    return [num for num in numbers if num % 2 == 0]

def count_vowels(text: str) -> int:
    """
    Returns the count of vowels (a, e, i, o, u) in the given text (case-insensitive).
    """
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def reverse_string(text: str) -> str:
    """
    Returns the reversed version of the input string.
    """
    return text[::-1]

def is_palindrome(text: str) -> bool:
    """
    Returns True if the input text is a palindrome, False otherwise.
    Ignores case and non-alphanumeric characters.
    """
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

def max_value(numbers: list[int]) -> int:
    """
    Returns the maximum value in the list without using the built-in max() function.
    """
    if not numbers:
        raise ValueError("List is empty")
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

def merge_dicts(d1: dict, d2: dict) -> dict:
    """
    Merges two dictionaries. Values from d2 overwrite d1 if keys overlap.
    Returns a new dictionary.
    """
    result = d1.copy()
    result.update(d2)
    return result

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    raise ValueError("No two sum solution")

def valid_parentheses(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

def max_subarray_sum(nums: list[int]) -> int:
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    """
    if not nums:
        return 0
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

def longest_substring_without_repeating(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    """
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    """
    anagram_map = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagram_map:
            anagram_map[sorted_s] = []
        anagram_map[sorted_s].append(s)
    return list(anagram_map.values())
