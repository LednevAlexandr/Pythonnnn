#38 напишите программу , удаляющую из текста все слова содержащие абв

a = 'абва ыва ыва  абв fsвабв ывабва фабвыв'.split()
b = [lambda i:i+10 for i in a if 'абв' in i]
s = list(filter(lambda i:'абв' not in i,a ))
print(a)
print(s)
