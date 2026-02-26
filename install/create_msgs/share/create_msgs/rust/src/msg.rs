pub mod rmw {
    #[cfg(feature = "serde")]
    use serde::{Deserialize, Serialize};

#[link(name = "create_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__Bumper() -> *const std::ffi::c_void;
}

#[link(name = "create_msgs__rosidl_generator_c")]
extern "C" {
    fn create_msgs__msg__Bumper__init(msg: *mut Bumper) -> bool;
    fn create_msgs__msg__Bumper__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Bumper>, size: usize) -> bool;
    fn create_msgs__msg__Bumper__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Bumper>);
    fn create_msgs__msg__Bumper__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Bumper>, out_seq: *mut rosidl_runtime_rs::Sequence<Bumper>) -> bool;
}

// Corresponds to create_msgs__msg__Bumper
#[repr(C)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Bumper {
    pub header: std_msgs::msg::rmw::Header,
    pub is_left_pressed: bool,
    pub is_right_pressed: bool,
    pub is_light_left: bool,
    pub is_light_front_left: bool,
    pub is_light_center_left: bool,
    pub is_light_center_right: bool,
    pub is_light_front_right: bool,
    pub is_light_right: bool,
    pub light_signal_left: u16,
    pub light_signal_front_left: u16,
    pub light_signal_center_left: u16,
    pub light_signal_center_right: u16,
    pub light_signal_front_right: u16,
    pub light_signal_right: u16,
}



impl Default for Bumper {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !create_msgs__msg__Bumper__init(&mut msg as *mut _) {
        panic!("Call to create_msgs__msg__Bumper__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Bumper {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__Bumper__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__Bumper__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__Bumper__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Bumper {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Bumper where Self: Sized {
  const TYPE_NAME: &'static str = "create_msgs/msg/Bumper";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__Bumper() }
  }
}


#[link(name = "create_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__ChargingState() -> *const std::ffi::c_void;
}

#[link(name = "create_msgs__rosidl_generator_c")]
extern "C" {
    fn create_msgs__msg__ChargingState__init(msg: *mut ChargingState) -> bool;
    fn create_msgs__msg__ChargingState__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ChargingState>, size: usize) -> bool;
    fn create_msgs__msg__ChargingState__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ChargingState>);
    fn create_msgs__msg__ChargingState__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ChargingState>, out_seq: *mut rosidl_runtime_rs::Sequence<ChargingState>) -> bool;
}

// Corresponds to create_msgs__msg__ChargingState
#[repr(C)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ChargingState {
    pub header: std_msgs::msg::rmw::Header,
    pub state: u8,
}

impl ChargingState {
    pub const CHARGE_NONE: u8 = 0;
    pub const CHARGE_RECONDITION: u8 = 1;
    pub const CHARGE_FULL: u8 = 2;
    pub const CHARGE_TRICKLE: u8 = 3;
    pub const CHARGE_WAITING: u8 = 4;
    pub const CHARGE_FAULT: u8 = 5;
}


impl Default for ChargingState {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !create_msgs__msg__ChargingState__init(&mut msg as *mut _) {
        panic!("Call to create_msgs__msg__ChargingState__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ChargingState {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__ChargingState__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__ChargingState__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__ChargingState__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ChargingState {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ChargingState where Self: Sized {
  const TYPE_NAME: &'static str = "create_msgs/msg/ChargingState";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__ChargingState() }
  }
}


#[link(name = "create_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__DefineSong() -> *const std::ffi::c_void;
}

#[link(name = "create_msgs__rosidl_generator_c")]
extern "C" {
    fn create_msgs__msg__DefineSong__init(msg: *mut DefineSong) -> bool;
    fn create_msgs__msg__DefineSong__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DefineSong>, size: usize) -> bool;
    fn create_msgs__msg__DefineSong__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DefineSong>);
    fn create_msgs__msg__DefineSong__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DefineSong>, out_seq: *mut rosidl_runtime_rs::Sequence<DefineSong>) -> bool;
}

// Corresponds to create_msgs__msg__DefineSong
#[repr(C)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DefineSong {
    pub song: u8,
    pub length: u8,
    pub notes: rosidl_runtime_rs::Sequence<u8>,
    pub durations: rosidl_runtime_rs::Sequence<f32>,
}



impl Default for DefineSong {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !create_msgs__msg__DefineSong__init(&mut msg as *mut _) {
        panic!("Call to create_msgs__msg__DefineSong__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DefineSong {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__DefineSong__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__DefineSong__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__DefineSong__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DefineSong {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DefineSong where Self: Sized {
  const TYPE_NAME: &'static str = "create_msgs/msg/DefineSong";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__DefineSong() }
  }
}


#[link(name = "create_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__Mode() -> *const std::ffi::c_void;
}

#[link(name = "create_msgs__rosidl_generator_c")]
extern "C" {
    fn create_msgs__msg__Mode__init(msg: *mut Mode) -> bool;
    fn create_msgs__msg__Mode__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Mode>, size: usize) -> bool;
    fn create_msgs__msg__Mode__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Mode>);
    fn create_msgs__msg__Mode__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Mode>, out_seq: *mut rosidl_runtime_rs::Sequence<Mode>) -> bool;
}

// Corresponds to create_msgs__msg__Mode
#[repr(C)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Mode {
    pub header: std_msgs::msg::rmw::Header,
    pub mode: u8,
}

impl Mode {
    pub const MODE_OFF: u8 = 0;
    pub const MODE_PASSIVE: u8 = 1;
    pub const MODE_SAFE: u8 = 2;
    pub const MODE_FULL: u8 = 3;
}


impl Default for Mode {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !create_msgs__msg__Mode__init(&mut msg as *mut _) {
        panic!("Call to create_msgs__msg__Mode__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Mode {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__Mode__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__Mode__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__Mode__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Mode {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Mode where Self: Sized {
  const TYPE_NAME: &'static str = "create_msgs/msg/Mode";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__Mode() }
  }
}


#[link(name = "create_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__PlaySong() -> *const std::ffi::c_void;
}

#[link(name = "create_msgs__rosidl_generator_c")]
extern "C" {
    fn create_msgs__msg__PlaySong__init(msg: *mut PlaySong) -> bool;
    fn create_msgs__msg__PlaySong__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<PlaySong>, size: usize) -> bool;
    fn create_msgs__msg__PlaySong__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<PlaySong>);
    fn create_msgs__msg__PlaySong__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<PlaySong>, out_seq: *mut rosidl_runtime_rs::Sequence<PlaySong>) -> bool;
}

// Corresponds to create_msgs__msg__PlaySong
#[repr(C)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct PlaySong {
    pub song: u8,
}



impl Default for PlaySong {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !create_msgs__msg__PlaySong__init(&mut msg as *mut _) {
        panic!("Call to create_msgs__msg__PlaySong__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for PlaySong {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__PlaySong__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__PlaySong__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__PlaySong__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for PlaySong {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for PlaySong where Self: Sized {
  const TYPE_NAME: &'static str = "create_msgs/msg/PlaySong";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__PlaySong() }
  }
}


#[link(name = "create_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__MotorSetpoint() -> *const std::ffi::c_void;
}

#[link(name = "create_msgs__rosidl_generator_c")]
extern "C" {
    fn create_msgs__msg__MotorSetpoint__init(msg: *mut MotorSetpoint) -> bool;
    fn create_msgs__msg__MotorSetpoint__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MotorSetpoint>, size: usize) -> bool;
    fn create_msgs__msg__MotorSetpoint__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MotorSetpoint>);
    fn create_msgs__msg__MotorSetpoint__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MotorSetpoint>, out_seq: *mut rosidl_runtime_rs::Sequence<MotorSetpoint>) -> bool;
}

// Corresponds to create_msgs__msg__MotorSetpoint
#[repr(C)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MotorSetpoint {
    pub duty_cycle: f32,
}



impl Default for MotorSetpoint {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !create_msgs__msg__MotorSetpoint__init(&mut msg as *mut _) {
        panic!("Call to create_msgs__msg__MotorSetpoint__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MotorSetpoint {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__MotorSetpoint__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__MotorSetpoint__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__MotorSetpoint__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MotorSetpoint {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MotorSetpoint where Self: Sized {
  const TYPE_NAME: &'static str = "create_msgs/msg/MotorSetpoint";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__MotorSetpoint() }
  }
}


#[link(name = "create_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__Cliff() -> *const std::ffi::c_void;
}

#[link(name = "create_msgs__rosidl_generator_c")]
extern "C" {
    fn create_msgs__msg__Cliff__init(msg: *mut Cliff) -> bool;
    fn create_msgs__msg__Cliff__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Cliff>, size: usize) -> bool;
    fn create_msgs__msg__Cliff__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Cliff>);
    fn create_msgs__msg__Cliff__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Cliff>, out_seq: *mut rosidl_runtime_rs::Sequence<Cliff>) -> bool;
}

// Corresponds to create_msgs__msg__Cliff
#[repr(C)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Cliff {
    pub header: std_msgs::msg::rmw::Header,
    pub is_cliff_left: bool,
    pub is_cliff_front_left: bool,
    pub is_cliff_right: bool,
    pub is_cliff_front_right: bool,
}



impl Default for Cliff {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !create_msgs__msg__Cliff__init(&mut msg as *mut _) {
        panic!("Call to create_msgs__msg__Cliff__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Cliff {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__Cliff__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__Cliff__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { create_msgs__msg__Cliff__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Cliff {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Cliff where Self: Sized {
  const TYPE_NAME: &'static str = "create_msgs/msg/Cliff";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__create_msgs__msg__Cliff() }
  }
}


}  // mod rmw

#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Bumper {
    pub header: std_msgs::msg::Header,
    pub is_left_pressed: bool,
    pub is_right_pressed: bool,
    pub is_light_left: bool,
    pub is_light_front_left: bool,
    pub is_light_center_left: bool,
    pub is_light_center_right: bool,
    pub is_light_front_right: bool,
    pub is_light_right: bool,
    pub light_signal_left: u16,
    pub light_signal_front_left: u16,
    pub light_signal_center_left: u16,
    pub light_signal_center_right: u16,
    pub light_signal_front_right: u16,
    pub light_signal_right: u16,
}



impl Default for Bumper {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(crate::msg::rmw::Bumper::default())
  }
}

impl rosidl_runtime_rs::Message for Bumper {
  type RmwMsg = crate::msg::rmw::Bumper;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        is_left_pressed: msg.is_left_pressed,
        is_right_pressed: msg.is_right_pressed,
        is_light_left: msg.is_light_left,
        is_light_front_left: msg.is_light_front_left,
        is_light_center_left: msg.is_light_center_left,
        is_light_center_right: msg.is_light_center_right,
        is_light_front_right: msg.is_light_front_right,
        is_light_right: msg.is_light_right,
        light_signal_left: msg.light_signal_left,
        light_signal_front_left: msg.light_signal_front_left,
        light_signal_center_left: msg.light_signal_center_left,
        light_signal_center_right: msg.light_signal_center_right,
        light_signal_front_right: msg.light_signal_front_right,
        light_signal_right: msg.light_signal_right,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      is_left_pressed: msg.is_left_pressed,
      is_right_pressed: msg.is_right_pressed,
      is_light_left: msg.is_light_left,
      is_light_front_left: msg.is_light_front_left,
      is_light_center_left: msg.is_light_center_left,
      is_light_center_right: msg.is_light_center_right,
      is_light_front_right: msg.is_light_front_right,
      is_light_right: msg.is_light_right,
      light_signal_left: msg.light_signal_left,
      light_signal_front_left: msg.light_signal_front_left,
      light_signal_center_left: msg.light_signal_center_left,
      light_signal_center_right: msg.light_signal_center_right,
      light_signal_front_right: msg.light_signal_front_right,
      light_signal_right: msg.light_signal_right,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      is_left_pressed: msg.is_left_pressed,
      is_right_pressed: msg.is_right_pressed,
      is_light_left: msg.is_light_left,
      is_light_front_left: msg.is_light_front_left,
      is_light_center_left: msg.is_light_center_left,
      is_light_center_right: msg.is_light_center_right,
      is_light_front_right: msg.is_light_front_right,
      is_light_right: msg.is_light_right,
      light_signal_left: msg.light_signal_left,
      light_signal_front_left: msg.light_signal_front_left,
      light_signal_center_left: msg.light_signal_center_left,
      light_signal_center_right: msg.light_signal_center_right,
      light_signal_front_right: msg.light_signal_front_right,
      light_signal_right: msg.light_signal_right,
    }
  }
}


#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ChargingState {
    pub header: std_msgs::msg::Header,
    pub state: u8,
}

impl ChargingState {
    pub const CHARGE_NONE: u8 = 0;
    pub const CHARGE_RECONDITION: u8 = 1;
    pub const CHARGE_FULL: u8 = 2;
    pub const CHARGE_TRICKLE: u8 = 3;
    pub const CHARGE_WAITING: u8 = 4;
    pub const CHARGE_FAULT: u8 = 5;
}


impl Default for ChargingState {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(crate::msg::rmw::ChargingState::default())
  }
}

impl rosidl_runtime_rs::Message for ChargingState {
  type RmwMsg = crate::msg::rmw::ChargingState;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        state: msg.state,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      state: msg.state,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      state: msg.state,
    }
  }
}


#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DefineSong {
    pub song: u8,
    pub length: u8,
    pub notes: Vec<u8>,
    pub durations: Vec<f32>,
}



impl Default for DefineSong {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(crate::msg::rmw::DefineSong::default())
  }
}

impl rosidl_runtime_rs::Message for DefineSong {
  type RmwMsg = crate::msg::rmw::DefineSong;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        song: msg.song,
        length: msg.length,
        notes: msg.notes.into(),
        durations: msg.durations.into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      song: msg.song,
      length: msg.length,
        notes: msg.notes.as_slice().into(),
        durations: msg.durations.as_slice().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      song: msg.song,
      length: msg.length,
      notes: msg.notes
          .into_iter()
          .collect(),
      durations: msg.durations
          .into_iter()
          .collect(),
    }
  }
}


#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Mode {
    pub header: std_msgs::msg::Header,
    pub mode: u8,
}

impl Mode {
    pub const MODE_OFF: u8 = 0;
    pub const MODE_PASSIVE: u8 = 1;
    pub const MODE_SAFE: u8 = 2;
    pub const MODE_FULL: u8 = 3;
}


impl Default for Mode {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(crate::msg::rmw::Mode::default())
  }
}

impl rosidl_runtime_rs::Message for Mode {
  type RmwMsg = crate::msg::rmw::Mode;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        mode: msg.mode,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      mode: msg.mode,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      mode: msg.mode,
    }
  }
}


#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct PlaySong {
    pub song: u8,
}



impl Default for PlaySong {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(crate::msg::rmw::PlaySong::default())
  }
}

impl rosidl_runtime_rs::Message for PlaySong {
  type RmwMsg = crate::msg::rmw::PlaySong;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        song: msg.song,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      song: msg.song,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      song: msg.song,
    }
  }
}


#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MotorSetpoint {
    pub duty_cycle: f32,
}



impl Default for MotorSetpoint {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(crate::msg::rmw::MotorSetpoint::default())
  }
}

impl rosidl_runtime_rs::Message for MotorSetpoint {
  type RmwMsg = crate::msg::rmw::MotorSetpoint;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        duty_cycle: msg.duty_cycle,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      duty_cycle: msg.duty_cycle,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      duty_cycle: msg.duty_cycle,
    }
  }
}


#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Cliff {
    pub header: std_msgs::msg::Header,
    pub is_cliff_left: bool,
    pub is_cliff_front_left: bool,
    pub is_cliff_right: bool,
    pub is_cliff_front_right: bool,
}



impl Default for Cliff {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(crate::msg::rmw::Cliff::default())
  }
}

impl rosidl_runtime_rs::Message for Cliff {
  type RmwMsg = crate::msg::rmw::Cliff;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        is_cliff_left: msg.is_cliff_left,
        is_cliff_front_left: msg.is_cliff_front_left,
        is_cliff_right: msg.is_cliff_right,
        is_cliff_front_right: msg.is_cliff_front_right,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      is_cliff_left: msg.is_cliff_left,
      is_cliff_front_left: msg.is_cliff_front_left,
      is_cliff_right: msg.is_cliff_right,
      is_cliff_front_right: msg.is_cliff_front_right,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      is_cliff_left: msg.is_cliff_left,
      is_cliff_front_left: msg.is_cliff_front_left,
      is_cliff_right: msg.is_cliff_right,
      is_cliff_front_right: msg.is_cliff_front_right,
    }
  }
}


