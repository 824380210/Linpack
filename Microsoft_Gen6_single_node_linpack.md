# reboot all blade to get a clear environment 
```
[root@micro-106 ~]#reboot_rack 192.168.11.48
spawn ssh root@192.168.11.48
root@192.168.11.48's password:
Last login: Wed Apr 24 08:21:39 2019 from 192.168.11.2
WcsCli# wcscli -setpoweroff  -a
Command Success: Blade 1: OFF
Command Success: Blade 2: OFF
Command Success: Blade 3: OFF
Command Success: Blade 4: OFF
Command Success: Blade 5: OFF
Command Success: Blade 6: OFF
Command Success: Blade 7: OFF
Command Success: Blade 8: OFF
Command Success: Blade 9: OFF
Command Success: Blade 10: OFF
Command Success: Blade 11: OFF
Command Success: Blade 12: OFF
Command Success: Blade 13: OFF
Command Success: Blade 14: OFF
Command Success: Blade 15: OFF
Command Success: Blade 16: OFF
Command Success: Blade 17: OFF
Command Success: Blade 18: OFF
Command Success: Blade 19: OFF
Command Success: Blade 20: OFF
Command Success: Blade 21: OFF
Command Success: Blade 22: OFF
Command Success: Blade 23: OFF
Command Success: Blade 24: OFF
Command Success: Blade 25: OFF
Command Success: Blade 26: OFF
Command Success: Blade 27: OFF
Command Success: Blade 28: OFF
Command Success: Blade 29: OFF
Command Success: Blade 30: OFF
Command Success: Blade 31: OFF
Command Success: Blade 32: OFF
Command Success: Blade 33: OFF
Command Success: Blade 34: OFF
Command Success: Blade 35: OFF
Command Success: Blade 36: OFF
Command Success: Blade 37: OFF
Command Success: Blade 38: OFF
Command Success: Blade 39: OFF
Command Success: Blade 40: OFF
Command Success: Blade 41: OFF
Command Success: Blade 42: OFF
Command Success: Blade 43: OFF
Command Success: Blade 44: OFF
Command Success: Blade 45: OFF
Command Success: Blade 46: OFF
Command Success: Blade 47: OFF
Command Success: Blade 48: OFF
WcsCli# wcscli -setpoweron  -a
Command Success: Blade 1: ON
Command Success: Blade 2: ON
Command Success: Blade 3: ON
Command Success: Blade 4: ON
Command Success: Blade 5: ON
Command Success: Blade 6: ON
Command Success: Blade 7: ON
Command Success: Blade 8: ON
Command Success: Blade 9: ON
Command Success: Blade 10: ON
Command Success: Blade 11: ON
Command Success: Blade 12: ON
Command Success: Blade 13: ON
Command Success: Blade 14: ON
Command Success: Blade 15: ON
Command Success: Blade 16: ON
Command Success: Blade 17: ON
Command Success: Blade 18: ON
Command Success: Blade 19: ON
Command Success: Blade 20: ON
Command Success: Blade 21: ON
Command Success: Blade 22: ON
Command Success: Blade 23: ON
Command Success: Blade 24: ON
Command Success: Blade 25: ON
Command Success: Blade 26: ON
Command Success: Blade 27: ON
Command Success: Blade 28: ON
Command Success: Blade 29: ON
Command Success: Blade 30: ON
Command Success: Blade 31: ON
Command Success: Blade 32: ON
Command Success: Blade 33: ON
Command Success: Blade 34: ON
Command Success: Blade 35: ON
Command Success: Blade 36: ON
Command Success: Blade 37: ON
Command Success: Blade 38: ON
Command Success: Blade 39: ON
Command Success: Blade 40: ON
Command Success: Blade 41: ON
Command Success: Blade 42: ON
Command Success: Blade 43: ON
Command Success: Blade 44: ON
Command Success: Blade 45: ON
Command Success: Blade 46: ON
Command Success: Blade 47: ON
Command Success: Blade 48: ON
WcsCli# [root@micro-106 ~]#



```
# scan the network to make sure all blade is up and running with first stage netboot image 
```
[root@micro-106 ~]#nmap -p22 --system-dns 192.168.14.0/24
...
Nmap done: 256 IP addresses (25 hosts up) scanned in 1.83 seconds
# make sure if 25 hosts is up (this rack is 24 blade + 1 management node )

```
# setup the test environment like ssh passwordless ,hostname ,fixed IP ,linpack binary code ,/etc/hosts file sync ,hugepages setup
```
[root@micro-106 ~]#python3.6 read_ms_gen6_rack_info.py
Find MS rack manager IP is 192.168.11.48
b'|    3    |     ON     |   True   |      3     | 28:16:A8:FD:13:DA  |     Success    \r\n|    4    |     ON     |   True   |      4     | 28:16:A8:FD:14:D1  |     Success    \r\n|    5    |     ON     |   True   |      5     | 28:16:A8:FD:17:64  |     Success    \r\n|    6    |     ON     |   True   |      6     | 28:16:A8:FD:17:CB  |     Success    \r\n|    7    |     ON     |   True   |      7     | 28:16:A8:FD:15:D8  |     Success    \r\n|    8    |     ON     |   True   |      8     | 28:16:A8:FD:17:CE  |     Success    \r\n|    9    |     ON     |   True   |      9     | 28:16:A8:FD:14:7A  |     Success    \r\n|   10    |     ON     |   True   |     10     | 28:16:A8:FD:14:9D  |     Success    \r\n|   11    |     ON     |   True   |     11     | 28:16:A8:FD:15:47  |     Success    \r\n|   12    |     ON     |   True   |     12     | 28:16:A8:FD:13:E2  |     Success    \r\n|   13    |     ON     |   True   |     13     | 28:16:A8:FD:13:F0  |     Success    \r\n|   14    |     ON     |   True   |     14     | 28:16:A8:FD:14:76  |     Success    \r\n|   27    |     ON     |   True   |     27     | 28:16:A8:FD:17:2A  |     Success    \r\n|   28    |     ON     |   True   |     28     | 28:16:A8:FD:15:58  |     Success    \r\n|   29    |     ON     |   True   |     29     | 28:16:A8:FD:14:B9  |     Success    \r\n|   30    |     ON     |   True   |     30     | 28:16:A8:FD:15:5C  |     Success    \r\n|   31    |     ON     |   True   |     31     | 28:16:A8:FD:14:AA  |     Success    \r\n|   32    |     ON     |   True   |     32     | 28:16:A8:FD:17:BE  |     Success    \r\n|   33    |     ON     |   True   |     33     | 28:16:A8:FD:15:CC  |     Success    \r\n|   34    |     ON     |   True   |     34     | 28:16:A8:FD:14:68  |     Success    \r\n|   35    |     ON     |   True   |     35     | 28:16:A8:FD:14:61  |     Success    \r\n|   36    |     ON     |   True   |     36     | 28:16:A8:FD:15:62  |     Success    \r\n|   37    |     ON     |   True   |     37     | 28:16:A8:FD:17:77  |     Success    \r\n|   38    |     ON     |   True   |     38     | 28:16:A8:FD:14:D9  |     Success    \r\n'
|    3    |     ON     |   True   |      3     | 28:16:A8:FD:13:DA  |     Success
run passwordless setting on node in Slot 3
verify passwordless seting on node in Slot 3
ip is  192.168.14.187
ssh 192.168.14.187 ls -l /dfcxact/product/common/linpack
ip 192.168.14.187 is passwordless ready
verify node is 1 node
|    4    |     ON     |   True   |      4     | 28:16:A8:FD:14:D1  |     Success
run passwordless setting on node in Slot 4
verify passwordless seting on node in Slot 4
ip is  192.168.14.67
ssh 192.168.14.67 ls -l /dfcxact/product/common/linpack
ip 192.168.14.67 is passwordless ready
verify node is 2 node
|    5    |     ON     |   True   |      5     | 28:16:A8:FD:17:64  |     Success
run passwordless setting on node in Slot 5
verify passwordless seting on node in Slot 5
ip is  192.168.14.93
ssh 192.168.14.93 ls -l /dfcxact/product/common/linpack
ip 192.168.14.93 is passwordless ready
verify node is 3 node
|    6    |     ON     |   True   |      6     | 28:16:A8:FD:17:CB  |     Success
run passwordless setting on node in Slot 6
verify passwordless seting on node in Slot 6
ip is  192.168.14.202
ssh 192.168.14.202 ls -l /dfcxact/product/common/linpack
ip 192.168.14.202 is passwordless ready
verify node is 4 node
|    7    |     ON     |   True   |      7     | 28:16:A8:FD:15:D8  |     Success
run passwordless setting on node in Slot 7
verify passwordless seting on node in Slot 7
ip is  192.168.14.156
ssh 192.168.14.156 ls -l /dfcxact/product/common/linpack
ip 192.168.14.156 is passwordless ready
verify node is 5 node
|    8    |     ON     |   True   |      8     | 28:16:A8:FD:17:CE  |     Success
run passwordless setting on node in Slot 8
verify passwordless seting on node in Slot 8
ip is  192.168.14.108
ssh 192.168.14.108 ls -l /dfcxact/product/common/linpack
ip 192.168.14.108 is passwordless ready
verify node is 6 node
|    9    |     ON     |   True   |      9     | 28:16:A8:FD:14:7A  |     Success
run passwordless setting on node in Slot 9
verify passwordless seting on node in Slot 9
ip is  192.168.14.77
ssh 192.168.14.77 ls -l /dfcxact/product/common/linpack
ip 192.168.14.77 is passwordless ready
verify node is 7 node
|   10    |     ON     |   True   |     10     | 28:16:A8:FD:14:9D  |     Success
run passwordless setting on node in Slot 10
verify passwordless seting on node in Slot 10
ip is  192.168.14.42
ssh 192.168.14.42 ls -l /dfcxact/product/common/linpack
ip 192.168.14.42 is passwordless ready
verify node is 8 node
|   11    |     ON     |   True   |     11     | 28:16:A8:FD:15:47  |     Success
run passwordless setting on node in Slot 11
verify passwordless seting on node in Slot 11
ip is  192.168.14.204
ssh 192.168.14.204 ls -l /dfcxact/product/common/linpack
ip 192.168.14.204 is passwordless ready
verify node is 9 node
|   12    |     ON     |   True   |     12     | 28:16:A8:FD:13:E2  |     Success
run passwordless setting on node in Slot 12
verify passwordless seting on node in Slot 12
ip is  192.168.14.15
ssh 192.168.14.15 ls -l /dfcxact/product/common/linpack
ip 192.168.14.15 is passwordless ready
verify node is 10 node
|   13    |     ON     |   True   |     13     | 28:16:A8:FD:13:F0  |     Success
run passwordless setting on node in Slot 13
verify passwordless seting on node in Slot 13
ip is  192.168.14.157
ssh 192.168.14.157 ls -l /dfcxact/product/common/linpack
ip 192.168.14.157 is passwordless ready
verify node is 11 node
|   14    |     ON     |   True   |     14     | 28:16:A8:FD:14:76  |     Success
run passwordless setting on node in Slot 14
verify passwordless seting on node in Slot 14
ip is  192.168.14.173
ssh 192.168.14.173 ls -l /dfcxact/product/common/linpack
ip 192.168.14.173 is passwordless ready
verify node is 12 node
|   27    |     ON     |   True   |     27     | 28:16:A8:FD:17:2A  |     Success
run passwordless setting on node in Slot 27
verify passwordless seting on node in Slot 27
ip is  192.168.14.200
ssh 192.168.14.200 ls -l /dfcxact/product/common/linpack
ip 192.168.14.200 is passwordless ready
verify node is 13 node
|   28    |     ON     |   True   |     28     | 28:16:A8:FD:15:58  |     Success
run passwordless setting on node in Slot 28
verify passwordless seting on node in Slot 28
ip is  192.168.14.215
ssh 192.168.14.215 ls -l /dfcxact/product/common/linpack
ip 192.168.14.215 is passwordless ready
verify node is 14 node
|   29    |     ON     |   True   |     29     | 28:16:A8:FD:14:B9  |     Success
run passwordless setting on node in Slot 29
verify passwordless seting on node in Slot 29
ip is  192.168.14.34
ssh 192.168.14.34 ls -l /dfcxact/product/common/linpack
ip 192.168.14.34 is passwordless ready
verify node is 15 node
|   30    |     ON     |   True   |     30     | 28:16:A8:FD:15:5C  |     Success
run passwordless setting on node in Slot 30
verify passwordless seting on node in Slot 30
ip is  192.168.14.21
ssh 192.168.14.21 ls -l /dfcxact/product/common/linpack
ip 192.168.14.21 is passwordless ready
verify node is 16 node
|   31    |     ON     |   True   |     31     | 28:16:A8:FD:14:AA  |     Success
run passwordless setting on node in Slot 31
verify passwordless seting on node in Slot 31
ip is  192.168.14.98
ssh 192.168.14.98 ls -l /dfcxact/product/common/linpack
ip 192.168.14.98 is passwordless ready
verify node is 17 node
|   32    |     ON     |   True   |     32     | 28:16:A8:FD:17:BE  |     Success
run passwordless setting on node in Slot 32
verify passwordless seting on node in Slot 32
ip is  192.168.14.70
ssh 192.168.14.70 ls -l /dfcxact/product/common/linpack
ip 192.168.14.70 is passwordless ready
verify node is 18 node
|   33    |     ON     |   True   |     33     | 28:16:A8:FD:15:CC  |     Success
run passwordless setting on node in Slot 33
verify passwordless seting on node in Slot 33
ip is  192.168.14.19
ssh 192.168.14.19 ls -l /dfcxact/product/common/linpack
ip 192.168.14.19 is passwordless ready
verify node is 19 node
|   34    |     ON     |   True   |     34     | 28:16:A8:FD:14:68  |     Success
run passwordless setting on node in Slot 34
verify passwordless seting on node in Slot 34
ip is  192.168.14.214
ssh 192.168.14.214 ls -l /dfcxact/product/common/linpack
ip 192.168.14.214 is passwordless ready
verify node is 20 node
|   35    |     ON     |   True   |     35     | 28:16:A8:FD:14:61  |     Success
run passwordless setting on node in Slot 35
verify passwordless seting on node in Slot 35
ip is  192.168.14.107
ssh 192.168.14.107 ls -l /dfcxact/product/common/linpack
ip 192.168.14.107 is passwordless ready
verify node is 21 node
|   36    |     ON     |   True   |     36     | 28:16:A8:FD:15:62  |     Success
run passwordless setting on node in Slot 36
verify passwordless seting on node in Slot 36
ip is  192.168.14.158
ssh 192.168.14.158 ls -l /dfcxact/product/common/linpack
ip 192.168.14.158 is passwordless ready
verify node is 22 node
|   37    |     ON     |   True   |     37     | 28:16:A8:FD:17:77  |     Success
run passwordless setting on node in Slot 37
verify passwordless seting on node in Slot 37
ip is  192.168.14.74
ssh 192.168.14.74 ls -l /dfcxact/product/common/linpack
ip 192.168.14.74 is passwordless ready
verify node is 23 node
|   38    |     ON     |   True   |     38     | 28:16:A8:FD:14:D9  |     Success
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
ssh  192.168.14.187  "   if ! ip a | grep 172.30.101.1; then   ip addr  add dev eth0 172.30.101.1/16 ;fi"
host 172.30.101.1 setting ok
the compute node hostname is node02.cluster
ssh  192.168.14.67  "   if ! ip a | grep 172.30.101.2; then   ip addr  add dev eth0 172.30.101.2/16 ;fi"
host 172.30.101.2 setting ok
the compute node hostname is node03.cluster
ssh  192.168.14.93  "   if ! ip a | grep 172.30.101.3; then   ip addr  add dev eth0 172.30.101.3/16 ;fi"
host 172.30.101.3 setting ok
the compute node hostname is node04.cluster
ssh  192.168.14.202  "   if ! ip a | grep 172.30.101.4; then   ip addr  add dev eth0 172.30.101.4/16 ;fi"
host 172.30.101.4 setting ok
the compute node hostname is node05.cluster
ssh  192.168.14.156  "   if ! ip a | grep 172.30.101.5; then   ip addr  add dev eth0 172.30.101.5/16 ;fi"
host 172.30.101.5 setting ok
the compute node hostname is node06.cluster
ssh  192.168.14.108  "   if ! ip a | grep 172.30.101.6; then   ip addr  add dev eth0 172.30.101.6/16 ;fi"
host 172.30.101.6 setting ok
the compute node hostname is node07.cluster
ssh  192.168.14.77  "   if ! ip a | grep 172.30.101.7; then   ip addr  add dev eth0 172.30.101.7/16 ;fi"
host 172.30.101.7 setting ok
the compute node hostname is node08.cluster
ssh  192.168.14.42  "   if ! ip a | grep 172.30.101.8; then   ip addr  add dev eth0 172.30.101.8/16 ;fi"
host 172.30.101.8 setting ok
the compute node hostname is node09.cluster
ssh  192.168.14.204  "   if ! ip a | grep 172.30.101.9; then   ip addr  add dev eth0 172.30.101.9/16 ;fi"
host 172.30.101.9 setting ok
the compute node hostname is node10.cluster
ssh  192.168.14.15  "   if ! ip a | grep 172.30.101.10; then   ip addr  add dev eth0 172.30.101.10/16 ;fi"
host 172.30.101.10 setting ok
the compute node hostname is node11.cluster
ssh  192.168.14.157  "   if ! ip a | grep 172.30.101.11; then   ip addr  add dev eth0 172.30.101.11/16 ;fi"
host 172.30.101.11 setting ok
the compute node hostname is node12.cluster
ssh  192.168.14.173  "   if ! ip a | grep 172.30.101.12; then   ip addr  add dev eth0 172.30.101.12/16 ;fi"
host 172.30.101.12 setting ok
the compute node hostname is node13.cluster
ssh  192.168.14.200  "   if ! ip a | grep 172.30.101.13; then   ip addr  add dev eth0 172.30.101.13/16 ;fi"
host 172.30.101.13 setting ok
the compute node hostname is node14.cluster
ssh  192.168.14.215  "   if ! ip a | grep 172.30.101.14; then   ip addr  add dev eth0 172.30.101.14/16 ;fi"
host 172.30.101.14 setting ok
the compute node hostname is node15.cluster
ssh  192.168.14.34  "   if ! ip a | grep 172.30.101.15; then   ip addr  add dev eth0 172.30.101.15/16 ;fi"
host 172.30.101.15 setting ok
the compute node hostname is node16.cluster
ssh  192.168.14.21  "   if ! ip a | grep 172.30.101.16; then   ip addr  add dev eth0 172.30.101.16/16 ;fi"
host 172.30.101.16 setting ok
the compute node hostname is node17.cluster
ssh  192.168.14.98  "   if ! ip a | grep 172.30.101.17; then   ip addr  add dev eth0 172.30.101.17/16 ;fi"
host 172.30.101.17 setting ok
the compute node hostname is node18.cluster
ssh  192.168.14.70  "   if ! ip a | grep 172.30.101.18; then   ip addr  add dev eth0 172.30.101.18/16 ;fi"
host 172.30.101.18 setting ok
the compute node hostname is node19.cluster
ssh  192.168.14.19  "   if ! ip a | grep 172.30.101.19; then   ip addr  add dev eth0 172.30.101.19/16 ;fi"
host 172.30.101.19 setting ok
the compute node hostname is node20.cluster
ssh  192.168.14.214  "   if ! ip a | grep 172.30.101.20; then   ip addr  add dev eth0 172.30.101.20/16 ;fi"
host 172.30.101.20 setting ok
the compute node hostname is node21.cluster
ssh  192.168.14.107  "   if ! ip a | grep 172.30.101.21; then   ip addr  add dev eth0 172.30.101.21/16 ;fi"
host 172.30.101.21 setting ok
the compute node hostname is node22.cluster
ssh  192.168.14.158  "   if ! ip a | grep 172.30.101.22; then   ip addr  add dev eth0 172.30.101.22/16 ;fi"
host 172.30.101.22 setting ok
the compute node hostname is node23.cluster
ssh  192.168.14.74  "   if ! ip a | grep 172.30.101.23; then   ip addr  add dev eth0 172.30.101.23/16 ;fi"
host 172.30.101.23 setting ok
the compute node hostname is node24.cluster
ssh  192.168.14.10  "   if ! ip a | grep 172.30.101.24; then   ip addr  add dev eth0 172.30.101.24/16 ;fi"
host 172.30.101.24 setting ok


```
# some test step no implemetion on the python code (will do later )
```
[root@micro-106 ~]#pdsh -w 172.30.101.[1-24] "cd /root; tar zxvf /dfcxact/product/common/linpack/HPL.tgz"
[root@micro-106 ~]#pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/hosts /etc/"
[root@micro-106 ~]# pdsh -w 172.30.101.[1-24] "echo 92 > /sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages"
[root@micro-106 ~]# pdsh -w 172.30.101.[1-24] "echo 92 > /sys/devices/system/node/node1/hugepages/hugepages-1048576kB/nr_hugepages"
[root@micro-106 ~]# pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/HPL.dat /root/HPL/"

```
# run linpack on node
```
[root@node01 HPL]# history
    1    tar zxvf /dfcxact/product/common/linpack/ssh_keys.tgz -C /root/.ssh/
    2  exit
    3  cat /dfcxact/product/common/linpack/peter/cluster/NB_Value_24
    4  exit
    5  cd HPL/
    6  bash run_smp_24
    7  history
[root@node01 HPL]# cat run_smp_24
PATH=$PATH:/root/HPL:
export LD_LIBRARY_PATH=/root/HPL

export I_MPI_FALLBACK=disable
export I_MPI_FABRICS=shm:tcp
export HPL_HWPREFETCH=1
export HNAME=`hostname`
mpirun -genvall -np 48 -ppn 2 -f hostfile  -genv I_MPI_NETMASK  eth0  /root/HPL/run_TLP_sky  | tee -a /dfcxact/product/common/linpack/24node_${HNAME}_20190424.log

[root@node01 HPL]#


```
# Test result for reference 
```
 99.78  706176   0.068   0.000   0.000   0.072    2.23   4579      0  25.38      31.63   65272.92  65.8   8.3  76 3.178 2.394 node16[31,3,7]
 99.84  706560   0.076   0.001   0.000   0.080    1.48   3924      0  50.19      17.05   65268.87  63.8   8.7  76 3.281 2.394 node17[32,4,0]
 99.89  706944   0.081   0.000   0.000   0.085    0.93   4753      0  43.05       8.04   65269.12  66.5   8.5  77 3.184 2.394 node21[41,5,1]
 99.95  707328   0.053   0.000   0.000   0.057    0.71   4053      0  48.89       4.00   65266.31  56.8   7.9  71 3.291 2.394 node02[2,0,2]
Peak Performance =   67313.31 GFlops /  1402.36 GFlops per node
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR00L2L4      707712   384     6     8            3621.21            6.52569e+04
HPL_pdgesv() start time Wed Apr 24 00:50:17 2019

HPL_pdgesv() end time   Wed Apr 24 01:50:38 2019

        HPL Efficiency by CPU Cycle   76.624%
        HPL Efficiency by BUS Cycle   65.908%
--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=        0.0017256 ...... PASSED
================================================================================

Finished      1 tests with the following results:
              1 tests completed and passed residual checks,
              0 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.
================================================================================


```
