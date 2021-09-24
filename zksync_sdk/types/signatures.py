from dataclasses import dataclass
from enum import Enum


class SignatureType(Enum):
    ethereum_signature = "EthereumSignature"
    EIP1271_signature = "EIP1271Signature"


@dataclass
class TxEthSignature:
    type: SignatureType
    signature: str

    @classmethod
    def from_dict(cls, json: dict):
        """
        Only the difference from __init__ that signature is already in hex format
        """
        obj = cls(type=json["type"], signature=b"")
        obj.signature = json["signature"]

    def __init__(self, type: SignatureType, signature: bytes):
        self.signature = signature.hex()
        self.type = type

    def dict(self):
        return {
            "type":      self.type.value,
            "signature": self.signature
        }


@dataclass
class TxSignature:
    public_key: str
    signature: str

    @classmethod
    def from_dict(cls, json: dict):
        """
        Only the difference from __init__ is that values are already in hex format
        """
        obj = cls(public_key=b"", signature=b"")
        obj.public_key = json["pubKey"]
        obj.signature = json["signature"]

    def __init__(self, public_key: bytes, signature: bytes):
        self.public_key = public_key.hex()
        self.signature = signature.hex()

    def dict(self):
        return {
            "pubKey":    self.public_key,
            "signature": self.signature
        }
