# generated from rosidl_generator_py/resource/_idl.py.em
# with input from create_msgs:msg/ChargingState.idl
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


class Metaclass_ChargingState(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ChargingState'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ChargingStateConstants(typing.TypedDict):
        CHARGE_NONE: typing.Literal[0]
        CHARGE_RECONDITION: typing.Literal[1]
        CHARGE_FULL: typing.Literal[2]
        CHARGE_TRICKLE: typing.Literal[3]
        CHARGE_WAITING: typing.Literal[4]
        CHARGE_FAULT: typing.Literal[5]

    __constants: ChargingStateConstants = {
        'CHARGE_NONE': 0,
        'CHARGE_RECONDITION': 1,
        'CHARGE_FULL': 2,
        'CHARGE_TRICKLE': 3,
        'CHARGE_WAITING': 4,
        'CHARGE_FAULT': 5,
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
                'create_msgs.msg.ChargingState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__charging_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__charging_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__charging_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__charging_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__charging_state

            from std_msgs.msg import Header
            if Header._TYPE_SUPPORT is None:
                Header.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'CHARGE_NONE': metacls.__constants['CHARGE_NONE'],
            'CHARGE_RECONDITION': metacls.__constants['CHARGE_RECONDITION'],
            'CHARGE_FULL': metacls.__constants['CHARGE_FULL'],
            'CHARGE_TRICKLE': metacls.__constants['CHARGE_TRICKLE'],
            'CHARGE_WAITING': metacls.__constants['CHARGE_WAITING'],
            'CHARGE_FAULT': metacls.__constants['CHARGE_FAULT'],
        }

    @property
    def CHARGE_NONE(self) -> typing.Literal[0]:
        """Message constant 'CHARGE_NONE'."""
        return Metaclass_ChargingState.__constants['CHARGE_NONE']

    @property
    def CHARGE_RECONDITION(self) -> typing.Literal[1]:
        """Message constant 'CHARGE_RECONDITION'."""
        return Metaclass_ChargingState.__constants['CHARGE_RECONDITION']

    @property
    def CHARGE_FULL(self) -> typing.Literal[2]:
        """Message constant 'CHARGE_FULL'."""
        return Metaclass_ChargingState.__constants['CHARGE_FULL']

    @property
    def CHARGE_TRICKLE(self) -> typing.Literal[3]:
        """Message constant 'CHARGE_TRICKLE'."""
        return Metaclass_ChargingState.__constants['CHARGE_TRICKLE']

    @property
    def CHARGE_WAITING(self) -> typing.Literal[4]:
        """Message constant 'CHARGE_WAITING'."""
        return Metaclass_ChargingState.__constants['CHARGE_WAITING']

    @property
    def CHARGE_FAULT(self) -> typing.Literal[5]:
        """Message constant 'CHARGE_FAULT'."""
        return Metaclass_ChargingState.__constants['CHARGE_FAULT']


class ChargingState(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ChargingState):
    """
    Message class 'ChargingState'.

    Constants:
      CHARGE_NONE
      CHARGE_RECONDITION
      CHARGE_FULL
      CHARGE_TRICKLE
      CHARGE_WAITING
      CHARGE_FAULT
    """

    __slots__ = [
        '_header',
        '_state',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'state': 'uint8',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[Header] = None,  # noqa: E501
                 state: typing.Optional[int] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.state = state if state is not None else int()

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
        if not isinstance(other, ChargingState):
            return False
        if self.header != other.header:
            return False
        if self.state != other.state:
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
    def state(self) -> int:
        """Message field 'state'."""
        return self._state

    @state.setter
    def state(self, value: int) -> None:

        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'state' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'state' field must be an unsigned integer in [0, 255]"
        self._state = value
