#!/bin/python3
# this is same tool fun
# argvParse(): argv -> {key:value..}

def T(v,msg=''):
    print('+++ ',msg,' ',v)
    if input()=='q':
        exit()

def argvParse(_argv=None):
    from sys import argv
    if not _argv:
        # remove first item
        argvs=argv[1:]
        it=iter(argvs)
    else:
        it=iter(_argv)
    n=0
    config={}
    li=[]
    nex=None
    while 1:
        try:
            if not nex:
                i=next(it)
            else:
                i=nex
                nex=None
            il=len(i)
            if i[0]=='-':
                if il == 1:
                    raise ValueError
                elif il == 2:
                    # -k
                    k=i[1]
                    config[k]=True
                    # -k v
                    nex=next(it)
                    if nex[0] != '-':
                        config[k]=nex
                        nex=None
                elif il >= 3:
                    if i[1] == '-':
                        r=i.find('=')
                        if r >= 2:
                            # --key=value
                            k=i[2:r]
                            v=i[r+1:]
                            config[k]=v
                        else:
                            # --key
                            k=i[2:]
                            config[k]=True
                    # -kv
                    elif i[1] != '-':
                        k=i[1]
                        v=i[2:]
                        config[k]=v
            else:
                # list
                li.append(i)
        except StopIteration:
            if li:
                if config:
                    return [config,li]
                return li
            if config:
                return config
        except ValueError:
            ('argv format error')
            exit(1)

from json import dumps as jsdumps
print(jsdumps(argvParse(),indent=1))
