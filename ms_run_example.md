# ms example 
#
```
[root@micro-106 ~]#python3.6 read_ms_gen6_rack_info.py
Find MS rack manager IP is 192.168.11.48
b'|    3    |     ON     |   True   |      3     | 28:16:A8:FD:13:DA  |     Success    \r\n|    4    |     ON     |   True   |      4     | 28:16:A8:FD:14:D1  |     Success    \r\n|    5    |     ON     |   True   |      5     | 28:16:A8:FD:17:64  |     Success    \r\n|    6    |     ON     |   True   |      6     | 28:16:A8:FD:17:CB  |     Success    \r\n|    7    |     ON     |   True   |      7     | 28:16:A8:FD:15:D8  |     Success    \r\n|    8    |     ON     |   True   |      8     | 28:16:A8:FD:17:CE  |     Success    \r\n|    9    |     ON     |   True   |      9     | 28:16:A8:FD:14:7A  |     Success    \r\n|   10    |     ON     |   True   |     10     | 28:16:A8:FD:14:9D  |     Success    \r\n|   11    |     ON     |   True   |     11     | 28:16:A8:FD:15:47  |     Success    \r\n|   12    |     ON     |   True   |     12     | 28:16:A8:FD:13:E2  |     Success    \r\n|   13    |     ON     |   True   |     13     | 28:16:A8:FD:13:F0  |     Success    \r\n|   14    |     ON     |   True   |     14     | 28:16:A8:FD:14:76  |     Success    \r\n|   27    |     ON     |   True   |     27     | 28:16:A8:FD:17:2A  |     Success    \r\n|   28    |     ON     |   True   |     28     | 28:16:A8:FD:15:58  |     Success    \r\n|   29    |     ON     |   True   |     29     | 28:16:A8:FD:14:B9  |     Success    \r\n|   30    |     ON     |   True   |     30     | 28:16:A8:FD:15:5C  |     Success    \r\n|   31    |     ON     |   True   |     31     | 28:16:A8:FD:14:AA  |     Success    \r\n|   32    |     ON     |   True   |     32     | 28:16:A8:FD:17:BE  |     Success    \r\n|   33    |     ON     |   True   |     33     | 28:16:A8:FD:15:CC  |     Success    \r\n|   34    |     ON     |   True   |     34     | 28:16:A8:FD:14:68  |     Success    \r\n|   35    |     ON     |   True   |     35     | 28:16:A8:FD:14:61  |     Success    \r\n|   36    |     ON     |   True   |     36     | 28:16:A8:FD:15:62  |     Success    \r\n|   37    |     ON     |   True   |     37     | 28:16:A8:FD:17:77  |     Success    \r\n|   38    |     ON     |   True   |     38     | 28:16:A8:FD:14:D9  |     Success    \r\n'
|    3    |     ON     |   True   |      3     | 28:16:A8:FD:13:DA  |     Success
slot id is 3 and IP is 192.168.14.187
run passwordless setting on node in Slot 3
verify passwordless seting on node in Slot 3
ip is  192.168.14.187
ssh 192.168.14.187 ls -l /dfcxact/product/common/linpack
ip 192.168.14.187 is passwordless ready
verify node is 1 node
|    4    |     ON     |   True   |      4     | 28:16:A8:FD:14:D1  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
run passwordless setting on node in Slot 4
verify passwordless seting on node in Slot 4
ip is  192.168.14.67
ssh 192.168.14.67 ls -l /dfcxact/product/common/linpack
ip 192.168.14.67 is passwordless ready
verify node is 2 node
|    5    |     ON     |   True   |      5     | 28:16:A8:FD:17:64  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
run passwordless setting on node in Slot 5
verify passwordless seting on node in Slot 5
ip is  192.168.14.93
ssh 192.168.14.93 ls -l /dfcxact/product/common/linpack
ip 192.168.14.93 is passwordless ready
verify node is 3 node
|    6    |     ON     |   True   |      6     | 28:16:A8:FD:17:CB  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
run passwordless setting on node in Slot 6
verify passwordless seting on node in Slot 6
ip is  192.168.14.202
ssh 192.168.14.202 ls -l /dfcxact/product/common/linpack
ip 192.168.14.202 is passwordless ready
verify node is 4 node
|    7    |     ON     |   True   |      7     | 28:16:A8:FD:15:D8  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
run passwordless setting on node in Slot 7
verify passwordless seting on node in Slot 7
ip is  192.168.14.156
ssh 192.168.14.156 ls -l /dfcxact/product/common/linpack
ip 192.168.14.156 is passwordless ready
verify node is 5 node
|    8    |     ON     |   True   |      8     | 28:16:A8:FD:17:CE  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
run passwordless setting on node in Slot 8
verify passwordless seting on node in Slot 8
ip is  192.168.14.108
ssh 192.168.14.108 ls -l /dfcxact/product/common/linpack
ip 192.168.14.108 is passwordless ready
verify node is 6 node
|    9    |     ON     |   True   |      9     | 28:16:A8:FD:14:7A  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
run passwordless setting on node in Slot 9
verify passwordless seting on node in Slot 9
ip is  192.168.14.77
ssh 192.168.14.77 ls -l /dfcxact/product/common/linpack
ip 192.168.14.77 is passwordless ready
verify node is 7 node
|   10    |     ON     |   True   |     10     | 28:16:A8:FD:14:9D  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
run passwordless setting on node in Slot 10
verify passwordless seting on node in Slot 10
ip is  192.168.14.42
ssh 192.168.14.42 ls -l /dfcxact/product/common/linpack
ip 192.168.14.42 is passwordless ready
verify node is 8 node
|   11    |     ON     |   True   |     11     | 28:16:A8:FD:15:47  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
run passwordless setting on node in Slot 11
verify passwordless seting on node in Slot 11
ip is  192.168.14.204
ssh 192.168.14.204 ls -l /dfcxact/product/common/linpack
ip 192.168.14.204 is passwordless ready
verify node is 9 node
|   12    |     ON     |   True   |     12     | 28:16:A8:FD:13:E2  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
run passwordless setting on node in Slot 12
verify passwordless seting on node in Slot 12
ip is  192.168.14.15
ssh 192.168.14.15 ls -l /dfcxact/product/common/linpack
ip 192.168.14.15 is passwordless ready
verify node is 10 node
|   13    |     ON     |   True   |     13     | 28:16:A8:FD:13:F0  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
run passwordless setting on node in Slot 13
verify passwordless seting on node in Slot 13
ip is  192.168.14.157
ssh 192.168.14.157 ls -l /dfcxact/product/common/linpack
ip 192.168.14.157 is passwordless ready
verify node is 11 node
|   14    |     ON     |   True   |     14     | 28:16:A8:FD:14:76  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
run passwordless setting on node in Slot 14
verify passwordless seting on node in Slot 14
ip is  192.168.14.173
ssh 192.168.14.173 ls -l /dfcxact/product/common/linpack
ip 192.168.14.173 is passwordless ready
verify node is 12 node
|   27    |     ON     |   True   |     27     | 28:16:A8:FD:17:2A  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
slot id is 27 and IP is 192.168.14.200
run passwordless setting on node in Slot 27
verify passwordless seting on node in Slot 27
ip is  192.168.14.200
ssh 192.168.14.200 ls -l /dfcxact/product/common/linpack
ip 192.168.14.200 is passwordless ready
verify node is 13 node
|   28    |     ON     |   True   |     28     | 28:16:A8:FD:15:58  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
slot id is 27 and IP is 192.168.14.200
slot id is 28 and IP is 192.168.14.215
run passwordless setting on node in Slot 28
verify passwordless seting on node in Slot 28
ip is  192.168.14.215
ssh 192.168.14.215 ls -l /dfcxact/product/common/linpack
ip 192.168.14.215 is passwordless ready
verify node is 14 node
|   29    |     ON     |   True   |     29     | 28:16:A8:FD:14:B9  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
slot id is 27 and IP is 192.168.14.200
slot id is 28 and IP is 192.168.14.215
slot id is 29 and IP is 192.168.14.34
run passwordless setting on node in Slot 29
verify passwordless seting on node in Slot 29
ip is  192.168.14.34
ssh 192.168.14.34 ls -l /dfcxact/product/common/linpack
ip 192.168.14.34 is passwordless ready
verify node is 15 node
|   30    |     ON     |   True   |     30     | 28:16:A8:FD:15:5C  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
slot id is 27 and IP is 192.168.14.200
slot id is 28 and IP is 192.168.14.215
slot id is 29 and IP is 192.168.14.34
slot id is 30 and IP is 192.168.14.21
run passwordless setting on node in Slot 30
verify passwordless seting on node in Slot 30
ip is  192.168.14.21
ssh 192.168.14.21 ls -l /dfcxact/product/common/linpack
ip 192.168.14.21 is passwordless ready
verify node is 16 node
|   31    |     ON     |   True   |     31     | 28:16:A8:FD:14:AA  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
slot id is 27 and IP is 192.168.14.200
slot id is 28 and IP is 192.168.14.215
slot id is 29 and IP is 192.168.14.34
slot id is 30 and IP is 192.168.14.21
slot id is 31 and IP is 192.168.14.98
run passwordless setting on node in Slot 31
verify passwordless seting on node in Slot 31
ip is  192.168.14.98
ssh 192.168.14.98 ls -l /dfcxact/product/common/linpack
ip 192.168.14.98 is passwordless ready
verify node is 17 node
|   32    |     ON     |   True   |     32     | 28:16:A8:FD:17:BE  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
slot id is 27 and IP is 192.168.14.200
slot id is 28 and IP is 192.168.14.215
slot id is 29 and IP is 192.168.14.34
slot id is 30 and IP is 192.168.14.21
slot id is 31 and IP is 192.168.14.98
slot id is 32 and IP is 192.168.14.70
run passwordless setting on node in Slot 32
verify passwordless seting on node in Slot 32
ip is  192.168.14.70
ssh 192.168.14.70 ls -l /dfcxact/product/common/linpack
ip 192.168.14.70 is passwordless ready
verify node is 18 node
|   33    |     ON     |   True   |     33     | 28:16:A8:FD:15:CC  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
slot id is 27 and IP is 192.168.14.200
slot id is 28 and IP is 192.168.14.215
slot id is 29 and IP is 192.168.14.34
slot id is 30 and IP is 192.168.14.21
slot id is 31 and IP is 192.168.14.98
slot id is 32 and IP is 192.168.14.70
slot id is 33 and IP is 192.168.14.19
run passwordless setting on node in Slot 33
verify passwordless seting on node in Slot 33
ip is  192.168.14.19
ssh 192.168.14.19 ls -l /dfcxact/product/common/linpack
ip 192.168.14.19 is passwordless ready
verify node is 19 node
|   34    |     ON     |   True   |     34     | 28:16:A8:FD:14:68  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
slot id is 27 and IP is 192.168.14.200
slot id is 28 and IP is 192.168.14.215
slot id is 29 and IP is 192.168.14.34
slot id is 30 and IP is 192.168.14.21
slot id is 31 and IP is 192.168.14.98
slot id is 32 and IP is 192.168.14.70
slot id is 33 and IP is 192.168.14.19
slot id is 34 and IP is 192.168.14.214
run passwordless setting on node in Slot 34
verify passwordless seting on node in Slot 34
ip is  192.168.14.214
ssh 192.168.14.214 ls -l /dfcxact/product/common/linpack
ip 192.168.14.214 is passwordless ready
verify node is 20 node
|   35    |     ON     |   True   |     35     | 28:16:A8:FD:14:61  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
slot id is 27 and IP is 192.168.14.200
slot id is 28 and IP is 192.168.14.215
slot id is 29 and IP is 192.168.14.34
slot id is 30 and IP is 192.168.14.21
slot id is 31 and IP is 192.168.14.98
slot id is 32 and IP is 192.168.14.70
slot id is 33 and IP is 192.168.14.19
slot id is 34 and IP is 192.168.14.214
slot id is 35 and IP is 192.168.14.107
run passwordless setting on node in Slot 35
verify passwordless seting on node in Slot 35
ip is  192.168.14.107
ssh 192.168.14.107 ls -l /dfcxact/product/common/linpack
ip 192.168.14.107 is passwordless ready
verify node is 21 node
|   36    |     ON     |   True   |     36     | 28:16:A8:FD:15:62  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
slot id is 27 and IP is 192.168.14.200
slot id is 28 and IP is 192.168.14.215
slot id is 29 and IP is 192.168.14.34
slot id is 30 and IP is 192.168.14.21
slot id is 31 and IP is 192.168.14.98
slot id is 32 and IP is 192.168.14.70
slot id is 33 and IP is 192.168.14.19
slot id is 34 and IP is 192.168.14.214
slot id is 35 and IP is 192.168.14.107
slot id is 36 and IP is 192.168.14.158
run passwordless setting on node in Slot 36
verify passwordless seting on node in Slot 36
ip is  192.168.14.158
ssh 192.168.14.158 ls -l /dfcxact/product/common/linpack
ip 192.168.14.158 is passwordless ready
verify node is 22 node
|   37    |     ON     |   True   |     37     | 28:16:A8:FD:17:77  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
slot id is 27 and IP is 192.168.14.200
slot id is 28 and IP is 192.168.14.215
slot id is 29 and IP is 192.168.14.34
slot id is 30 and IP is 192.168.14.21
slot id is 31 and IP is 192.168.14.98
slot id is 32 and IP is 192.168.14.70
slot id is 33 and IP is 192.168.14.19
slot id is 34 and IP is 192.168.14.214
slot id is 35 and IP is 192.168.14.107
slot id is 36 and IP is 192.168.14.158
slot id is 37 and IP is 192.168.14.74
run passwordless setting on node in Slot 37
verify passwordless seting on node in Slot 37
ip is  192.168.14.74
ssh 192.168.14.74 ls -l /dfcxact/product/common/linpack
ip 192.168.14.74 is passwordless ready
verify node is 23 node
|   38    |     ON     |   True   |     38     | 28:16:A8:FD:14:D9  |     Success
slot id is 3 and IP is 192.168.14.187
slot id is 4 and IP is 192.168.14.67
slot id is 5 and IP is 192.168.14.93
slot id is 6 and IP is 192.168.14.202
slot id is 7 and IP is 192.168.14.156
slot id is 8 and IP is 192.168.14.108
slot id is 9 and IP is 192.168.14.77
slot id is 10 and IP is 192.168.14.42
slot id is 11 and IP is 192.168.14.204
slot id is 12 and IP is 192.168.14.15
slot id is 13 and IP is 192.168.14.157
slot id is 14 and IP is 192.168.14.173
slot id is 27 and IP is 192.168.14.200
slot id is 28 and IP is 192.168.14.215
slot id is 29 and IP is 192.168.14.34
slot id is 30 and IP is 192.168.14.21
slot id is 31 and IP is 192.168.14.98
slot id is 32 and IP is 192.168.14.70
slot id is 33 and IP is 192.168.14.19
slot id is 34 and IP is 192.168.14.214
slot id is 35 and IP is 192.168.14.107
slot id is 36 and IP is 192.168.14.158
slot id is 37 and IP is 192.168.14.74
slot id is 38 and IP is 192.168.14.10
run passwordless setting on node in Slot 38
verify passwordless seting on node in Slot 38
ip is  192.168.14.10
ssh 192.168.14.10 ls -l /dfcxact/product/common/linpack
ip 192.168.14.10 is passwordless ready
verify node is 24 node

ID is 3 and IP is 192.168.14.187
ID is 4 and IP is 192.168.14.67
ID is 5 and IP is 192.168.14.93
ID is 6 and IP is 192.168.14.202
ID is 7 and IP is 192.168.14.156
ID is 8 and IP is 192.168.14.108
ID is 9 and IP is 192.168.14.77
ID is 10 and IP is 192.168.14.42
ID is 11 and IP is 192.168.14.204
ID is 12 and IP is 192.168.14.15
ID is 13 and IP is 192.168.14.157
ID is 14 and IP is 192.168.14.173
ID is 27 and IP is 192.168.14.200
ID is 28 and IP is 192.168.14.215
ID is 29 and IP is 192.168.14.34
ID is 30 and IP is 192.168.14.21
ID is 31 and IP is 192.168.14.98
ID is 32 and IP is 192.168.14.70
ID is 33 and IP is 192.168.14.19
ID is 34 and IP is 192.168.14.214
ID is 35 and IP is 192.168.14.107
ID is 36 and IP is 192.168.14.158
ID is 37 and IP is 192.168.14.74
ID is 38 and IP is 192.168.14.10
the compute node hostname is node01.cluster
host 172.30.101.1 setting ok
the compute node hostname is node02.cluster
host 172.30.101.2 setting ok
the compute node hostname is node03.cluster
host 172.30.101.3 setting ok
the compute node hostname is node04.cluster
host 172.30.101.4 setting ok
the compute node hostname is node05.cluster
host 172.30.101.5 setting ok
the compute node hostname is node06.cluster
host 172.30.101.6 setting ok
the compute node hostname is node07.cluster
host 172.30.101.7 setting ok
the compute node hostname is node08.cluster
host 172.30.101.8 setting ok
the compute node hostname is node09.cluster
host 172.30.101.9 setting ok
the compute node hostname is node10.cluster
host 172.30.101.10 setting ok
the compute node hostname is node11.cluster
host 172.30.101.11 setting ok
the compute node hostname is node12.cluster
host 172.30.101.12 setting ok
the compute node hostname is node13.cluster
host 172.30.101.13 setting ok
the compute node hostname is node14.cluster
host 172.30.101.14 setting ok
the compute node hostname is node15.cluster
host 172.30.101.15 setting ok
the compute node hostname is node16.cluster
host 172.30.101.16 setting ok
the compute node hostname is node17.cluster
host 172.30.101.17 setting ok
the compute node hostname is node18.cluster
host 172.30.101.18 setting ok
the compute node hostname is node19.cluster
host 172.30.101.19 setting ok
the compute node hostname is node20.cluster
host 172.30.101.20 setting ok
the compute node hostname is node21.cluster
host 172.30.101.21 setting ok
the compute node hostname is node22.cluster
host 172.30.101.22 setting ok
the compute node hostname is node23.cluster
host 172.30.101.23 setting ok
the compute node hostname is node24.cluster
host 172.30.101.24 setting ok
[root@micro-106 ~]#diff read_ms_gen6_rack_info.py ms_20190423.py
89,93c89,90
<         if "28:16" in line:
<             ip,mac  = line.split()
<             new_ip  = ip.strip()
<             new_mac = mac.strip()
<             mac2ip[new_mac] = new_ip
---
>         ip,mac = line.split()
>         mac2ip[mac] = ip
[root@micro-106 ~]#

```
