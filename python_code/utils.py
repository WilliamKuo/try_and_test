#########################################################################
#  (C) Copyright Promise Technology Inc., 2014 All Rights Reserved      #
#  Author: William Kuo <william.kuo@tw.promise.com>                     #
#  Date: 2017-01-5                                                      #
#  Code description:                                                    #
#       Common API for ljubljana.                                       #
#       Any import from python original module go to here.              #
#       Please keep here as simple as possible.                         #
#########################################################################

import copy
import csv
import os
import sys
import uuid
import time
import datetime
import re
import inspect
import math
import json
import requests
import grp
import pwd
import subprocess
from commands import getstatusoutput
from distutils.version import LooseVersion
from ljubljana.manager.comm.path import HH_MASTER_KEY_PATH, PATH_TMP


def run_cmd(cmd):
    """
    Run bash command
    
    :param cmd: bash command 
    :return ret: return code 
    :return res: result message
    """
    # Not recommend adding retry, cut unwanted string in res, log, ....
    # Good way just import this and wrap it in your own run command API
    # (ljubljana/manager/library/core/exec.py)

    #print 'cmd:[{}]'.format(cmd)
    ret, res = getstatusoutput('sudo '+cmd)
    _eight_bit_mask = 0xff
    #sig = ret & _eight_bit_mask
    ret = ret >> 8 & _eight_bit_mask
    #print 'ret:[{}] res:[{}]\n'.format(ret, res)

    return ret, res


def py_background(script_name):
    """
    Run a python script in back ground
    
    :param script_name: 
    :return process_nu: 
    """
    # Will not be use in future
    process_nu = subprocess.Popen(['nohup', 'python', script_name])

    return process_nu


def path_join(path_l, path_r):
    """
    Combined two path to one path.
    
    :param path_l: path base
    :param path_r: path branch
    :return path_combined: 
    """
    path_combined = os.path.join(path_l, path_r)

    return path_combined


def path_exist(path):
    """
    Check path exist or not.
    
    :param path: target path 
    :return bool: 
    """
    if os.path.exists(path):
        return True

    return False


def sleeping(sec=1):
    """
    # Time(sec) for sleep.
    
    :param sec: Time for sleep.(default 1 sec) 
    :return True: 
    """
    time.sleep(sec)
        
    return True


def generate_id():
    """
    Generate UUID
    
    :param -: 
    :return uuid_str:  UUID1
    """
    uid_str = uuid.uuid1().__str__()

    return uid_str


def ceil(n):
    """
    Returns ceiling value of n - the smallest integer not less than x
    
    :param n: 
    :return ret: 
    """
    return math.ceil(n)


def check_value_in_list(value, check_list):
    """
    To see if some value is in list or not.
    
    :param value: The value which to be checked.
    :param check_list: Reference of list. 
    :return bool: 
    """
    if value in check_list:
        return True
 
    return False
          

def count_message_line(msg):
    """
    Return line count in input message.
    
    :param msg: string and \n ...
    :return count: line number in message 
    """
    count = 0
    for line in msg.split('\n'):
        count += 1
 
    return count
          

def count_file_line(input_file):
    """
    Return line count in input file.
    
    :param input_file: 
    :return count: line number in file 
    """
    count = 0
    with open(input_file, 'r') as f:
        for line in f:
            count += 1
 
    return count


def get_int_in_file(src_file):
    """
    Get non-negative integer value from file.
    
    :param src_file: File path name contains an non-negative integer value.
    :return ret: Integer value get from file or return -1 if fail. 
    """
    ret = -1
    with open(src_file) as f:
        for line in f:
            ret = int(line)
            break 
                
    return ret


def read_str_from_file(src_file):
    """
    Get string from file.
    
    :param src_file: 
    :return str: return string 
    """
    with open(src_file, 'r') as f:
        ret = f.read()
                
    return ret.strip()


def write_str_to_file(src_file, str_line):
    """
    Write one string to file.
    
    :param src_file: 
    :param str_line: A string input 
    :return bool: or raise 
    """
    with open(src_file, 'w+') as f:
        f.write('{}'.format(str_line))
    
    return True


def append_str_to_file(src_file, str_line):
    """
    Append one line to file.
    
    :param src_file: 
    :param str_line: Add line to file.(auto next line '\n')
    :return bool: or rase 
    """
    with open(src_file, 'a+') as f:
        f.write('{}\n'.format(str_line))
    
    return True


def delete_file(src_file):
    """
    Delete file.
    
    :param src_file: 
    :return bool: or raise 
    """
    os.remove(src_file)
    
    return True


def get_file_size(src_file):
    """
    Get file size(byte).
    
    :param src_file: 
    :return file_size:  
    """
    file_size = os.path.getsize(src_file)
    
    return file_size


def get_file_guid(src_file):
    """
    Get file uid gid.
    
    :param src_file: 
    :return uid: 
    :return gid: 
    """
    stat_info = os.stat(src_file)
    uid = stat_info.st_uid
    gid = stat_info.st_gid
    
    return uid, gid


def is_file_empty(src_file):
    """
    Check file empty or not.
    
    :param src_file: 
    :return bool: 
    """
    ret = True
    if os.stat(src_file).st_size is not 0:
        ret = False
    
    return ret


def is_file_dir(src_file):
    """
    Check file directory or not.
    
    :param src_file: 
    :return bool: 
    """
    ret = True
    if not os.path.isdir(src_file):
        ret = False
    
    return ret


def get_dir_list(path):
    """
    Return all file and directory in directory.
    
    :param path: fila path name 
    :return ret_list: list of file in it 
    """
    ret_list = os.listdir(path)
    
    return ret_list


def gen_random_file(base_path='/tmp'):
    """
    Generate a random filename in /tmp.   
    
    :param base_path: The folder path as prefix of file path. (optional)
    :return random_file: Random 'full' pathname in temp or base_path 
    """
    if not path_exist(base_path):
        base_path = PATH_TMP

    (frame, filename, line_number, function_name, lines, index) =\
        inspect.getouterframes(inspect.currentframe())[1]
    uuid_str = generate_id()
    filename = filename.split('/')[-1]

    ret_str = '{base}/{caller_file}_L{line_nu}_{uuid}'.format(
        base=base_path,
        caller_file=filename,
        line_nu=line_number,
        uuid=uuid_str,
        )

    return ret_str


def get_time_now():
    """
    Return a string about time in sec now.   
    
    :param -: 
    :return time_str: string of time 
    """
    time_str = time.time()
    
    return time_str


def get_strf_datetime(strf='%Y-%m-%d %H:%M:%S'):
    """
    Return a string about the date and time now.   
    
    :param srtf: output format
    :return time_srt: string of time 
    """
    time_str = datetime.datetime.now().strftime(strf)
    
    return time_str


def get_caller_name_line(layer=1):
    """
    Get this API file name and line number.(log debug use)
    
    :param layer: default is 1 
    :return filename: 
    :return line_number: 
    """
    (frame, filename, line_number, function_name, lines, index) =\
        inspect.getouterframes(inspect.currentframe())[layer]

    return filename, line_number


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
    Write data to CSV file (overwrite)
    
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


def read_json_file(src_file):
    """
    Read JSON file and convert to dictionary
    
    :param src_file:  
    :return data_dict: 
    """
    with open(src_file) as f:    
        data_dict = json.load(f)
    
    return data_dict


def write_json_file(src_file, data_dict):
    """
    Write dictionary to JSON file 
    
    :param src_file:  
    :param data_dict: 
    :return bool: 
    """
    with open(src_file, 'w') as f:    
        json.dump(data_dict, f)

    return True


def encode_json(data_dict):
    """
    Dictionary convert to json
    
    :param data_dict: dict
    :return json_str: string 
    """
    json_str = json.dumps(data_dict)

    return json_str


def decode_json(json_str):
    """
    JSON convert to dictionary
    
    :param json_str: string 
    :return ret_dict: dict 
    """
    ret_dict = json.loads(json_str)

    return ret_dict


def hh_curl(request, url, headers='', data='', timeout=3):
    """
    curl command control Hothatch (HTTP request) 
    
    :param request: 'get'/'post'/'delete' 
    :param url    : string                
    :param headers: dictionary            
    :param data   : dictionary            
    :param timeout: int sec               
    :return ret    : http return status code 
    :return head   : dictionary              
    :return content: dictionary              
    """
    #print 'RestAPI URL: {}' .format(url)
    #print 'Header: {}' .format(headers)
    #print 'Data: {}' .format(data)
    if data != '':
        data = encode_json(data)

    if request == 'GET':
        ret_obj = requests.get(
            url, headers=headers, timeout=timeout
        )
    elif request == 'POST':
        ret_obj = requests.post(
            url, headers=headers, data=data, timeout=timeout
        )
    elif request == 'DELETE':
        ret_obj = requests.delete(
            url, headers=headers, timeout=timeout
        )
    else:
        raise

    if type(ret_obj.status_code) != int:
        ret = int(ret_obj.status_code)
    else:
        ret = ret_obj.status_code

    header = ret_obj.headers
    
    try:
        content = decode_json(ret_obj.content)
    except:
        content = dict()

    return ret, header, content


def get_gid_info(gid):
    """
    Get group id info
    
    :param gid: group ID 
    :return gr_name:   
    :return gr_passwd:
    :return gr_gid:
    :return gr_mem:   
    """
    gr_name, gr_passwd, gr_gid, gr_mem = grp.getgrgid(gid)

    return gr_name, gr_passwd, gr_gid, gr_mem


def get_uid_info(uid):
    """
    Get user id info
    
    :param uid: user ID 
    :return pw_name: 
    :return pw_passwd: 
    :return pw_uid:    
    :return pw_gid:    
    :return pw_gecos:  
    :return pw_dir:    
    :return pw_shell:  
    """
    pw_name, pw_passwd, pw_uid, pw_gid, pw_gecos, pw_dir, pw_shell =\
        pwd.getpwuid(uid)

    return pw_name, pw_passwd, pw_uid, pw_gid, pw_gecos, pw_dir, pw_shell


def input_argv():
    """
    Get input argv
    
    :param -: 
    :return argc: number of argv list item 
    :return argv: list of input argument.([0] is file name)
    """
    argv = sys.argv
    argc = len(argv)

    return argc, argv


def ouput_stdout(code):
    """
    Standard out put script
    
    :param code: return code number 
    :return -: 
    """
    sys.exit(code)


def list_diff(list_a, list_b):
    """
    Return a list have list_a item unique than list_b item
    
    :param list_a: compare list
    :param list_b: compare list base
    :return list_diff: output list 
    """
    list_diff = list(set(list_a) - set(list_b))         

    return list_diff
    

def ver_compare(str_a, str_b):
    """
    Compare version greater and smaller
    
    :param str_a: compare string 
    :param str_b: compare string
    :return int: 1:a>b, 0:a=b, -1:a<b 
    """
    V_A = LooseVersion(str_a) 
    V_B = LooseVersion(str_b)
    if V_A > V_B:
        ret = 1
    elif V_A < V_B:
        ret = -1
    elif V_A == V_B:
        ret = 0
    else:
        raise

    return ret


def match_format(input_str, pattern):
    """
    Do a match use re.match
    
    :param input_str: 
    :param pattern: 
    :return bool: 
    """
    match = re.match(pattern, input_str)
    if match == None:
        return False

    return True


def is_mounted(path):
    """
    Check is mounted or not
    
    :param path: 
    :return bool: 
    """
    ret = os.path.ismount(path)

    return ret


def is_linked(path):
    """
    To determine if a directory entry is a symlink
    
    :param path: 
    :return bool: 
    """
    ret = os.path.islink(path)

    return ret


def is_dm_str(input_str):
    """
    To determine if is a domain name string
    
    :param input_str: 
    :return bool: 
    """
    if len(input_str) > 255:
        return False
    if input_str[-1] == ".":
        # strip exactly one dot from the right, if present
        input_str = input_str[:-1] 
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)

    return all(allowed.match(x) for x in input_str.split("."))


def is_config_volume(volume):
    """
    Check if the volume is config volume (system datastore).
    
    :param volume: 
    :return: bool
    """
    return volume.get('config_volume', False)


def generate_gluster_key(volume_name, volume_id):
    """
    Create gluster encrypt key and put in file.
    
    :param volume_name: 
    :param volume_id: 
    :return: 
    """
    # _valid_list = [
    #     ('Gluster volume name', volume_name, str, None, None),
    #     ('Gluster volume ID', volume_id, str, None, None),
    # ]
    # valid_param_list(valid_list=_valid_list)

    # gen master key for gluster volume use
    _key_file_path = '{filepath}/{filename}' .format(
        filepath=HH_MASTER_KEY_PATH,
        filename=volume_name
    )
    _key_content = volume_name.replace('-', '') + volume_id.replace('-', '')

    _counter = 0
    while read_str_from_file(_key_file_path) != _key_content:
        write_str_to_file(_key_file_path, _key_content)
        _counter += 1
        if _counter > 5:
            raise Exception('Failed to create share disk encrypt key.')

    return True


def delete_gluster_key(volume_name):
    """
    Delete gluster encrypt key file.
    
    :param volume_name: 
    :return: 
    """
    _key_file_path = '{filepath}/{filename}' .format(
        filepath=HH_MASTER_KEY_PATH,
        filename=volume_name
    )
    os.remove(_key_file_path)

    return True


def copy_shallow(in_put):
    """
    Return a shallow copy of in_put.

    :param in_put: list or dict
    :return: same as in_put type
    """
    out_put = copy.copy(in_put)

    return out_put 


def copy_deep(in_put):
    """
    Return a deep copy of in_put.

    :param in_put: list or dict
    :return: same as in_put type
    """
    out_put = copy.deepcopy(in_put)

    return out_put 
