# leetcode

* My leetcode DSA preparation notes and solved problems
* Namming example  python/0001-two-sum.py


[0001 two-sum](https://github.com/JalilTahirov/leetcode/blob/main/python/0001-two-sum.py)

```
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty dictionary to store seen numbers and their corresponding indices
        map = {}

        # Loop through each element in the list
        for i in range(len(nums)):
            x = nums[i]
            y = target - x

            # Check if the complement has already been seen in the list
            if x in map:
                # If yes, we've found a pair that adds up to the target
                return [i, map[x]]
            else:
                # If not, add the current number and its index to the dictionary
                map[y] = i


```

[0015 3 sum](https://github.com/JalilTahirov/leetcode/blob/main/python/0015-3sum.py)

[0143 reorder List](https://github.com/JalilTahirov/leetcode/blob/main/python/0143-reorder-list.py)

[0455-assign cookies](https://github.com/JalilTahirov/leetcode/blob/main/python/0455-assign-cookies.py)

[1984-minimum-difference-between-highest-and-lowest-of-k-scores](https://github.com/JalilTahirov/leetcode/blob/main/python/1984-minimum-difference-between-highest-and-lowest-of-k-scores.py)


[0680-valid polindrome](https://github.com/JalilTahirov/leetcode/blob/main/python/0680-valid-palindrome-ii.py)







