# generated from rosidl_generator_py/resource/_idl.py.em
# with input from create_msgs:msg/Bumper.idl
# generated code does not contain a copyright notice

from __future__ import annotations

import collections.abc
from os import getenv
import typing

import rosidl_pycommon.interface_base_classes

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


if typing.TYPE_CHECKING:
    from std_msgs.msg import Header
    from ctypes import Structure

    class PyCapsule(Structure):
        pass  # don't need to define the full structure


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Bumper(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'Bumper'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class BumperConstants(typing.TypedDict):
        pass

    __constants: BumperConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('create_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'create_msgs.msg.Bumper')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__bumper
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__bumper
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__bumper
            cls._TYPE_SUPPORT = module.type_support_msg__msg__bumper
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__bumper

            from std_msgs.msg import Header
            if Header._TYPE_SUPPORT is None:
                Header.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Bumper(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_Bumper):
    """Message class 'Bumper'."""

    __slots__ = [
        '_header',
        '_is_left_pressed',
        '_is_right_pressed',
        '_is_light_left',
        '_is_light_front_left',
        '_is_light_center_left',
        '_is_light_center_right',
        '_is_light_front_right',
        '_is_light_right',
        '_light_signal_left',
        '_light_signal_front_left',
        '_light_signal_center_left',
        '_light_signal_center_right',
        '_light_signal_front_right',
        '_light_signal_right',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'is_left_pressed': 'boolean',
        'is_right_pressed': 'boolean',
        'is_light_left': 'boolean',
        'is_light_front_left': 'boolean',
        'is_light_center_left': 'boolean',
        'is_light_center_right': 'boolean',
        'is_light_front_right': 'boolean',
        'is_light_right': 'boolean',
        'light_signal_left': 'uint16',
        'light_signal_front_left': 'uint16',
        'light_signal_center_left': 'uint16',
        'light_signal_center_right': 'uint16',
        'light_signal_front_right': 'uint16',
        'light_signal_right': 'uint16',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[Header] = None,  # noqa: E501
                 is_left_pressed: typing.Optional[bool] = None,  # noqa: E501
                 is_right_pressed: typing.Optional[bool] = None,  # noqa: E501
                 is_light_left: typing.Optional[bool] = None,  # noqa: E501
                 is_light_front_left: typing.Optional[bool] = None,  # noqa: E501
                 is_light_center_left: typing.Optional[bool] = None,  # noqa: E501
                 is_light_center_right: typing.Optional[bool] = None,  # noqa: E501
                 is_light_front_right: typing.Optional[bool] = None,  # noqa: E501
                 is_light_right: typing.Optional[bool] = None,  # noqa: E501
                 light_signal_left: typing.Optional[int] = None,  # noqa: E501
                 light_signal_front_left: typing.Optional[int] = None,  # noqa: E501
                 light_signal_center_left: typing.Optional[int] = None,  # noqa: E501
                 light_signal_center_right: typing.Optional[int] = None,  # noqa: E501
                 light_signal_front_right: typing.Optional[int] = None,  # noqa: E501
                 light_signal_right: typing.Optional[int] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.is_left_pressed = is_left_pressed if is_left_pressed is not None else bool()
        self.is_right_pressed = is_right_pressed if is_right_pressed is not None else bool()
        self.is_light_left = is_light_left if is_light_left is not None else bool()
        self.is_light_front_left = is_light_front_left if is_light_front_left is not None else bool()
        self.is_light_center_left = is_light_center_left if is_light_center_left is not None else bool()
        self.is_light_center_right = is_light_center_right if is_light_center_right is not None else bool()
        self.is_light_front_right = is_light_front_right if is_light_front_right is not None else bool()
        self.is_light_right = is_light_right if is_light_right is not None else bool()
        self.light_signal_left = light_signal_left if light_signal_left is not None else int()
        self.light_signal_front_left = light_signal_front_left if light_signal_front_left is not None else int()
        self.light_signal_center_left = light_signal_center_left if light_signal_center_left is not None else int()
        self.light_signal_center_right = light_signal_center_right if light_signal_center_right is not None else int()
        self.light_signal_front_right = light_signal_front_right if light_signal_front_right is not None else int()
        self.light_signal_right = light_signal_right if light_signal_right is not None else int()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Bumper):
            return False
        if self.header != other.header:
            return False
        if self.is_left_pressed != other.is_left_pressed:
            return False
        if self.is_right_pressed != other.is_right_pressed:
            return False
        if self.is_light_left != other.is_light_left:
            return False
        if self.is_light_front_left != other.is_light_front_left:
            return False
        if self.is_light_center_left != other.is_light_center_left:
            return False
        if self.is_light_center_right != other.is_light_center_right:
            return False
        if self.is_light_front_right != other.is_light_front_right:
            return False
        if self.is_light_right != other.is_light_right:
            return False
        if self.light_signal_left != other.light_signal_left:
            return False
        if self.light_signal_front_left != other.light_signal_front_left:
            return False
        if self.light_signal_center_left != other.light_signal_center_left:
            return False
        if self.light_signal_center_right != other.light_signal_center_right:
            return False
        if self.light_signal_front_right != other.light_signal_front_right:
            return False
        if self.light_signal_right != other.light_signal_right:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self) -> Header:
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value: Header) -> None:

        if self._check_fields:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def is_left_pressed(self) -> bool:
        """Message field 'is_left_pressed'."""
        return self._is_left_pressed

    @is_left_pressed.setter
    def is_left_pressed(self, value: bool) -> None:

        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'is_left_pressed' field must be of type 'bool'"
        self._is_left_pressed = value

    @builtins.property
    def is_right_pressed(self) -> bool:
        """Message field 'is_right_pressed'."""
        return self._is_right_pressed

    @is_right_pressed.setter
    def is_right_pressed(self, value: bool) -> None:

        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'is_right_pressed' field must be of type 'bool'"
        self._is_right_pressed = value

    @builtins.property
    def is_light_left(self) -> bool:
        """Message field 'is_light_left'."""
        return self._is_light_left

    @is_light_left.setter
    def is_light_left(self, value: bool) -> None:

        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'is_light_left' field must be of type 'bool'"
        self._is_light_left = value

    @builtins.property
    def is_light_front_left(self) -> bool:
        """Message field 'is_light_front_left'."""
        return self._is_light_front_left

    @is_light_front_left.setter
    def is_light_front_left(self, value: bool) -> None:

        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'is_light_front_left' field must be of type 'bool'"
        self._is_light_front_left = value

    @builtins.property
    def is_light_center_left(self) -> bool:
        """Message field 'is_light_center_left'."""
        return self._is_light_center_left

    @is_light_center_left.setter
    def is_light_center_left(self, value: bool) -> None:

        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'is_light_center_left' field must be of type 'bool'"
        self._is_light_center_left = value

    @builtins.property
    def is_light_center_right(self) -> bool:
        """Message field 'is_light_center_right'."""
        return self._is_light_center_right

    @is_light_center_right.setter
    def is_light_center_right(self, value: bool) -> None:

        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'is_light_center_right' field must be of type 'bool'"
        self._is_light_center_right = value

    @builtins.property
    def is_light_front_right(self) -> bool:
        """Message field 'is_light_front_right'."""
        return self._is_light_front_right

    @is_light_front_right.setter
    def is_light_front_right(self, value: bool) -> None:

        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'is_light_front_right' field must be of type 'bool'"
        self._is_light_front_right = value

    @builtins.property
    def is_light_right(self) -> bool:
        """Message field 'is_light_right'."""
        return self._is_light_right

    @is_light_right.setter
    def is_light_right(self, value: bool) -> None:

        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'is_light_right' field must be of type 'bool'"
        self._is_light_right = value

    @builtins.property
    def light_signal_left(self) -> int:
        """Message field 'light_signal_left'."""
        return self._light_signal_left

    @light_signal_left.setter
    def light_signal_left(self, value: int) -> None:

        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'light_signal_left' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'light_signal_left' field must be an unsigned integer in [0, 65535]"
        self._light_signal_left = value

    @builtins.property
    def light_signal_front_left(self) -> int:
        """Message field 'light_signal_front_left'."""
        return self._light_signal_front_left

    @light_signal_front_left.setter
    def light_signal_front_left(self, value: int) -> None:

        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'light_signal_front_left' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'light_signal_front_left' field must be an unsigned integer in [0, 65535]"
        self._light_signal_front_left = value

    @builtins.property
    def light_signal_center_left(self) -> int:
        """Message field 'light_signal_center_left'."""
        return self._light_signal_center_left

    @light_signal_center_left.setter
    def light_signal_center_left(self, value: int) -> None:

        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'light_signal_center_left' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'light_signal_center_left' field must be an unsigned integer in [0, 65535]"
        self._light_signal_center_left = value

    @builtins.property
    def light_signal_center_right(self) -> int:
        """Message field 'light_signal_center_right'."""
        return self._light_signal_center_right

    @light_signal_center_right.setter
    def light_signal_center_right(self, value: int) -> None:

        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'light_signal_center_right' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'light_signal_center_right' field must be an unsigned integer in [0, 65535]"
        self._light_signal_center_right = value

    @builtins.property
    def light_signal_front_right(self) -> int:
        """Message field 'light_signal_front_right'."""
        return self._light_signal_front_right

    @light_signal_front_right.setter
    def light_signal_front_right(self, value: int) -> None:

        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'light_signal_front_right' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'light_signal_front_right' field must be an unsigned integer in [0, 65535]"
        self._light_signal_front_right = value

    @builtins.property
    def light_signal_right(self) -> int:
        """Message field 'light_signal_right'."""
        return self._light_signal_right

    @light_signal_right.setter
    def light_signal_right(self, value: int) -> None:

        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'light_signal_right' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'light_signal_right' field must be an unsigned integer in [0, 65535]"
        self._light_signal_right = value
