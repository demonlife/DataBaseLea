#encoding: utf8

import redis, time

r = redis.Redis('localhost', db=0)

script1 = '''
local i=0
local b=0
local res
local limit = tonumber(KEYS[1])
while (i <= limit) do
    res = redis.call('set', i, b)
    i = i + 1
    b = b + 1
end
return KEYS[1]
'''
#r.eval(script1, 1, 200)

script2 = '''
local list = redis.call('keys', '*')
for x in pairs(list) do
    redis.call('del', x)
end
return 1
'''

try:
    print r.eval(script2, 0)
except Exception, e:
    print e
