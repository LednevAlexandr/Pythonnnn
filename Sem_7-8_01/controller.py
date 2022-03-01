from fractions import Fraction
import modul_rational as modul
import view
import logger

def click():
    a1 = view.get_vallue()
    b1 = view.get_vallue()
    a2 = view.get_vallue()
    b2 = view.get_vallue()
    i = view.get_operat()
    j = view.get_number()
    # j = view.get_number()
    modul.init(j,a1,b1,a2,b2)
    result = modul.calk(i)
    view.view_data(result)  
    # logger.value_logger(i,j,result)  

