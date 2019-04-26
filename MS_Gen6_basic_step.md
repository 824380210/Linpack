#### use nmap to check if all system up and ready 

```
nmap -p22 --system-dns 192.168.14.0/24

```


#### 运行python脚本

```
[root@micro-106 linpack]#python3.6 /root/read_ms_gen6_rack_info.py

```

#### hugepages 设置来运行

```
# 解压
[root@micro-106 linpack]#pdsh -w 172.30.101.[1-24] "cd /root; tar zxvf /dfcxact/product/common/linpack/HPL.tgz"
# 准备HPL.dat文件
[root@micro-106 linpack]# pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/HPL.dat /root/HPL/"
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



