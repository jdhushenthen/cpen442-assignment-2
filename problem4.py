'''
    Author: Janahan Dhushenthen (56777220)
    Date: 2021-09-29
    Description: CPEN 442 Assignment 2 - Problem 4
                 force_crc(): attempts to modify message to have desired CRC checksum (not working)
'''

import zlib

class Problem4:
    def __init__(self):
        self.md5 = "af0c5e1e4784991400b7728a99ed257e".encode()
        self.md5_crc = zlib.crc32(self.md5)
        self.message = "abcdefghijklmnopqrstuvqxyz01".encode()

    def force_crc(self):
        message_crc = zlib.crc32(self.message)
        print(hex(self.md5_crc), hex(message_crc))

        influence = zlib.crc32(self.message + bytearray(4))
        padding = (self.md5_crc ^ influence).to_bytes(4, byteorder='big')
        message_crc = zlib.crc32(self.message + padding)
        print(hex(self.md5_crc), hex(message_crc))

        while self.md5_crc != message_crc:
            padding = (self.md5_crc ^ message_crc).to_bytes(4, byteorder='big')
            message_crc = zlib.crc32(self.message + padding)
            print(hex(self.md5_crc), hex(message_crc))

if __name__ == "__main__":
    P4 = Problem4()
    P4.force_crc()