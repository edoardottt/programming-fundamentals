""" 
    A common way of storing tables is as dictionary lists. 
    Each row of the table corresponds to a dictionary whose keys are the names of the columns of the table. 
    This collection of dictionaries is then stored in a list. 5 For example the table
    
    name  | year | tel
  --------|------|---------
   Sofia  | 1973 | 5553546 
   Bruno  | 1981 | 5558432

can be stored as
[{'name': 'Sofia', 'year': 1973 ,'tel': 5553546},{'name': 'Bruno', 'year': 1981 ,'tel': 5558432}]

"""


def es26(table, column):
    """
    Implement the function es26 (table, column) that I took as input 
    - a table represented by a list of dictionaries 
    - a string with the name of one of the columns of the table 
    destructively modifies the table by reordering its rows in descending order 
    to the values ​​contained in the indicated column. The function must return the number of columns in the table.
       For example with table = [{'name': 'Bruno', 'year': 1981 ,'tel': 5558432},
                        {'name': 'Sofia', 'year': 1973 ,'tel': 5553546}]
    at the end of es26(dati, 'anno')  the table will have been changed to
    [{'name': 'Bruno', 'year': 1981 ,'tel': 5558432},{'name': 'Sofia', 'year': 1973 ,'tel': 5553546}]
    and returns the number of columns 3.
    """
    tabe = sorted(table, reverse=True, key=lambda x: x[column])
    table.clear()
    table.extend(tabe)
    return len(table[0])
