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


```
#### ssh to rack manager to get the compute node slot ID to mac address mapping (table 1 )
```


```
#### create the static slot ID to hostname mappings (table 2 )
#### create the static slot ID to linpack IP mappings （require or not ? ）(tables 3)

#### nmap -p22 192.168.x.0/24 to update the arp tables 
#### check the arp tables to find the MAC to IP mappings (table 4)

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
