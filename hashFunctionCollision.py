import hashlib
import time

def find_collision(digest_size):
    hashTable = {}

    #starting
    start = bytes("w24", encoding='utf8')
    h = hashlib.blake2b(digest_size=digest_size)
    h.update(start)
    hashValue = h.hexdigest()

    #add starting hv to ht
    hashTable[hashValue] = start

    # tracking time 
    beginTime = time.time()
    hfCalls = 1

    # find collision
    while True:
        # next hash value
        h = hashlib.blake2b(digest_size=digest_size)
        h.update(hashValue.encode('utf-8'))
        hashValue = h.hexdigest()
        hfCalls += 1

        #does hash value exist in hash table
        if hashValue in hashTable:
            # collision found !
            endTime = time.time()
            totalTime = endTime - beginTime
            return hashTable[hashValue], hashValue, totalTime, hfCalls
        else:
            # add hash value to hash table
            hashTable[hashValue] = hashValue



collidingValue, sameDigestValue, totalTime, hfCalls = find_collision(digest_size=6)

print("Values:")
print("Value 1:", collidingValue)
print("Value 2:", sameDigestValue)
print("Collision Time:", totalTime, "seconds")
print("Number of Hash Function Calls:", hfCalls)