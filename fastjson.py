#!/bin/python3
import json,os,copy

js={}
strTypeMap={
        'int':['i','int','l','long'],
        'str':['s','str','string'],
        'float':['f','float'],
        'dict':['dic','dict','{','{}'],
        'list':['li','list','[','[]']
        }

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
    else:
        raise ValueError

def formatDis():
    print('typeAlias')
    for k,ts in strTypeMap.items():
        print('%s = "'%k,end='')
        for t in ts:
            print(t,' ',end='')
        print('"')
    print('usage-> key:type ...')

def getFormat():
    formatDis()
    strFormat=input()
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

def gpi(dis=[],df=None):
    for i in dis:
        key,typ=i
        print('%s(%s)-'%(key,typ),end='')
    print('>>',end='')
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



def getValue(dis,v):
    if v=='int':
        return getInt(dis)
    elif v=='str':
        return getStr(dis)
    elif v=='float':
        return getFloat(dis)
    elif v=='dict':
        return dictEdit(dis)
    elif v=='list':
        return listEdit(dis)

def listEdit(dis):
    lis=[]


def dictEdit(dis,forMat=None):
    dic={}
    _dis=copy.deepcopy(dis)
    if not forMat:
        forMat=getFormat()
    for k,v in forMat.items():
        _dis.append((k,v))
        _v=getValue(_dis,v)
        dic[k]=_v
    return dic


def main():
    global js
    js=dictEdit([('root','{}')])

main()
cls()
print(js)

