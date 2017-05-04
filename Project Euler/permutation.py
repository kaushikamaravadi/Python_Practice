"""Permutation"""
def perms(s):
    if(len(s)==1):
        return [s]
    result=[]
    #print(result)
    for i,v in enumerate(s):
        print(i,v)
        result += [v+p for p in perms(s[:i]+s[i+1:])]
        #print(result[2])
        #print(result)
    return result


print(perms('abc'))

