#!/bin/python3
import json,os,copy

js={}
strTypeMap={
        'int':['i','int','l','long'],
        'str':['s','str','string'],
        'float':['f','float'],
        'dict':['dic','dict','{','{}'],
        'list':['li','list','[','[]'],
        'bool':['bool','tf']
        }
def T(v,msg=None):
    print(msg,' ',str(v))
    input()

def cls():
    os.system('clear')

def typeCheck(t):
    if t in strTypeMap['int']:
        return 'int'
    elif t in strTypeMap['str']:
        return 'str'
    elif t in strTypeMap['float']:
        return 'flo'
    elif t in strTypeMap['dict']:
        return '{}'
    elif t in strTypeMap['list']:
        return '[]'
    elif t in strTypeMap['bool']:
        return 'bol'
    else:
        raise ValueError

def formatDis():
    for k,ts in strTypeMap.items():
        print('%s = "'%k,end='')
        for t in ts:
            print(t,' ',end='')
        print('"')

def getFormat(dis=[]):
    formatDis()
    print('\nPlease input the dict attributes \nusage-> key:type ...\n')
    strFormat=gpi(dis)
    if strFormat in ['','\n']:
        print('input nothing , exit...')
        exit()
    listFormat=strFormat.split()
    forMat={}
    print('strformat    %s'%strFormat)
    try:
        for k_t in listFormat:
            t=k_t.split(':')
            key,typ=t
            forMat[key]=typeCheck(typ)
    except ValueError:
        return getFormat()
    print('forMat:  %s'%forMat)
    return forMat

def showHead(dis):
    for i in dis:
        key,typ=i
        print('%s(%s)-'%(key,typ),end='')

def gpi(dis=[],df=None):
    showHead(dis)
    print('>> ',end='')
    _v=input()
    if _v in ['','\n']:
        return df
    return _v

def getInt(dis):
    v=gpi(dis,0)
    try:
        return int(v)
    except Exception:
        return getInt(dis)

def getStr(dis):
    return gpi(dis,'')

def getFloat(dis):
    v=gpi(dis,0)
    try:
        return float(v)
    except Exception:
        return getFloat(dis)

def getBool(dis):
    v=gpi(dis)
    try:
        if v in ['t','T','true','TRUE','True']:
            return True
        elif v in ['f','F','False','false','FALSE']:
            return False
        else:
            raise ValueError
    except Exception:
        return getBool(dis)


def getValue(dis,v):
    if v=='int':
        return getInt(dis)
    elif v=='str':
        return getStr(dis)
    elif v=='flo':
        return getFloat(dis)
    elif v=='{}':
        return dictEdit(dis)
    elif v=='[]':
        return listEdit(dis)
    elif v=='bol':
        return getBool(dis)

def listEdit(dis):
    lis=[]
    


def dictEdit(dis,forMat=None):
    dic={}
    _dis=copy.deepcopy(dis)
    if not forMat:
        forMat=getFormat(_dis)
    for k,v in forMat.items():
        if v=='dict':
            _dis.append((k,v))
        t=copy.deepcopy(_dis)
        t.append([k,v])
        _v=getValue(t,v)
        dic[k]=_v
    return dic


def main():
    global js
    js=dictEdit([('root','{}')])

main()
cls()
print(json.dumps(js,indent=2))