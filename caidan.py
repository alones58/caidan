import random


#lista = {1: '张三', 2: '李四', 3: '王五', 4: '赵六', 5: '王麻子', 6: '包子', 7: '豆浆'}
lista = {'张三': 1,  '李四': 2,  '王五': 3,  '赵六': 4,  '王麻子': 5,  '包子': 6,  '豆浆': 7}
b = random.randint(2, 5)
suijishu = random.sample(lista.keys(), b)  # 随机一个字典中的key，第二个参数为限制个数
print(suijishu)
key = suijishu[0]

value = lista.values(key)

print(value)