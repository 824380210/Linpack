# Microsoft Gen 6 Rack linpack test step for reference 
#
#
#### determine the interface that connect to the Gen 6 rack 
```
[root@micro-106 linpack]#ibdev2netdev
mlx4_0 port 1 ==> eth6 (Up)
mlx4_0 port 2 ==> eth7 (Down)
```
#### determine the linpack IP for management node (remove first if have been config ,then config in case MFG use another port for rack test 
```
[root@micro-106 linpack]#ip addr show dev eth6
10: eth6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
    link/ether 24:8a:07:63:05:81 brd ff:ff:ff:ff:ff:ff
    inet 192.168.14.2/24 brd 192.168.14.255 scope global eth6
    inet 172.30.0.1/16 brd 172.30.255.255 scope global eth6
    inet6 fe80::268a:7ff:fe63:581/64 scope link
       valid_lft forever preferred_lft forever

[root@micro-106 linpack]#ip a | grep 172.30
    inet 172.30.0.1/16 brd 172.30.255.255 scope global eth6

[root@micro-106 linpack]#ip addr del dev eth6 172.30.0.1/16


``` 

#### scan the dhcp.lease file or arp tables to find the rack manager 
```

ot@mfg-l1-4nl3 ~]# arp | grep 'f0:1d:bc'
192.168.11.197           ether   f0:1d:bc:fd:10:22   C                     eth1
[root@mfg-l1-4nl3 ~]# arp | grep 'f0:1d:bc' | awk '{print $1}' | head -n 1
192.168.11.197


```
#### ssh to rack manager to get the compute node slot ID to mac address mapping (table 1 )
```
|   31    |     ON     |   True   |     31     | 28:16:A8:FD:09:0A  |     Success
|   32    |     ON     |   True   |     32     | 28:16:A8:FD:07:80  |     Success
|   33    |     ON     |   True   |     33     | 28:16:A8:FD:0A:A3  |     Success
|   34    |     ON     |   True   |     34     | 28:16:A8:FD:0A:5C  |     Success
|   35    |     ON     |   True   |     35     | 28:16:A8:FD:07:0B  |     Success
|   36    |     ON     |   True   |     36     | 28:16:A8:FD:06:2F  |     Success
|   37    |     ON     |   True   |     37     | 28:16:A8:FD:07:DC  |     Success
|   38    |     ON     |   True   |     38     | 28:16:A8:FD:08:0F  |     Success


```
#### create the static slot ID to hostname mappings (table 2 )
```
# python3 dictionary , compute node will have 2 IP for eth0 ,one is from DHCP ,one is set base on the slot ID locations 
id_ip= {    "3":"172.30.101.1",
            "4":"172.30.101.2",
            "5":"172.30.101.3",
            "6":"172.30.101.4",
            "7":"172.30.101.5",
            "8":"172.30.101.6",
            "9":"172.30.101.7",
            "10":"172.30.101.8",
            "11":"172.30.101.9",
            "12":"172.30.101.10",
            "13":"172.30.101.11",
            "14":"172.30.101.12",
            "27":"172.30.101.13",
            "28":"172.30.101.14",
            "29":"172.30.101.15",
            "30":"172.30.101.16",
            "31":"172.30.101.17",
            "32":"172.30.101.18",
            "33":"172.30.101.19",
            "34":"172.30.101.20",
            "35":"172.30.101.21",
            "36":"172.30.101.22",
            "37":"172.30.101.23",
            "38":"172.30.101.24"
            }


```
#### create the static hostname to linpack IP mappings （require or not ? ）(tables 3)
```
## all compute node will have the same /etc/hosts for cluster level linpack 
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
169.254.95.118 imm
169.254.96.118 imm2
172.30.101.1    node01  node01.cluster
172.30.101.2    node02  node02.cluster
172.30.101.3    node03  node03.cluster
172.30.101.4    node04  node04.cluster
172.30.101.5    node05  node05.cluster
172.30.101.6    node06  node06.cluster
172.30.101.7    node07  node07.cluster
172.30.101.8    node08  node08.cluster
172.30.101.9    node09  node09.cluster
172.30.101.10   node10  node10.cluster
172.30.101.11   node11  node11.cluster
172.30.101.12   node12  node12.cluster
172.30.101.13   node13  node13.cluster
172.30.101.14   node14  node14.cluster
172.30.101.15   node15  node15.cluster
172.30.101.16   node16  node16.cluster
172.30.101.17   node17  node17.cluster
172.30.101.18   node18  node18.cluster
172.30.101.19   node19  node19.cluster
172.30.101.20   node20  node20.cluster
172.30.101.21   node21  node21.cluster
172.30.101.22   node22  node22.cluster
172.30.101.23   node23  node23.cluster
172.30.101.24   node24  node24.cluster
172.30.101.25   node25  node25.cluster
172.30.101.26   node26  node26.cluster
172.30.101.27   node27  node27.cluster
172.30.101.28   node28  node28.cluster
172.30.101.29   node29  node29.cluster
172.30.101.30   node30  node30.cluster
172.30.101.31   node31  node31.cluster
172.30.101.32   node32  node32.cluster
172.30.101.33   node33  node33.cluster
172.30.101.34   node34  node34.cluster
172.30.101.35   node35  node35.cluster
172.30.101.36   node36  node36.cluster

```
#### nmap -p22 192.168.x.0/24 to update the arp tables 
#### check the arp tables to find the MAC to IP mappings (table 4)
```
[root@mfg-l1-4nl3 ~]# arp | grep 28:16
192.168.15.40            ether   28:16:a8:fd:06:2f   C                     eth7
192.168.15.59            ether   28:16:a8:fd:0a:5c   C                     eth7
192.168.15.55            ether   28:16:a8:fd:07:bc   C                     eth7
192.168.15.29            ether   28:16:a8:fd:0a:39   C                     eth7
192.168.15.70            ether   28:16:a8:fd:07:80   C                     eth7
192.168.15.69            ether   28:16:a8:fd:09:0a   C                     eth7
192.168.15.63            ether   28:16:a8:fd:08:04   C                     eth7
192.168.15.61            ether   28:16:a8:fd:08:0f   C                     eth7
192.168.15.52            ether   28:16:a8:fd:06:dd   C                     eth7
192.168.15.50            ether   28:16:a8:fd:08:92   C                     eth7
192.168.15.72            ether   28:16:a8:fd:07:0b   C                     eth7
192.168.15.49            ether   28:16:a8:fd:07:b1   C                     eth7
192.168.15.27            ether   28:16:a8:fd:09:c4   C                     eth7
192.168.15.68            ether   28:16:a8:fd:07:dc   C                     eth7
192.168.15.71            ether   28:16:a8:fd:0a:a3   C                     eth7

```

#### ssh compute node to update the SSH key pair for passwordless authentications (linpack MPI process requirement )

#### ssh compute node to set the hostname base on the tables  
#### ssh compute node to set the linpack IP base on the tables 

#### untar the linpack tools to the /root/HPL dir

#### update the /etc/hosts for name resolutions 
#### update the HPL.dat base on the Memory install on the compute node 
#### update the hostfile (who will join the cluster linpack ? )
#### start to run the cluster linpack
#### check the linpack result fo see if pass or failed 
```
[root@micro-106 linpack]#cat 24node_9run.log | grep 'CPU Cycle'
        HPL Efficiency by CPU Cycle   76.057%
        HPL Efficiency by CPU Cycle   76.786%
        HPL Efficiency by CPU Cycle   75.884%
        HPL Efficiency by CPU Cycle   75.441%
        HPL Efficiency by CPU Cycle   76.266%
        HPL Efficiency by CPU Cycle   75.780%
        HPL Efficiency by CPU Cycle   75.945%
        HPL Efficiency by CPU Cycle   75.870%
        HPL Efficiency by CPU Cycle   75.504%
[root@micro-106 linpack]#cat 24node_9run.log | grep 'BUS Cycle'
        HPL Efficiency by BUS Cycle   65.520%
        HPL Efficiency by BUS Cycle   65.900%
        HPL Efficiency by BUS Cycle   65.466%
        HPL Efficiency by BUS Cycle   65.271%
        HPL Efficiency by BUS Cycle   65.604%
        HPL Efficiency by BUS Cycle   65.413%
        HPL Efficiency by BUS Cycle   65.484%
        HPL Efficiency by BUS Cycle   65.501%
        HPL Efficiency by BUS Cycle   65.347%

```
#### debug if need (single linpack run or group linpack run )
#### remove the linpack IP in the management node 
#### goto next step   
