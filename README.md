# Read Me
## Split <file-name> with the size of <number> MB 
```
python split_file.py -n <file-name> -s <number>
```
### Example
```
python split_file.py -n file.json -s 2
```


## Split file in size of <number> and give you of <x1,..,xn> files

*<x1,x2,...,xn> is set of numbers seprated with ','*
```
python split_file.py -n <file-name> -s <number> -f <x1,x2,...,xn>
```
### Example
```
python split_file.py -n file.json -s 2 -f 1,2,7
```
