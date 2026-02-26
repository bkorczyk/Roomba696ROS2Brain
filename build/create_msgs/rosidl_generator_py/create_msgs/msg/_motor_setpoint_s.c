// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from create_msgs:msg/MotorSetpoint.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "create_msgs/msg/detail/motor_setpoint__struct.h"
#include "create_msgs/msg/detail/motor_setpoint__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool create_msgs__msg__motor_setpoint__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
    if (class_attr == NULL) {
      return false;
    }
    PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
    if (name_attr == NULL) {
      Py_DECREF(class_attr);
      return false;
    }
    PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
    if (module_attr == NULL) {
      Py_DECREF(name_attr);
      Py_DECREF(class_attr);
      return false;
    }

    // PyUnicode_1BYTE_DATA is just a cast
    assert(strncmp("create_msgs.msg._motor_setpoint", (char *)PyUnicode_1BYTE_DATA(module_attr), 31) == 0);
    assert(strncmp("MotorSetpoint", (char *)PyUnicode_1BYTE_DATA(name_attr), 13) == 0);

    Py_DECREF(module_attr);
    Py_DECREF(name_attr);
    Py_DECREF(class_attr);
  }
  create_msgs__msg__MotorSetpoint * ros_message = _ros_message;
  {  // duty_cycle
    PyObject * field = PyObject_GetAttrString(_pymsg, "duty_cycle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->duty_cycle = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * create_msgs__msg__motor_setpoint__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of MotorSetpoint */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("create_msgs.msg._motor_setpoint");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "MotorSetpoint");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  create_msgs__msg__MotorSetpoint * ros_message = (create_msgs__msg__MotorSetpoint *)raw_ros_message;
  {  // duty_cycle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->duty_cycle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "duty_cycle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
