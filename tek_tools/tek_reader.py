# Copyright 2017 Hendrik Soehnholz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tek Tools

Read data from Tektronix oscilloscopes

H. Soehnholz
Initial version: 2014-04-25
"""

import struct
import numpy as np


def load(filename, wordvalues=False, signed=False):
    """Read data from binary Tek oscilloscope file"""

    # open file and read data
    datafile = open(filename, 'rb')  # read binary
    buf = datafile.read()
    datafile.close()

#    print len(buf)

    # find start of header/data
    i = 0
    for i in range(len(buf)):
        data = struct.unpack_from('B', buf, i)
        if data[0] == ord('#'):
            break

    # get number of data points
    i += 1
    data = struct.unpack_from('c', buf, i)
    nbytes = int(data[0])  # number of bytes for specifying data set size

    i += 1
    data = struct.unpack_from('c' * nbytes, buf, i)
    npoints_string = ''
    for j in range(len(data)):
        npoints_string += data[j].decode()
    npoints = int(npoints_string)
#    print "npoints = ", npoints

    if wordvalues:
        # read 16-bit data

        i += nbytes

        if signed:
            data = struct.unpack_from('>' + 'h' * (npoints / 2), buf, i)
            data_final = np.array(data) >> 8
        else:
            data = struct.unpack_from('>' + 'H' * (npoints / 2), buf, i)
            data_final = np.array(data) >> 8

    else:
        # read 8-bit data (default)

        i += nbytes

        if signed:
            data = struct.unpack_from('b' * npoints, buf, i)
            data_final = np.array(data)
        else:
            data = struct.unpack_from('B' * npoints, buf, i)
            data_final = np.array(data)

    i += npoints
    endbyte = struct.unpack_from('c', buf, i)
    if ord(endbyte[0]) != 0x0a:
        print("Error: number of data points doesn't match file size!")
        return -1

    return data_final
