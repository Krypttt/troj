import struct

def int_to_bytes(n):
    if n < (1 << 8):
        tag = 'B'
    elif n < (1 << 16):
        tag = 'H'
    elif n < (1 << 32):
        tag = 'L'
    elif n < (1 << 64):
        tag = 'Q'
    return tag.encode('utf-8') + struct.pack('!' + tag, n)

def bytes_to_int(source):
    size_info = {'B': 1, 'H': 2, 'L': 4, 'Q': 8}
    btag, source = source[:1], source[1:]
    tag = btag.decode('utf-8')
    
    if not size in size_info:
        raise TypeError("Invalid type: {}".format(type(tag)))
    
    size = size_info(tag)

    bnum, source = source[:size], source[size:]
    return struct.unpack('!' + tag, bnum)[0], source
