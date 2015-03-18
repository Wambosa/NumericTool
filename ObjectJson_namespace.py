import json

from NumericObject_class import NumericObject

TYPES = { 'NumericInfo': NumericObject}
          #ChildClass': ChildClass}


class ObjectJson(json.JSONEncoder):
    """A custom JSONEncoder class that knows how to encode core custom
    objects.

    Custom objects are encoded as JSON object literals (ie, dicts) with
    one key, '__TypeName__' where 'TypeName' is the actual name of the
    type to which the object belongs.  That single key maps to another
    object literal which is just the __dict__ of the object encoded."""

    @staticmethod
    def encode(obj):

        if isinstance(obj, tuple(TYPES.values())):

            key = '__%s__' % obj.__class__.__name__
            return { key: obj.__dict__ }

        return json.JSONEncoder.encode(obj)

    @staticmethod
    def decode(dct):

        if len(dct) == 1:

            type_name, value = dct.popitem() # dct.items()[0]

            type_name = type_name.strip('_')

            if type_name in TYPES:
                return TYPES[type_name](0, 0, value)

        return dct