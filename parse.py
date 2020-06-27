"""
DNS message parsing.

See DNS message format definition in section 4.1 of the official protocol:
https://tools.ietf.org/html/rfc1035

All communications inside of the domain protocol are carried in a single
format called a message.  The top level format of message is divided
into 5 sections (some of which are empty in certain cases) shown below:

    +---------------------+
    |        Header       |
    +---------------------+
    |       Question      | the question for the name server
    +---------------------+
    |        Answer       | RRs answering the question
    +---------------------+
    |      Authority      | RRs pointing toward an authority
    +---------------------+
    |      Additional     | RRs holding additional information
    +---------------------+


The header contains the following fields:

                                1  1  1  1  1  1
  0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                      ID                       |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|QR|   Opcode  |AA|TC|RD|RA|   Z    |   RCODE   |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    QDCOUNT                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    ANCOUNT                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    NSCOUNT                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    ARCOUNT                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
"""

fileToRead = "./example-packets"

class Header:
    def __init__(self):
        self.id = []
        self.QR = 0
        self.Opcode = 0
        self.AA = 0
        self.TC = 0
        self.RC = 0
        self.RA = 0
        self.Z = 0
        self.RCODE = 0
        self.QDCOUNT = []
        self.ANCOUNT = []
        self.NSCOUNT = []
        self.ARCOUNT = []

class DnsMessage:
    def __init__(self):
        # number of bytes in packet
        self.count = 0
        self.header = Header()


def parseMessage(location):
    count = 0
    message = DnsMessage()
    bytes = []
    with open(fileToRead, "rb") as f:
        bytes = f.read()
    message.count = len(bytes)
    print(bytes)

    # parse header
    message.header.id = bytes[0:16]
    # message.header.qr =

    return message

p = parseMessage(fileToRead)
print(f'bytes read: {p.count}')
print(f'header id: {p.header.id}')

"""
Raw bytestring of message:
\xd4\xc3\xb2\xa1\x02\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x9c\xbc\xf7^OY\n\x008\x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x00*\xce\xed@\x00@\x11m\xd3\x7f\x00\x00\x01\x7f\x00\x00\x01\xda\xe7N!\x00\x16\xfe)Hello friend!\n\x9c\xbc\xf7^mZ\n\x00:\x00\x00\x00:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x00,\xce\xee@\x00@\x11m\xd0\x7f\x00\x00\x01\x7f\x00\x00\x01N!\xda\xe7\x00\x18\xfe+Hello UDP Client


bytes read: 170

"""
