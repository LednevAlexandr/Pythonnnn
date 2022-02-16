from fractions import Fraction
import modul_real as modul
import view
import logger

def click():
    a1 = view.get_vallue()
    b1 = view.get_vallue()
    a2 = view.get_vallue()
    b2 = view.get_vallue()
    i = view.get_operat()
    modul.init(a1,b1,a2,b2)
    result = modul.calk(i)
    view.view_data(result)  
    logger.value_logger(i,result)  

