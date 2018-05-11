
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
 
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name == 'Model':
            print('Model:',name)
            return type.__new__(cls,name,bases,attrs)
        print('Found Model: %s' % name)
        print('attrs:',attrs)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s ==> %s' % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
    def __init__(self, **kwarg):
         return super(Model, self).__init__(**kwarg) 

    def __getattr__(self, key):
        print('get:key = %s; value = %s' % (key,self[key]))
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)
 
    def __setattr__(self, key, value):
        print('key = %s; value = %s',(key,value))
        self[key] = value

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Batman', email='batman@nasa.org', password='iamback')
u.save()