# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncalc.proto\x12\x04\x63\x61lc\"$\n\nAddRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\"\x16\n\x08\x41\x64\x64Reply\x12\n\n\x02n1\x18\x01 \x01(\x05\"*\n\x10SubstractRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\"\x1c\n\x0eSubstractReply\x12\n\n\x02n1\x18\x01 \x01(\x05\")\n\x0fMultiplyRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\"\x1b\n\rMultiplyReply\x12\n\n\x02n1\x18\x01 \x01(\x05\"\'\n\rDivideRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\"\x19\n\x0b\x44ivideReply\x12\n\n\x02\x66\x31\x18\x01 \x01(\x02\x32\xe2\x01\n\nCalculator\x12)\n\x03\x41\x64\x64\x12\x10.calc.AddRequest\x1a\x0e.calc.AddReply\"\x00\x12;\n\tSubstract\x12\x16.calc.SubstractRequest\x1a\x14.calc.SubstractReply\"\x00\x12\x38\n\x08Multiply\x12\x15.calc.MultiplyRequest\x1a\x13.calc.MultiplyReply\"\x00\x12\x32\n\x06\x44ivide\x12\x13.calc.DivideRequest\x1a\x11.calc.DivideReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ADDREQUEST']._serialized_start=20
  _globals['_ADDREQUEST']._serialized_end=56
  _globals['_ADDREPLY']._serialized_start=58
  _globals['_ADDREPLY']._serialized_end=80
  _globals['_SUBSTRACTREQUEST']._serialized_start=82
  _globals['_SUBSTRACTREQUEST']._serialized_end=124
  _globals['_SUBSTRACTREPLY']._serialized_start=126
  _globals['_SUBSTRACTREPLY']._serialized_end=154
  _globals['_MULTIPLYREQUEST']._serialized_start=156
  _globals['_MULTIPLYREQUEST']._serialized_end=197
  _globals['_MULTIPLYREPLY']._serialized_start=199
  _globals['_MULTIPLYREPLY']._serialized_end=226
  _globals['_DIVIDEREQUEST']._serialized_start=228
  _globals['_DIVIDEREQUEST']._serialized_end=267
  _globals['_DIVIDEREPLY']._serialized_start=269
  _globals['_DIVIDEREPLY']._serialized_end=294
  _globals['_CALCULATOR']._serialized_start=297
  _globals['_CALCULATOR']._serialized_end=523
# @@protoc_insertion_point(module_scope)
