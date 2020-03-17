#!/bin/python3
import json,os,copy

js={}
strTypeMap={
        'int':['i','int','l','long'],
        'str':['s','str','string'],
        'flo':['f','float'],
        '{}':['dic','dict','{','{}'],
        '[]':['li','list','[','[]'],
        'bol':['b','bool','tf']
        }
trueList=['t','T','true','TRUE','True']
falseList=['f','F','False','false','FALSE']
yesList=['y','Y','yes','Yes','YES']
noList=['n','N','No','NO','no']

forMat={}
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
    elif t in strTypeMap['flo']:
        return 'flo'
    elif t in strTypeMap['{}']:
        return '{}'
    elif t in strTypeMap['[]']:
        return '[]'
    elif t in strTypeMap['bol']:
        return 'bol'
    else:
        raise ValueError

def formatDis():
    for k,ts in strTypeMap.items():
        print('%6s = '%k,end='')
        for t in ts:
            print('%6s'%t,' ',end='')
        print()

def getDictFormat(dis=[],strFormat=None):
    formatDis()
    if not strFormat:
        msg='''Please input the dict attributes
        usage-> key:type ...'''
        strFormat=gpi(dis)
        if not strFormat:
            print('input nothing , exit...')
            exit()
    try:
        listFormat=strFormat.split()
        forMat={}
        for item in listFormat:
            key,typ=item.split(':')
            ftyp=typeCheck(typ)
            if ftyp=='{}':
                dis.append([key,ftyp])
                forMat[key]=getDictFormat(dis)
                dis.pop()
            elif ftyp=='[]':
                dis.append([key,ftyp])
                forMat[key]=getListFormat(dis)
                dis.pop()
            else:
                forMat[key]=ftyp
    except ValueError:
        return getDictFormat(dis)
    return forMat

def getListFormat(dis=[]):
    formatDis()
    msg='''[] item attributes
    is {} ? usage-> key:type ...
    is sample class ? usage-> type'''
    print(msg)
    strFormat=gpi(dis)
    if strFormat.find(':') >= 0:
        #is {}
        #T(strFormat,'getListFormat {} strFormat')
        dis.append(['..','{}'])
        forMat=getDictFormat(dis,strFormat)
        dis.pop()
        return [forMat]
    elif strFormat in ['','\n']:
        print('input nothing,exit...')
        exit()
    strType=strFormat.split()[0]
    strType=typeCheck(strType)
    if strType=='[]':
        dis.append(['..','[]'])
        forMat=getListFormat(dis)
        dis.pop()
    else:
        # may be int,str,bol,float
        return strType


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
        if v in trueList:
            return True
        elif v in falseList:
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
    showHead(dis)
    print('is dict?y/n: ',end='')
    isDict=input()
    _dis=copy.deepcopy(dis)
    num=0
    if isDict in yesList:
        forMat=getFormat(_dis)
        while 1:
            _dis.append(['[%s]'%num,'{}'])
            num += 1
            lis.append(dictEdit(_dis,forMat))
            _dis.pop()
            showHead(dis)
            print('Press \'c\' to continue: ',end='')
            isContinue=input()
            if isContinue!='c':
                break
    elif isDict in noList:
        showHead(dis)
        print('(type): ',end='')
        strType=input()
        strType=typeCheck(strType)
        while 1:
            _dis.append(['[%s]'%num,strType])
            num += 1
            lis.append(getValue(_dis,strType))
            _dis.pop()
            showHead(dis)
            print('Press \'c\' to continue: ',end='')
            isContinue=input()
            if isContinue!='c':
                break
    return lis


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

dis=[('root','{}')]
def main():
    global js,dis,forMat
    forMat=getDictFormat(dis)

main()
print(json.dumps(forMat,indent=2))
