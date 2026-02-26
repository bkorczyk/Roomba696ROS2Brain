// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from create_msgs:msg/PlaySong.idl
// generated code does not contain a copyright notice

#include "create_msgs/msg/detail/play_song__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_create_msgs
const rosidl_type_hash_t *
create_msgs__msg__PlaySong__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x22, 0xdf, 0x61, 0x18, 0x23, 0x4c, 0x4d, 0x0f,
      0x47, 0xff, 0xaa, 0xec, 0x83, 0xfb, 0xaa, 0x55,
      0x7c, 0xb5, 0x24, 0x75, 0xc0, 0xf3, 0x1e, 0xea,
      0x31, 0x23, 0xae, 0x01, 0xf4, 0x62, 0x37, 0xf5,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char create_msgs__msg__PlaySong__TYPE_NAME[] = "create_msgs/msg/PlaySong";

// Define type names, field names, and default values
static char create_msgs__msg__PlaySong__FIELD_NAME__song[] = "song";

static rosidl_runtime_c__type_description__Field create_msgs__msg__PlaySong__FIELDS[] = {
  {
    {create_msgs__msg__PlaySong__FIELD_NAME__song, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
create_msgs__msg__PlaySong__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {create_msgs__msg__PlaySong__TYPE_NAME, 24, 24},
      {create_msgs__msg__PlaySong__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "uint8 song      # song number [0-3]";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
create_msgs__msg__PlaySong__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {create_msgs__msg__PlaySong__TYPE_NAME, 24, 24},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 36, 36},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
create_msgs__msg__PlaySong__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *create_msgs__msg__PlaySong__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
