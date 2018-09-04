class AttributeHolder(object):
    """Abstract base class that provides __repr__.

    The __repr__ method returns a string in the format::
        ClassName(attr=name, attr=name, ...)
    The attributes are determined either by a class-level attribute,
    '_kwarg_names', or by inspecting the instance __dict__.
    """

    def __repr__(self):
        type_name = type(self).__name__
        arg_strings = []
        for arg in self._get_args():
            arg_strings.append(repr(arg))
        for name, value in self._get_kwargs():
            arg_strings.append('%s=%r' % (name, value))
        return '%s(%s)' % (type_name, ', '.join(arg_strings))

    def _get_kwargs(self):
        return sorted(self.__dict__.items())

    def _get_args(self):
        return []

class A(AttributeHolder):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def funct(self, a):
        print(a)
        print(self.args)
        print(self.kwargs)

if __name__=='__main__':
    a = A(1,2,3, name='sunminghui')
    a
