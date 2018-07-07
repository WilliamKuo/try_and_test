from commands import getstatusoutput
import csv
import pprint

def read_csv_file(src_file, delimiter=','):
    """ 
    Read CSV file and convert to dictionary
    
    :param src_file:  
    :param delimiter: default is ','  
    :return head_list: 
    :return data_list: 
    """
    data_list = list()
    head_list = list()
    with open(src_file, 'rb') as f:
        data_obj = csv.reader(f, delimiter=delimiter)
        for row in data_obj:
            if not head_list:
                head_list = row
                continue
            data_list.append(row)
 
    return head_list, data_list

def write_csv_file(src_file, data_head_list, data_row_list, delimiter=','):
    """
    Write list to CSV file 
    
    :param src_file:  
    :param data_head_list: item name in list
    :param data_list: list of row in list
    :param delimiter: default is ','  
    :return bool: or raise 
    """
    with open(src_file, 'wb') as f:    
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerow(data_head_list)
        for row in data_row_list:
            writer.writerow(row)

    return True

TEST = 'test2.csv'

write_csv_file(TEST, ['A', 'B', 'C', 'D'], [[1, 2, 3, 4], ['aa', 'bb', 'cc', 'dd',], [1, 2, 3]])
pprint.pprint(read_csv_file(TEST))









