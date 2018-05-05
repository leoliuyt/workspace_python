from collections import namedtuple
#namedtuple
# namedtuple('名称', [属性list]):
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print('p:(%s,%s)' % p)

#deque
#deque是为了高效实现插入和删除操作的双向列表
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
q.popleft()
print(q)

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print(dd['key2'])

#OrderedDict
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：

from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])

od = OrderedDict([('a',1),('b',2),('c',3)])
print('d',d)
print('od',od)

#Counter 
#Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch]+=1
print(c)