# 双指针问题


"""
给你一个 升序排列 的数组 nums ，
请你 原地 删除重复出现的元素，
使每个元素 只出现一次 ，
返回删除后数组的新长度。
元素的 相对顺序 应该保持 一致 。
"""
from shutil import move


def main1(arr):
    fast, slow = 1, 0
    while fast < len(arr):
        if arr[fast] == arr[slow]:
            fast += 1
        else:
            slow += 1
            arr[slow] = arr[fast]
            fast += 1
    
    return arr[:slow+1]


# 买卖股票的最佳时机
def main2(test2):
    days = len(test2)

    # d_profit_0 = 0
    # d_profit_1 = -test2[0]
    # print(d_profit_0, d_profit_1)
    # for i in range(1, days-1):
    #     d_profit_0 = max(d_profit_0, d_profit_1 + test2[i])
    #     d_profit_1 = max(d_profit_1, d_profit_0 - test2[i])
    #     print(d_profit_0, d_profit_1)
    # res = max(d_profit_0, d_profit_1 + test2[days-1])

    res = 0
    for d in range(days-1):
        if test2[d+1] > test2[d]:
            res += (test2[d+1] - test2[d])
        else:
            continue

    return res


# 旋转数组
def main3(nums, k):
    # 1.先全部反转
    nums = nums[::-1]

    # 2.反转前k个
    nums[:k] = nums[:k][::-1]

    # 3.反转剩余的
    nums[k-len(nums):] = nums[k-len(nums):][::-1]


# 删除零
def move_zero(nums):
    index = 0
    for j in range(len(nums)):
        if nums[j] == 0:
            continue
        else:
            nums[index] = nums[j]
            index += 1
    while(index < len(nums)):
        nums[index] = 0
        index += 1

    return nums


def int_reverse(x):
        if x == 0:
            return 0
        res = 0
        if x > 0:
            while x > 0:
                res = res * 10 + x % 10
                x = x // 10
        if x < 0:
            x = -x
            while x > 0:
                res = res * 10 + x % 10
                x = x // 10
            res = -res
        if res > pow(2, 31) or res < pow(-2, 31) - 1:
            return 0
        return res


def isPalindrome(s: str) -> bool:
    s = s.lower()
    length = len(s)
    if length == 0 or length  == 1:
        return True
    slow, fast = 0, length-1
    while slow < fast:
        while s[slow].isalnum() is False:
            slow += 1
        while s[fast].isalnum() is False:
            fast -= 1
        if s[slow] != s[fast]:
            return False
        slow += 1
        fast -= 1
    return True



if __name__ == "__main__":
    # arr = [1, 1, 2, 3, 3, 4, 5]
    # arr = [1, 1, 2]

    # print(arr)
    # res = main1(arr)

    # test2 = [7, 1, 5, 3, 6, 4]
    # res = main2(test2)
    # print(res)

    # nums = [1, 2, 3, 4, 5, 6, 7]
    # nums_set = set(nums)
    # if nums_set.add(8):
    #     print('this is ')
    # print(nums_set)

    # k = 3
    # main3(nums, k)
    # print(nums)

    # x = -321
    # num = int_reverse(x)
    # print(num)

    s = "A man, a plan, a canal: Panama"
    res = isPalindrome(s)
    print(res)
