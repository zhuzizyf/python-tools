from pylru import lrudecorator
import pylru
from functools import lru_cache
# 方法1 lru_chache
@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y

print(add(1, 2))
print(add(1, 2))
print(add(2, 3))

# calculating: 1 + 2
# 3
# 3
# calculating: 2 + 3
# 5

# 方法2 pylru 
# https://pypi.org/project/pylru/
def square(x):
    print('not hit cache')
    return x * x


size = 100
cached = pylru.FunctionCacheManager(square, size)

print(cached(7))
print(cached(6))
print(cached(7))

# The results of cached are the same as square, but automatically cached
# to speed up future calls.

cached.size()       # Returns the size of the cache
cached.size(3)      # Changes the size of the cache. x MUST be greater than
# zero. Returns the new size x.

cached.clear()      # Remove all items from the cache.


@lrudecorator(100) #size 100
def square1(x):
    print('not hit cache')
    return x * x


# The results of the square function are cached to speed up future calls.
print(square1(7))
print(square1(6))
print(square1(7))

square1.size()       # Returns the size of the cache
square1.size(10)      # Changes the size of the cache. x MUST be greater than
# zero. Returns the new size x.

square1.clear()      # Remove all items from the cache.




size = 100          # Size of the cache. The maximum number of key/value
# pairs you want the cache to hold.

cache = pylru.lrucache(size)
# Create a cache object.

value = cache[key]  # Lookup a value given its key.
cache[key] = value  # Insert a key/value pair.
del cache[key]      # Delete a value given its key.
#
# These three operations affect the order of the cache.
# Lookup and insert both move the key/value to the most
# recently used position. Delete (obviously) removes a
# key/value from whatever position it was in.

key in cache        # Test for membership. Does not affect the cache order.

value = cache.peek(key)
# Lookup a value given its key. Does not affect the
# cache order.

cache.keys()        # Return an iterator over the keys in the cache
cache.values()      # Return an iterator over the values in the cache
cache.items()       # Return an iterator over the (key, value) pairs in the
# cache.
#
# These calls have no effect on the cache order.
# lrucache is scan resistant when these calls are used.
# The iterators iterate over their respective elements
# in the order of most recently used to least recently
# used.
#
# WARNING - While these iterators do not affect the
# cache order the lookup, insert, and delete operations
# do. The result of changing the cache's order
# during iteration is undefined. If you really need to
# do something of the sort use list(cache.keys()), then
# loop over the list elements.

for key in cache:   # Caches support __iter__ so you can use them directly
    pass            # in a for loop to loop over the keys just like
    # cache.keys()

cache.size()        # Returns the size of the cache
cache.size(x)       # Changes the size of the cache. x MUST be greater than
# zero. Returns the new size x.

x = len(cache)      # Returns the number of items stored in the cache.
# x will be less than or equal to cache.size()

cache.clear()       # Remove all items from the cache.
