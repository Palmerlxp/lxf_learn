# -练习1：根据用户输入的口令，计算出存储在数据库中的MD5口令-
import hashlib
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())

calc_md5('how to use md5 in python hashlib?')

# -练习二：设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False-
import hashlib
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    md5_password = md5.hexdigest()
    return print(db[user] == md5_password)

# ---验证---
login('michael', '123456')               #正确的用户口令
login('michael', 'e10aad')               #错误的用户口令