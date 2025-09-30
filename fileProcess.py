import pickle
import json


def hello():
	print('fileProcess.py is imported successfully')

def loadDict(fpath):
    '''
    load pickle or json file into dict data
    '''
    if fpath.endswith("pickle"):
        with open(fpath, 'rb') as file:
            my_dict = pickle.load(file)
    elif fpath.endswith("json"):
        with open(fpath, 'r') as file:
            my_dict = json.load(file)
    return my_dict


def dict2pickle(filename,dict_out):
    '''
    output dict to pickle file
    '''

    if not filename.endswith('.pickle'):
        filename=filename+'.pickle'

    with open(filename, 'wb') as file:
        pickle.dump(dict_out, file)

def loadLine2list(fpath,skip_empty=True,strip=True,comment=True):
    """
    Read a file line by line into a list.
    
    Parameters
    ----------
    fpath : str
        Path to the file.
    strip : bool, default True
        Whether to strip whitespace (like '\n') from each line.
    skip_empty : bool, default True
        Whether to skip empty lines.
    comment:
        skip lines begining with #
                
    Returns
    -------
    list of str
        List containing lines from the file.
    """
    lines = []
    with open(fpath, 'r', encoding='utf-8') as f:
        for line in f:
            if line[0]=='#' and comment:
                continue
            if strip:
                line = line.strip()
            if skip_empty and not line:
                continue
            lines.append(line)
    return lines