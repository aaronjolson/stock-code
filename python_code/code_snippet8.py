try:
    from reprlib import recursive_repr as _recursive_repr
    # pylint: disable=invalid-name
    _recursive_repr_if_available = _recursive_repr()
except ImportError:
    def _recursive_repr_if_available(function):
        return function


__all__ = ('compose',)
__version__ = '1.1.2'


def _name(obj):
    return type(obj).__name__


class compose(object):  # pylint: disable=invalid-name
    # pylint: disable=bad-option-value,useless-object-inheritance
    """Function composition: compose(f, g)(...) is equivalent to f(g(...))."""

    def __init__(self, *functions):
        """Initialize the composed function.

        Arguments:
            *functions: Functions (or other callables) to compose.
                Functions that are instances of `compose` are expanded
                into their composed functions instead of being nested.

        Raises:
            TypeError:
                If no arguments are given.
                If any argument is not callable.
        """
        if not functions:
            name = _name(self)
            raise TypeError(repr(name) + ' needs at least one argument')
        _functions = []
        for function in reversed(functions):
            if not callable(function):
                name = _name(self)
                raise TypeError(repr(name) + ' arguments must be callable')
            if isinstance(function, compose):
                _functions.append(function.__wrapped__)
                _functions.extend(function._wrappers)
            else:
                _functions.append(function)
        self.__wrapped__ = _functions[0]
        self._wrappers = tuple(_functions[1:])

    def __call__(*args, **kwargs):  # pylint: disable=no-method-argument
        """Call the composed function."""
        self, args = args[0], args[1:]
        result = self.__wrapped__(*args, **kwargs)
        for function in self._wrappers:
            result = function(result)
        return result

    @_recursive_repr_if_available
    def __repr__(self):
        """Represent the composed function as an unambiguous string."""
        arguments = ', '.join(map(repr, reversed(self.functions)))
        return _name(self) + '(' + arguments + ')'

    @property
    def functions(self):
        """Read-only tuple of the composed callables, in order of execution."""
        return (self.__wrapped__,) + tuple(self._wrappers)


# Portability to some minimal Python implementations:
try:
    compose.__name__
except AttributeError:
    compose.__name__ = 'compose'