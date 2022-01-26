# определить номер четверти плоскости, в которой находится точка с координатами x и y, причем x!=0 и y != 0

def definition_quarter(x,y):
  s=''
  if x>0 and y>0:
    s = 'вторая четверть'
  elif x>0 and y<0:
    s='третья четверть'
  elif x<0 and y<0:
    s ='четвертая четверть'
  else:
    s='первая четверть'
  return s
print(definition_quarter(-5,5))
