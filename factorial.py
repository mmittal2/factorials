num = int(input("Integer: "))

def cal_factorial(num):
    answer = [1]
    return recursive_cal_factorial(num, 1, answer)

def recursive_cal_factorial(num, current_num, answer):
    if num == current_num:
        result = ""
        for x in answer:
            result += str(x)
        result = int(result)
        print(result)
    else:
        second_num = 0
        first_num = 0
        current_num += 1
        new_answer = []
        for i in range(len(answer) - 1, -1, -1):
            if i == len(answer) - 1:
                new_num = int(current_num * answer[i])
            else:
                new_num = int(current_num * answer[i] + second_num)
            if new_num > 9:
                first_num = int(new_num % 10)
                second_num = int(new_num / 10)
                new_answer.insert(0, first_num)
            else:
                second_num = 0
                new_answer.insert(0, new_num)
        if second_num != 0:
            new_answer.insert(0, second_num)
        recursive_cal_factorial(num, current_num, new_answer)
            

cal_factorial(num)
