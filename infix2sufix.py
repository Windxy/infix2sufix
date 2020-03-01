# 字符串表达式计算
# 方法1.eval()
# 方法2.先转为后缀表达式，然后进行后缀表达式计算
class Stack(object):
    def __init__(self):     self.items = []
    def isEmpty(self):      return True if len(self.items)==0 else False
    def push(self, item):   self.items.append(item)
    def pop(self):          return self.items.pop()
    def top(self):          return self.items[len(self.items) - 1]
    def pop_front(self):    return self.items.pop(0)       #本质是list，这里就直接将其当作队列~不过不妨碍栈做中转后缀的思路

# 判断是+—*/()还是数字
def str_j(s):
    if s=='(' or s=='+' or s=='-' or s=='*' or s=='/' or s==')':return True
    else : return False #如果是数字，返回0

# 中缀表达式转为后缀表达式
# 输入：字符串中缀表达式
# 输出：后缀表达式
def TranHou(str):
    Pri = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1, ')': 0}#制定优先级
    st_num = Stack()#数字栈
    st_symbol = Stack()#符号栈
    lens = len(str)
    for i in range(lens):
        if str_j(str[i]):                                   # 如果是符号
            if st_symbol.isEmpty() :                            # 如果为空，直接入栈
                st_symbol.push(str[i])
            else:                                               # 不为空
                if str[i] == "(":st_symbol.push(str[i])             # 如果是"("，直接压进去
                elif str[i] == ")":                                 # 如果是")",迭代弹出栈顶元素，直到遇到"(",然后弹出将其弹出
                    while (st_symbol.top() != "("):
                        st_num.push(st_symbol.pop())
                    st_symbol.pop()
                else:                                               # 否则，需要将优先级大于该元素的栈顶元素，一一弹出到数字栈中,然后将其压进符号栈，直到遇到"("或者为空
                    while(Pri[st_symbol.top()] >= Pri[str[i]]):
                        if st_symbol.top()=='(':
                            break
                        st_num.push(st_symbol.pop())
                        if st_symbol.isEmpty():break
                    st_symbol.push(str[i])
        else:st_num.push(str[i])                            # 如果不是符号，数字直接压进数字栈
    st_num.push(st_symbol.pop())                            # 把最后一个符号也压入数字栈
    return st_num

# 计算后缀表达式
# 输入：后缀表达式
# 输出：结果式子
def CaluHou(st):
    ans = 0
    st_temp = Stack()
    st_temp.push(st.items[0])
    while(st.isEmpty()==False):#如果不为空
        #实际上st就是个list，可以直接当作队列...
        st_temp.push(st.pop_front())
        if str_j(st_temp.top()):    #如果是符号
            a = st_temp.pop()
            b = st_temp.pop();b = int(b)
            c = st_temp.pop();c = int(c)
            if a == '+': ans = (c + b)
            elif a == '-': ans = (c - b)
            elif a == '*': ans = (c * b)
            elif a == '/': ans = (c * 1.0 / b)
            st_temp.push(ans)
            if st_temp.isEmpty():break
    return ans

if __name__ == '__main__':
    str = '2*(3-6/2+5)+(3-2)*4+4'
    st_ = TranHou(str)
    ans_ = CaluHou(st_)

    print(eval(str))
    print(ans_)
    print('Finish')
