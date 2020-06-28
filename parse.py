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
from bitstring import BitArray

fileToRead = "./example-packets"
"""
Raw bytestring of message:
\xd4\xc3\xb2\xa1\x02\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x9c\xbc\xf7^OY\n\x008\x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x00*\xce\xed@\x00@\x11m\xd3\x7f\x00\x00\x01\x7f\x00\x00\x01\xda\xe7N!\x00\x16\xfe)Hello friend!\n\x9c\xbc\xf7^mZ\n\x00:\x00\x00\x00:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x00,\xce\xee@\x00@\x11m\xd0\x7f\x00\x00\x01\x7f\x00\x00\x01N!\xda\xe7\x00\x18\xfe+Hello UDP Client

bytes read: 170 (1360 bits)

### Header ###
ID: 0xd4c3
QR: 1           ---> query, not reply
Opcode: 0x6
"""

class Header:
    def __init__(self):
        self.ID = []
        """
        A 16 bit identifier assigned by the program that generates any kind
        of query.  This identifier is copied the corresponding reply
        and can be used by the requester to match up replies
        to outstanding queries.
        """

        self.QR = False
        """
        A one bit field that specifies whether this message is a query (0),
        or a response (1).
        """

        self.Opcode = 0
        """
        A four bit field that specifies kind of query in this
        message.  This value is set by the originator of a query
        and copied into the response.  The values are:

        0               a standard query (QUERY)

        1               an inverse query (IQUERY)

        2               a server status request (STATUS)

        3-15            reserved for future use
        """

        self.AA = False
        self.TC = False
        self.RC = False
        self.RA = False
        self.Z = False
        self.RCODE = False
        self.QDCOUNT = []
        self.ANCOUNT = []
        self.NSCOUNT = []
        self.ARCOUNT = []
    def __repr__(self):
        return f"""
            QR: {self.QR}
            Opcode: {self.Opcode}
            AA: {self.AA}
            TC: {self.TC}
            RC: {self.RC}
            RA: {self.RA}
            Z: {self.Z}
            RCODE: {self.RCODE}
            QDCOUNT: {self.QDCOUNT}
            ANCOUNT: {self.ANCOUNT}
            NSCOUNT: {self.NSCOUNT}
        """

class DnsMessage:
    def __init__(self):
        # number of bytes in packet
        self.count = 0
        self.header = Header()
    def __repr__(self):
        return f"""{self.count} bit message ({self.header.ID}):
            {self.header}
        """


def parseMessage(location):
    count = 0
    message = DnsMessage()
    bits = None
    with open(fileToRead, "rb") as f:
        bits = BitArray(f)
    message.count = len(bits)

    # parse header
    message.header.ID = bits[0:16]
    message.header.QR = bits[16]
    message.header.Opcode = (bits[17:21]).int

    return message

m = parseMessage(fileToRead)
print(m)
