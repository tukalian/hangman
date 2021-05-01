# カプセル化

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
    
    def change_data(self, index, n):
        self.nums[index] = n

# インスタンス変数numsを直接変更
data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

# change_dataメソッドを使う
data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)
