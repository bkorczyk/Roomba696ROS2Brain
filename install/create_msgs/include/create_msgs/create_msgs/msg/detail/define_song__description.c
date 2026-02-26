// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from create_msgs:msg/DefineSong.idl
// generated code does not contain a copyright notice

#include "create_msgs/msg/detail/define_song__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_create_msgs
const rosidl_type_hash_t *
create_msgs__msg__DefineSong__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x02, 0xbf, 0x2e, 0x20, 0xe0, 0x24, 0xc5, 0xf5,
      0xb2, 0x48, 0x20, 0xd7, 0x20, 0xba, 0xc2, 0x9e,
      0x5b, 0x7e, 0x60, 0x90, 0xb8, 0xa0, 0x6d, 0x55,
      0x55, 0xbd, 0x2e, 0xf4, 0xa0, 0xac, 0xbe, 0x37,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char create_msgs__msg__DefineSong__TYPE_NAME[] = "create_msgs/msg/DefineSong";

// Define type names, field names, and default values
static char create_msgs__msg__DefineSong__FIELD_NAME__song[] = "song";
static char create_msgs__msg__DefineSong__FIELD_NAME__length[] = "length";
static char create_msgs__msg__DefineSong__FIELD_NAME__notes[] = "notes";
static char create_msgs__msg__DefineSong__FIELD_NAME__durations[] = "durations";

static rosidl_runtime_c__type_description__Field create_msgs__msg__DefineSong__FIELDS[] = {
  {
    {create_msgs__msg__DefineSong__FIELD_NAME__song, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {create_msgs__msg__DefineSong__FIELD_NAME__length, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {create_msgs__msg__DefineSong__FIELD_NAME__notes, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8_UNBOUNDED_SEQUENCE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {create_msgs__msg__DefineSong__FIELD_NAME__durations, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT_UNBOUNDED_SEQUENCE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
create_msgs__msg__DefineSong__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {create_msgs__msg__DefineSong__TYPE_NAME, 26, 26},
      {create_msgs__msg__DefineSong__FIELDS, 4, 4},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "uint8 song            # song number [0-3]\n"
  "uint8 length          # song length [1-16]\n"
  "uint8[] notes         # notes defined by the MIDI note numbering scheme. Notes outside the range of [31-127] are rest notes.\n"
  "float32[] durations   # durations in seconds. Maximum duration is 255/64.";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
create_msgs__msg__DefineSong__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {create_msgs__msg__DefineSong__TYPE_NAME, 26, 26},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 284, 284},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
create_msgs__msg__DefineSong__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *create_msgs__msg__DefineSong__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
