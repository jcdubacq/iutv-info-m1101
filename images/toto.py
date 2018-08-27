import random
import unicodedata

def get_random_unicode(length,diff):
    x=''
    ranges=[[0,127],[128,2047],[2048,65535],[65536,1114111]]
    range = ranges[diff]
    while len(x)<length:
        a=random.randint(range[0],range[1])
        if ((unicodedata.category(unichr(a)))[0] == 'L' ):
            found=True
            x=x+unichr(a)
    return(x)

if __name__ == '__main__':
    print('A random string: ' + get_random_unicode(10,0))
    print('A random string: ' + get_random_unicode(10,1))
    print('A random string: ' + get_random_unicode(10,2))
    print('A random string: ' + get_random_unicode(10,3))
