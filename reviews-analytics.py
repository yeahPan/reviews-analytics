# 留言筆數
data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
    print('檔案讀取完了，總共有', len(data), '筆留言')


# 留言平均長度
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('留言平均長度為', sum_len / len(data), '個字')

# 留言長度小於100的筆數
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('留言長度小於100的有', len(new), '筆')

# 一共有幾筆留言提到good 
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')

# 文字計數
wc = {} # word_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

for word in wc:
    if wc[word] > 100:
        print(word, wc[word])       
print('字典中有', len(wc), '個字')

# 查詢功能
while True:
    word = input('請輸入要查的字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, wc[word])
    else:
        print('這個字沒出現過!')
    
print('感謝使用本查詢功能')


