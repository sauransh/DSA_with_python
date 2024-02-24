class Solution:
    def reorderLogFiles(self, logs:list[str])-> list[str]:
        # my solution
        # digit_log=[]
        # letter_log = []
        # for i in range(len(logs)):

        # # for log in logs:
        #     if logs[i][0] == 'l':
        #         letter_log.append(logs[i])
        #         # logs.sort(key= lambda x: x[5])
        #     else:
        #         digit_log.append(logs[i])
        #     letter_log.sort(key= lambda x:x[5])
        # return letter_log + digit_log

# Given solution
        digit_log = []
        letter_log =[]

        for log in logs:
            if log[-1].isdigit():
                digit_log.append(log)
            else:
                letter_log.append(log)

        letter_log.sort(key= lambda x :(x.split()[1:], x.split()[0]))
        
        return letter_log + digit_log


ss= Solution()
logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6','let2 own kit dig','let3 art zero']
print(ss.reorderLogFiles(logs=logs))