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
    filtered_players = {}
    for key, value in data.items():
        if value < limit:
            filtered_players[key] = value
    max_score = 0
    for value in filtered_players.values():
        if value > int(max_score):
            max_score = value
    print(max_score)
    for k,v in filtered_players.items():
        if v == max_score:
            player = k
    return player
print(get_selected(data, 200))

op = {
    "square": lambda x: x * x,
    "cube": lambda x: x * x * x,
    "double": lambda x: x * 2,
    "noone": lambda x: x,
}

def do_op(operation, value):
    func = op[operation]
    print(op[operation], func(3))
    print(do_op)
    return op[operation](5)

print(do_op("cube", 5))

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
    elif i % 5==0 and i not in op:
        op.append(i)
    elif i % 7==0 and i not in op:
        op.append(i)
print(op)
print(sum(op))


