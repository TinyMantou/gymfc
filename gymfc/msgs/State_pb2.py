# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: State.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='State.proto',
  package='gymfc.msgs',
  syntax='proto2',
  serialized_pb=_b('\n\x0bState.proto\x12\ngymfc.msgs\".\n\x05State\x12\x10\n\x08sim_time\x18\x01 \x02(\x02\x12\x13\n\x0btest_string\x18\x02 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STATE = _descriptor.Descriptor(
  name='State',
  full_name='gymfc.msgs.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sim_time', full_name='gymfc.msgs.State.sim_time', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_string', full_name='gymfc.msgs.State.test_string', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['State'] = _STATE

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(
  DESCRIPTOR = _STATE,
  __module__ = 'State_pb2'
  # @@protoc_insertion_point(class_scope:gymfc.msgs.State)
  ))
_sym_db.RegisterMessage(State)


# @@protoc_insertion_point(module_scope)