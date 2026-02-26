# generated from rosidl_generator_py/resource/_idl.py.em
# with input from create_msgs:msg/DefineSong.idl
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
    from ctypes import Structure

    class PyCapsule(Structure):
        pass  # don't need to define the full structure


# Import statements for member types

# Member 'notes'
# Member 'durations'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_DefineSong(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DefineSong'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DefineSongConstants(typing.TypedDict):
        pass

    __constants: DefineSongConstants = {
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
                'create_msgs.msg.DefineSong')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__define_song
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__define_song
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__define_song
            cls._TYPE_SUPPORT = module.type_support_msg__msg__define_song
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__define_song

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DefineSong(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DefineSong):
    """Message class 'DefineSong'."""

    __slots__ = [
        '_song',
        '_length',
        '_notes',
        '_durations',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'song': 'uint8',
        'length': 'uint8',
        'notes': 'sequence<uint8>',
        'durations': 'sequence<float>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('uint8')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
    )

    def __init__(self, *,
                 song: typing.Optional[int] = None,  # noqa: E501
                 length: typing.Optional[int] = None,  # noqa: E501
                 notes: typing.Optional[typing.Union[array.array[int], collections.abc.Sequence[int]]] = None,  # noqa: E501
                 durations: typing.Optional[typing.Union[array.array[float], collections.abc.Sequence[float]]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.song = song if song is not None else int()
        self.length = length if length is not None else int()
        self.notes = notes if notes is not None else array.array('B', [])
        self.durations = durations if durations is not None else array.array('f', [])

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
        if not isinstance(other, DefineSong):
            return False
        if self.song != other.song:
            return False
        if self.length != other.length:
            return False
        if self.notes != other.notes:
            return False
        if self.durations != other.durations:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def song(self) -> int:
        """Message field 'song'."""
        return self._song

    @song.setter
    def song(self, value: int) -> None:

        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'song' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'song' field must be an unsigned integer in [0, 255]"
        self._song = value

    @builtins.property
    def length(self) -> int:
        """Message field 'length'."""
        return self._length

    @length.setter
    def length(self, value: int) -> None:

        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'length' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'length' field must be an unsigned integer in [0, 255]"
        self._length = value

    @builtins.property
    def notes(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'notes'."""
        return self._notes

    @notes.setter
    def notes(self, value: typing.Union[array.array[int], collections.abc.Sequence[int]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'B', \
                    "The 'notes' array.array() must have the type code of 'B'"
                self._notes = value
                return
            from collections.abc import Sequence
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= 0 and val < 256 for val in value)), \
                "The 'notes' field must be sequence and each value of type 'int' and each unsigned integer in [0, 255]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._notes = array.array('B', value)  # type: ignore[assignment]

    @builtins.property
    def durations(self) -> typing.Annotated[typing.Any, array.array[float]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'durations'."""
        return self._durations

    @durations.setter
    def durations(self, value: typing.Union[array.array[float], collections.abc.Sequence[float]]) -> None:

        from collections.abc import Set
        if isinstance(value, Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'f', \
                    "The 'durations' array.array() must have the type code of 'f'"
                self._durations = value
                return
            from collections.abc import Sequence
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'durations' field must be sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._durations = array.array('f', value)  # type: ignore[assignment]
