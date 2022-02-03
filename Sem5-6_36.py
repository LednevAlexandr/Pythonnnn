#36 дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего. Пример : [1,5,2,3,4,6,1,7] => [ 1,7] или [1,6,7]

a = [1,5,2,3,100,6,1,7]
b=[value for index,value in enumerate(a) if a[index]>=a[index-1]]
print(b)

    
#b = list(filter(lambda x:x+1>x,a))
#print(b)
    # найти сумму чисел списка стоящих на нечетных позициях
##  b = [v for i,v in enumerate(a) if  i%2]
 # return sum(b)
