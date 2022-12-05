from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class convertReply(_message.Message):
    __slots__ = ["hash"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class convertRequest(_message.Message):
    __slots__ = ["file"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: bytes
    def __init__(self, file: _Optional[bytes] = ...) -> None: ...

class deleteReply(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class deleteRequest(_message.Message):
    __slots__ = ["hash"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class downloadReply(_message.Message):
    __slots__ = ["file"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: bytes
    def __init__(self, file: _Optional[bytes] = ...) -> None: ...

class downloadRequest(_message.Message):
    __slots__ = ["hash"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class queueReply(_message.Message):
    __slots__ = ["file"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: str
    def __init__(self, file: _Optional[str] = ...) -> None: ...

class queueRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
