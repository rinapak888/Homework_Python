a = input("Текст: ").split() 
b = input("Введите тип выравнивания (left - <), (right - >), (center - ^): ")
c = input("Символ: ")
d = input("Кол-во символов: ")

def sss (a, b, c, d):
    result = ''
    f = {'center': '^','left': '<','right': '>'} 
    for i in a:
        result += ('{0:{1}{2}{3}}'.format(i, c, f[b], d)) + '\n'
    return result

print(sss(a, b, c, d))






