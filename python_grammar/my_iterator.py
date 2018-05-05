from collections import Iterable,Iterator
isinstance([],Iterable)#True
isinstance({},Iterable)#True
isinstance('abc',Iterable)#True
isinstance((x for x in range(10)),Iterable)#True

isinstance((x for x in range(10)),Iterator)#True
isinstance([],Iterator)#False
isinstance({},Iterator)#False
isinstance('abc',Iterator)#False

isinstance(iter([]),Iterator)#True
isinstance(iter('abc'),Iterator)#True