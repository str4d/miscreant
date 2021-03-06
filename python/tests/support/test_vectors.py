"""test_vectors.py: Parse examples from vectors/aes_siv.tjson"""

# TODO: switch to tjson-python instead of hand-rolling a TJSON parser

import binascii
import json
from collections import namedtuple

class SIVExample(namedtuple("SIVExample", ["name", "key", "ad", "plaintext", "ciphertext"])):
    @staticmethod
    def load():
        """Load message examples from vectors/aes_siv.tjson"""
        return SIVExample.load_from_file("../vectors/aes_siv.tjson")

    @staticmethod
    def load_from_file(filename):
        """Load message examples from the specified file"""
        examples_file = open(filename, "r")
        examples_text = examples_file.read()
        examples_file.close()

        examples_tjson = json.loads(examples_text)
        examples = examples_tjson[u"examples:A<O>"]

        result = []
        for example in examples:
            result.append(SIVExample(
                name=example[u"name:s"],
                key=binascii.unhexlify(example[u"key:d16"]),
                ad=[binascii.unhexlify(ad) for ad in example[u"ad:A<d16>"]],
                plaintext=binascii.unhexlify(example[u"plaintext:d16"]),
                ciphertext=binascii.unhexlify(example[u"ciphertext:d16"])
            ))

        return result

class DblExample(namedtuple("DblExample", ["input", "output"])):
    @staticmethod
    def load():
        """Load message examples from vectors/dbl.tjson"""
        return DblExample.load_from_file("../vectors/dbl.tjson")

    @staticmethod
    def load_from_file(filename):
        """Load message examples from the specified file"""
        examples_file = open(filename, "r")
        examples_text = examples_file.read()
        examples_file.close()

        examples_tjson = json.loads(examples_text)
        examples = examples_tjson[u"examples:A<O>"]

        result = []
        for example in examples:
            result.append(DblExample(
                input=binascii.unhexlify(example[u"input:d16"]),
                output=binascii.unhexlify(example[u"output:d16"])
            ))

        return result
