from datetime import datetime as dt

def value_logger(operator,data):
    with open('loger.csv', 'a') as file:
        file.write('operator;{};result;{}\n'
                    .format(operator,data))
