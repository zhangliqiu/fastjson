## fastjson
this program can help me to edit json quick,you can design the json format real time or as a exist file such as:
### format.json
```{
key1:'str',# the value is string type
key2:'int',# int
key3:'flo',# float
key4:'bol',# bool
list:[	
# list class and the value is 'int' type
# the frist item format is model of list items
	'int'
	],
list1:[
	{
		key1:'int',
		key2:'str',
		list2:[

			...
		]
	}
	]
}
```
and then use `-f format.json` to config,or you can design format when run `fastjson`, 
you also can save the format object is case next to use
#### the format is recursive

## argvs
 -f --informat` config the format file`
 -o --outjson` the output path`
 --indent=2 `fill the TAB on file ,is easy to read`
 --outformat=path `to save the format object`
