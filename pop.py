a = ['foo', 'bar', 'baz', 'qux', 'corge'] #LIST = [ ]
while a: #while a is true
    if len(a) < 3: #if length is less that 3 
        break #continue
    print(a.pop())
print('Done.')