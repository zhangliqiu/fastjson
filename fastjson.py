#!/bin/python3
import json,os,copy
from sys import argv

js={}
strTypeMap={
        'int':['i','int','l','long'],
        'str':['s','str','string'],
        'flo':['f','float'],
        '{}':['dic','dict','{','{}'],
        '[]':['li','list','[','[]'],
        'bol':['b','bool','tf']
        }
configNameMap={
        'informat':['f','format','informat'],
        'outformat':['outformat'],
        'outjson':['o','out'],
        'indent':['indent']
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
        print(msg)
        strFormat=getStrFormat(dis)
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

def getStrFormat(dis):
    return gpi(dis,head='fm')

def getListFormat(dis=[]):
    formatDis()
    msg='''[] item attributes
    is {} ? usage-> key:type ...
    is sample class ? usage-> type'''
    print(msg)
    strFormat=getStrFormat(dis)
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
        return [strType]


def showHead(dis,head=None):
    if head:
        print('<%s> '%head,end='')
    for i in dis:
        key,typ=i
        print('%s(%s)-'%(key,typ),end='')

def gpi(dis=[],df=None,head=None):
    showHead(dis,head)
    print('>> ',end='')
    _v=input()
    if _v in ['','\n']:
        return df
    return _v

def getInt(dis):
    v=gpi(dis,df=0,head='vl')
    try:
        return int(v)
    except Exception:
        return getInt(dis)

def getStr(dis):
    return gpi(dis,df='',head='vl')

def getFloat(dis):
    v=gpi(dis,df=0,head='vl')
    try:
        return float(v)
    except Exception:
        return getFloat(dis)

def getBool(dis):
    v=gpi(dis,head='vl')
    try:
        if v in trueList:
            return True
        elif v in falseList:
            return False
        else:
            raise ValueError
    except Exception:
        return getbool(dis)

def getDict(forMat=None,dis=None):
    dic={}
    for k,v in forMat.items():
        vtype=type(v)
        if vtype==str:
            dis.append([k,v])
            dic[k]=getvalue(dis,v)
            dis.pop()
        elif vtype==list:
            dis.append([k,'[]'])
            dic[k]=getList(forMat=v,dis=dis)
            dis.pop()
        elif vtype==dict:
            dis.append([k,'{}'])
            dic[k]=getDict(forMat=v,dis=dis)
            dis.pop()
    return dic



def getvalue(dis,v):
    if v=='int':
        return getInt(dis)
    elif v=='str':
        return getStr(dis)
    elif v=='flo':
        return getFloat(dis)
    elif v=='bol':
        return getBool(dis)

def keyFormat(_config,keyMap):
    config={}
    for key,klist in keyMap.items():
        for alikey in klist:
            value=_config.get(alikey)
            if value:
                config[key]=value
                break
    return config

def argvParse(argv,keyMap=None):
    n=0
    _config={}
    alen=len(argv)
    while n<alen:
        item=argv[n]
        ilen=len(item)
        i2=item[1]
        if i2=='-':
            # --indent=2
            key,value=item[2:].split('=')
            _config[key]=value
            n += 1
            continue
        if ilen==2:
            key,value=i2,argv[n+1]
            _config[key]=value
            n += 2
            continue
        if ilen>2:
            key,value=i2,item[2:]
            _config[key]=value
            n += 1
            continue
    if not keyMap:
        return _config
    else:
        return keyFormat(_config,keyMap)


def jsSave(path,dic,indent=None):
    with open(path,'w') as f:
        json.dump(dic,f,indent=indent)
    print(path,' save finished')

def jsRead(path):
    if os.path.isfile(path):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:
            print(path,' format error')
            exit(1)

if len(argv):
    argv=argv[1:]


#forMat=getDictFormat([['root','{}']])
config=argvParse(argv,configNameMap)
# informat outformat outjson indent
dis=[['root','{}']]
outjson=config.get('outjson')
informat=config.get('informat')
outformat=config.get('outformat')
indent=config.get('indent')
if indent:
    indent=1
if informat:
    forMat=readFormat(informat)
else:
    forMat=getDictFormat(dis)
    if outformat:
        jsSave(path=outformat,dic=forMat,indent=indent)
js=getDict(forMat=forMat,dis=dis)
if outjson:
    jsSave(path=outjson,dic=js,indent=indent)
else:
    sPath=gpi(head='out path ')
    jsSave(path=sPath,dic=js)
