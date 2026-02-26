// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from create_msgs:msg/MotorSetpoint.idl
// generated code does not contain a copyright notice

#include "create_msgs/msg/detail/motor_setpoint__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_create_msgs
const rosidl_type_hash_t *
create_msgs__msg__MotorSetpoint__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xcb, 0x6e, 0x1f, 0x4c, 0x37, 0x3c, 0x1d, 0x86,
      0x66, 0xb5, 0xad, 0x6a, 0x33, 0xd8, 0x89, 0x69,
      0x5d, 0xf3, 0x9d, 0x63, 0x50, 0xbe, 0xa2, 0xd3,
      0x5c, 0x81, 0x00, 0x64, 0x05, 0xfe, 0x8c, 0x95,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char create_msgs__msg__MotorSetpoint__TYPE_NAME[] = "create_msgs/msg/MotorSetpoint";

// Define type names, field names, and default values
static char create_msgs__msg__MotorSetpoint__FIELD_NAME__duty_cycle[] = "duty_cycle";

static rosidl_runtime_c__type_description__Field create_msgs__msg__MotorSetpoint__FIELDS[] = {
  {
    {create_msgs__msg__MotorSetpoint__FIELD_NAME__duty_cycle, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
create_msgs__msg__MotorSetpoint__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {create_msgs__msg__MotorSetpoint__TYPE_NAME, 29, 29},
      {create_msgs__msg__MotorSetpoint__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# For the main and side brush motors, provide a duty cycle in the range [-1, 1]\n"
  "# The range of acceptable values for the vacuum motor is [0, 1]\n"
  "float32 duty_cycle\n"
  "";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
create_msgs__msg__MotorSetpoint__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {create_msgs__msg__MotorSetpoint__TYPE_NAME, 29, 29},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 164, 164},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
create_msgs__msg__MotorSetpoint__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *create_msgs__msg__MotorSetpoint__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
