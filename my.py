# n = input()
n = '23'
d = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
print(len(d))
import os
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
exit()
st = []
for i in n:
    st.append(d[int(i)])
print(st)
def gen_binary(n, prefix, arr):
    if n >= len(arr)-1:
        print(prefix)
    else:
        for b in range(len(arr[n+1])):
            gen_binary(n+1, prefix+arr[n+1][b], arr)


gen_binary(0,'',st)
exit()


st = []
arr = []
for i in n:
    st.append(d[int(i)])
print(st)

def gen_st(n, pef, arr):
    if n == 0:
        print(pref)
        return

arr = []
for i in range(len(st[0])):
    buf = st[0][i]
    for j in range(len(st[1])):
        arr.append(buf + st[1][j])
print(*arr)