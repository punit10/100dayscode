# Day65 Design website that people like design a demo on canva and export as website.

class Solution:
    def __init__(self):
        pass
    def product_except_self(self, nums: list[int]) -> list[int]:
        answer = []
        for n in range(len(nums)):
            prod = 1
            for i in range(len(nums)):
                if i != n:
                    prod *=nums[i]
            answer.append(prod)
        return answer

    def pair_divisible_four(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] - nums[j]) % 4 == 0:
                    count += 1
        return count

s = Solution()
num = [1,2,3,4]
print(s.product_except_self(num))

num1 = [2, 6, 10]
num2 = [4, 10, 14, 8]
print(s.pair_divisible_four(num1))
print(s.pair_divisible_four(num2))


data = {
    "Rohit sharma": 250,
    "Virat Kohli": 300,
    "Ishan Kishan": 100,
    "Sanju": 109,
    "Abhishek": 108
}
def get_selected(data, limit):
    sorted_players = sorted(data.items(), key=lambda item: item[1])
    filtered_players = [item for item in sorted_players if item[1] < limit]
    max_score = 0
    player = ""
    print("sorted", sorted_players)
    print("Filtered", filtered_players[-1][0])

    players = {}
    for key, value in data.items():
        if value < limit:
            players[key] = value
    max_score = 0
    for value in players.values():
        if value > int(max_score):
            max_score = value
    for k,v in players.items():
        if v == max_score:
            player = k
    return player
print(get_selected(data, 200))

todo = {
    "square": lambda x: x * x,
    "cube": lambda x: x * x * x,
    "double": lambda x: x * 2,
    "noone": lambda x: x,
}

def do_operation(operation, value):
    return todo[operation](value)


# Return True if two strings are anagrams (same letters, same frequency).
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    for c in t:
        if c not in s:
            return False
    return True

n = 15
op = []
for i in range(1, n):
    if i % 3==0 and i%5 ==0 and i % 7 == 0:
        op.append(i)
    elif i % 3==0 and i%5 ==0:
        op.append(i)
    elif i % 3==0 and i % 7 == 0:
        op.append(i)
    elif i%5 ==0 and i % 7 == 0:
        op.append(i)
    elif i % 3==0:
        op.append(i)
print(sum(op))


# Given a sorted array of integers and a target,
# return the 1‑based indices of two numbers that sum to the target.
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers)-1
    res = None
    while left < right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            res = [left+1, right+1]
    return res


####################################################################
# Return the length of the longest substring with no repeating characters.
def length_of_longest_substring(s: str) -> int:
    seen = {}
    left = 0
    best = 0
    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = i
        best = max(best, i - left + 1)
    return best
print(length_of_longest_substring("division"))

s = "division"
for i, v in enumerate(s):
    if v in "aeiou":
        # print(i, v)
        pass
# print(list(enumerate(s)))
# print(dict(enumerate(s)))
print(tuple(enumerate(s)))

####################################################################
# Return an array where
# output[i] = product of all nums[j] except nums[i], without using division.
def product_except_self(nums: list[int]) -> list[int]:
    res = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i != j:
                prod *=nums[j]
        res.append(prod)
    return res

def compress(chars: list[str]) -> int:
    ans = ""
    i = 0
    j = 0
    count = 0
    if len(chars) == 1:
        return 1
    while j < len(chars):
        if chars[i] == chars[j]:
            count += 1
            j += 1
        else:
            if count > 1:
                ans += chars[i] + str(count)
                chars[i + 1] = str(count)
            else:
                ans += chars[i]
            i = j
            count = 0
    if count > 1:
        ans += chars[i] + str(count)
        chars[i + 1] = str(count)
    else:
        ans += chars[i]
    del chars[len(ans): ]
    print(chars)
    return len(ans)
chars = ["a","a","b","b","c","c","c"]
# print(compress(chars))
chars = ["a","b","c"]
# print(compress(chars))

# Normalize and deduplicate account IDs (trim + uppercase) from a list of strings.
ids = ["sjdiad", "  sjdas sdasd    ", "ssdsd", "rohan", " sdhsfdfhoi   ", " Rohan "]
def normalise(ids):
    res = []
    for i in range(len(ids)):
        ids[i] = ids[i].strip()
        ids[i] = ids[i].capitalize()
        if ids[i] not in res:
            res.append(ids[i])
    return res
print(normalise(ids))        

# Compute top-K merchants by total spend from a stream of (merchant, amount) transactions.
amounts = [("Raju", 2341), ("rohan", 5763), ("akash", 1453), ("Vaibhav", 4354), ("Ravi", 3322)]
amm = [{"name": "amazon", "amount": 303}, {"name": "flipkart", "amount": 202},
       {"name": "ajio", "amount": 404}]
k = 2
def top_k_merchants(amounts, k):
    sorted_amounts = sorted(amounts, key=lambda item: item[1])
    print(sorted_amounts)
    return sorted_amounts[-k:]


# merchants = []
    # res = []
    # for value in amounts:
    #     merchants.append(value[1])
    # merchants.sort()
    # print(merchants)
    # for i in merchants:
    #     for j in amounts:
    #         if i == j[1]:
    #             res.append(j)
    # print(res)
    # return res[len(res)-k:]

print(top_k_merchants(amounts, k))
nums = [10, 20, 30, 40, 50, 60, 70]
nums.sort()
res = []
print(nums)
for i in nums[-k:]:
    res.append(i)
print(res)

amount = [200, 3000, 4000, 1600, 800, 160]
s = [item * item for item in range(0, 10) if item % 2 == 0]
t = [(item, round(item * 0.18, 2)) for item in amount]
# print(s)
print(t)
# Group transaction reference IDs that are anagrams and return grouped lists.
ids = ["listen", "silent", "abc", "rat", "tar", "pqr", "atr"]
anagrams = []
for i in range(len(ids)):
    for j in range(i+1, len(ids)):
        if is_anagram(ids[i], ids[j]):
            anagrams.append((ids[i], ids[j]))
print(anagrams)

from collections import defaultdict
def group_anagrams(ids):
    # groups = defaultdict(list)
    groups = {}
    for word in ids:
        key = tuple(sorted(word))
        if groups.get(key) is None:
            groups[key] = [word]
        else:
            groups[key].append(word)
        print(key, groups[key])
    return list(groups.values())

ids = ["listen", "silent", "abc", "rat", "tar", "pqr", "atr"]
print(group_anagrams(ids))

# grouped  = [item for item in ids if is_anagram(item)]
# print(grouped)
#
# "Coding Question :
# I have a gym system design having member class for gym member and membership
# class write code improve the membership class and to run the test successfully
# only change membership class
# Member class has id ,name and membership status
# Membership status can be bronze(free)
# Silver and gold(paid)
# Correct the get membership average method in membership class to run the test
# successfully to return overall average of membership status to paid membership
# Solution hint: add an OR condition for Gold status along with silver because both
# are paid status,
#
#
# In he above code add workout class having workoutid , start time , end time ,
# duration (end - starttime)
# Each member can have multiple workouts
# Now we need to find
# 1. Add member method to add workouts to each member of gym and run test successfully
# 2.the average work out time duration for each member and test class should run successfully."


# Running maximum from a stream (add_value/get_max)

amount = [20, 30, 40, 16, 8, 10]
k = 10
def get_max(amount, k) -> int:
    return max([item + k for item in amount])
print(get_max(amount, k))

amount = [20, 30, 40, 16, 8, 10]
k = 50
def two_sum(amount, k) -> list:
    i, j = 0, 1
    res = []
    while i < len(amount):
        j = i + 1
        while j < len(amount):
            if amount[i] + amount[j] == k:
                res.append((i, j))
                j += 1
            j += 1
        i += 1
    return res
print(two_sum(amount, k))
m = [2, 4, 6, 8]
n = [3, 9, 11, 15, 5, 1, 7, 8]
print(m+n)
m.extend(n)
p = { i : n[i] * 3 for i in range(0, len(n)) if n[i] % 2 != 0 }
q = [{'name': 'John', 'score': 78}, {'name': 'Harry', 'score': 85}, {'name': 'Leo', 'score': 91}]
r = sorted(q, key=lambda x: len(x["name"]), reverse=True)
print(m)
print(p)
print(r)
n = [2, 4, 6, 8, 10, 12]
print(n[:2], n[0:5:1])