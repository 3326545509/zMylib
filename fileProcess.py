import pickle
import json

# all_sta_dict=fileProcess.loadDict(fpath='../result/station.pickle')

def hello():
	print('fileProcess.py is imported successfully')

def loadDict(fpath):
    if fpath.endswith("pickle"):
        with open(fpath, 'rb') as file:
            my_dict = pickle.load(file)
    elif fpath.endswith("json"):
        with open(fpath, 'r') as file:
            my_dict = json.load(file)
    return my_dict


# fileProcess.dict2file(filename='../result/resp',dict_output=resp)
def dict2file(filename,dict_output):
    if not filename.endswith('.pickle'):
        filename=filename+'.pickle'

    with open(filename, 'wb') as file:
        pickle.dump(dict_output, file)