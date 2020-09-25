def merge_packages(items, limit):
    
    checker = 0
    counter = 0
    length = len(items)
    table = {}
    while counter < length :
        if counter == checker:
            checker += 1
            continue
        
        if checker ==length:
            counter += 1
            checker = 0
            continue
        
        x =items[counter] 
        y= items[checker]
        val = x+y
        
        if val not in table:
            table[val] = [counter,checker]
        if limit in table:
            return table[limit]
            
        checker +=1
        
        
        
    return False
        
             

print(merge_packages([4, 6, 10, 15, 16],21))