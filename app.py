#region-----------Imports-------------
from functools import lru_cache
import timeit
#endregion-----------Imports-------------

#region-----------Methods------------------
@lru_cache(maxsize=None)
def fibCached(n):
    if(n <= 1):
        return 1
    return fibCached(n-1) + fibCached(n-2)

def fibNoCache(n):
    if(n <= 1):
        return 1
    return fibNoCache(n-1) + fibNoCache(n-2)
#endregion---------Methods------------------

#region-----------TestMethods-------------

test_noCache = '''
for num in range(30):
    print(num, fibNoCache(num))
print('Completed')

'''
test_Cache = '''
for num in range(30):
    print(num, fibCached(num))
print('Completed')

'''
cacheImportSetup = '''
from __main__ import  fibCached
from functools import lru_cache 
'''

noCacheImportSetup = '''
from __main__ import  fibNoCache
'''

#endregion-----------TestMethods-----------

if __name__ == '__main__':
    print('Testing Non Cached Version for fibNoCache(30)')
    print(timeit.timeit(setup=noCacheImportSetup,
                        stmt =  test_noCache,
                        number = 20)) 
    print('Testing Cached Version for fibCached(30)')
    print(timeit.timeit(setup = cacheImportSetup,
                        stmt = test_Cache,
                        number = 20)) 