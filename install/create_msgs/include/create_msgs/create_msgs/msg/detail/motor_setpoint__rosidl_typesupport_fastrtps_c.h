// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from create_msgs:msg/MotorSetpoint.idl
// generated code does not contain a copyright notice
#ifndef CREATE_MSGS__MSG__DETAIL__MOTOR_SETPOINT__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define CREATE_MSGS__MSG__DETAIL__MOTOR_SETPOINT__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "create_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "create_msgs/msg/detail/motor_setpoint__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_create_msgs
bool cdr_serialize_create_msgs__msg__MotorSetpoint(
  const create_msgs__msg__MotorSetpoint * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_create_msgs
bool cdr_deserialize_create_msgs__msg__MotorSetpoint(
  eprosima::fastcdr::Cdr &,
  create_msgs__msg__MotorSetpoint * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_create_msgs
size_t get_serialized_size_create_msgs__msg__MotorSetpoint(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_create_msgs
size_t max_serialized_size_create_msgs__msg__MotorSetpoint(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_create_msgs
bool cdr_serialize_key_create_msgs__msg__MotorSetpoint(
  const create_msgs__msg__MotorSetpoint * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_create_msgs
size_t get_serialized_size_key_create_msgs__msg__MotorSetpoint(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_create_msgs
size_t max_serialized_size_key_create_msgs__msg__MotorSetpoint(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_create_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, create_msgs, msg, MotorSetpoint)();

#ifdef __cplusplus
}
#endif

#endif  // CREATE_MSGS__MSG__DETAIL__MOTOR_SETPOINT__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
