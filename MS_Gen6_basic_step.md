#### use nmap to check if all system up and ready 

```
nmap -p22 --system-dns 192.168.14.0/24

```


#### 运行python脚本

```
# make sure the interface connect to th TOR switch have setup with 192.168.x.0 network and 172.30.0.1(linpack IP ) for communication 
#
[root@micro-106 ~]#ibdev2netdev
mlx4_0 port 1 ==> eth6 (Up)
mlx4_0 port 2 ==> eth7 (Down)
#
# use the "ip addr show dev eth6" to check the IP address ,but not use the ifconfig ,it will not show all IP as we expect 
[root@micro-106 ~]#ip addr show dev eth6
10: eth6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
    link/ether 24:8a:07:63:05:81 brd ff:ff:ff:ff:ff:ff
    inet 192.168.14.2/24 brd 192.168.14.255 scope global eth6
    inet 172.30.0.1/16 brd 172.30.255.255 scope global eth6
    inet6 fe80::268a:7ff:fe63:581/64 scope link
       valid_lft forever preferred_lft forever

##
##

[root@micro-106 linpack]#python3.6 /root/read_ms_gen6_rack_info.py

```

#### hugepages 设置来运行

```
# 解压
[root@micro-106 linpack]#pdsh -w 172.30.101.[1-24] "cd /root; tar zxvf /dfcxact/product/common/linpack/HPL.tgz"
# 准备HPL.dat文件
[root@micro-106 linpack]# pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/HPL.dat /root/HPL/"
[root@micro-106 linpack]# pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/run_smp_10hrs /root/HPL/ "
# hugepage setup
[root@micro-106 linpack]# pdsh -w 172.30.101.[1-24] "echo 92 > /sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages;echo 92 > /sys/devices/system/node/node1/hugepages/hugepages-1048576kB/nr_hugepages"


```
# 10小时压力测试开始跑

```
[root@micro-106 ~]# pdsh -w 172.30.101.[1-24] "cd /root/HPL; bash run_smp_10hrs"


```
# 详细10小时压力脚本
```


[root@micro-106 linpack]#cat run_smp_10hrs
PATH=$PATH:/root/HPL:
export LD_LIBRARY_PATH=/root/HPL

export I_MPI_FALLBACK=disable
export I_MPI_FABRICS=shm:shm
export HPL_HWPREFETCH=1
export HNAME=`hostname`
# run 60 cycle to reach 10hrs
for a in `seq 60`
do
mpirun -genvall -np 2 -ppn 2 -hosts $HNAME /root/HPL/run_TLP_sky  | tee -a /dfcxact/product/common/linpack/single_${HNAME}_10hours.log
done

```

# cluster level linpack step after single node level linpack done 
```
# 1: update the HPL.dat base on the cluster node number and memory size 
	pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/HPL.dat.24 /root/HPL/HPL.dat "

# 2: update the /etc/hosts for name resolution for whole cluster 
	pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/hosts  /etc/hosts "

# 3: update the hostfile ,so all compute node in hostfile will join the cluster level linpack run
	pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/hostfile  /root/HPL/ "
# 4: update the scripts in one compute node (any node ),then run the scripts for cluster level 

[root@micro-106 ~]#ssh 172.30.101.1
[root@node01 ~]# cd HPL/
[root@node01 HPL]# vim run_smp_24_10hrs
[root@node01 HPL]# cat run_smp_24_10hrs
PATH=$PATH:/root/HPL:
export LD_LIBRARY_PATH=/root/HPL

export I_MPI_FALLBACK=disable
export I_MPI_FABRICS=shm:tcp
export HPL_HWPREFETCH=1
export HNAME=`hostname`
for a in `seq 10`
do
mpirun -genvall -np 48 -ppn 2 -f hostfile  -genv I_MPI_NETMASK  eth0  /root/HPL/run_TLP_sky  | tee -a /dfcxact/product/common/linpack/24node_cluster_10hrs.log
done
[root@node01 HPL]#bash run_smp_24_10hrs

```

