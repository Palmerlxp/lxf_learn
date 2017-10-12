#请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#版本二可以验证并提取出带名字的Email地址：

import re
# --版本一--
re1_email = re.compile(r'^[\w.]+@[\w.]+[\w.]+$')
print(re1_email.match('someone@gmail.com'))
print(re1_email.match('bill.gates@microsoft.com'))

# --版本二--
re2_email = re.compile(r'^<([\w\s]*)>\s[\w.]+@[\w.]+[\w.]+$')
name = re2_email.match('<Tom Paris> tom@voyager.org').groups(0)
print(name)