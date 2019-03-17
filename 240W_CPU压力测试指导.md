# TU 订单linux Linpack 测试指导

## 单机测试指导

###### 1: 正常CMOS 设置更新

```
# 刷新tu1.asu，并重启使之生效

[root@mgt43 ~]# cat tu1.asu
loaddefault BootOrder
loaddefault uEFI
set OperatingModes.ChooseOperatingMode "Maximum Performance"


# 刷新 tu2.asu，再设置CPU TDP 为240W 

[root@mgt43 ~]# cat tu2.asu
set OperatingModes.ChooseOperatingMode "Custom Mode"
set Processors.CPUPstateControl Cooperative
set Processors.SNC Disable
set SystemRecovery.F1StartControl "Text Setup"
set DevicesandIOPorts.ConsoleRedirection Enable
set DevicesandIOPorts.SerialPortSharing Enable
set DevicesandIOPorts.SerialPortAccessMode Dedicated
set DevicesandIOPorts.Com1TerminalEmulation VT-UTF8
set DevicesandIOPorts.Com1ActiveAfterBoot Enable
set DevicesandIOPorts.Com1FlowControl Hardware
set DiskGPTRecovery.DiskGPTRecovery None
set EnableDisableAdapterOptionROMSupport.OnboardVideo UEFI

# 参考CPU工作在240W的命令，注意仅支持特定型号，如现在的8174 CPU 

 pasu all set  processors.TDP 240 --override


```


###### 2: 配置hugepage引导选项

```
chdef  all addkcmdline="hugepagesz=1G hugepages=88 default_hugepagesz=1G"
nodeset all osimage=myopa741
rsetboot all net -u
# 注意 chiller并不支持整机跑压力测试（受制冷功率限制 ），因此不要全开机，
rpower c1,c2,c3,c4 on

```
###### 3：测试前检查节点的hugepage

```
[root@mgt43 ~]# psh c1 cat /proc/meminfo | grep -i hugepages_total
n405-003: HugePages_Total:      88
n405-002: HugePages_Total:      88
n405-004: HugePages_Total:      88
n405-005: HugePages_Total:      88
n405-006: HugePages_Total:      88
n405-001: HugePages_Total:      88
n405-008: HugePages_Total:      88
n405-009: HugePages_Total:      88
n405-010: HugePages_Total:      88
n405-007: HugePages_Total:      88
n405-011: HugePages_Total:      88
n405-012: HugePages_Total:      88

```

###### 4：执行单机版的压力测试脚本

```
管理节点上解压文件
[root@mgt43 install]# md5sum /tmp/chk_tu_2019.tgz
d1eee94d3e1fa081386069602e178641  /tmp/chk_tu_2019.tgz


[root@mgt43 ~]# cd /install/
[root@mgt43 install]# tar czvf /tmp/chk_tu_2019.tgz chk/
chk/
chk/.hfilist.swp
chk/cluster/
...

# 同步单机压力测试到计算节点
[root@mgt43 install]# pscp /install/chk/tu_single_run.sh c1,c2:/root/
n405-001: done
n405-006: done
n405-004: done

# 执行压力测试
[root@mgt43 ~]# psh c1 "cd /root ; bash tu_single_run.sh"

# 约6分钟左右就会完成单机测试，检查结果 （要求单机结果大于 3.2 TFlops ）

[root@mgt43 install]# grep WC /install/chk_n405-*.log  |sort -n -k7
/install/chk_n405-003.cluster_single_201903171128.log:WC00L2L4      102144   336     1     2             221.26            3.21106e+03
/install/chk_n405-007.cluster_single_201903171128.log:WC00L2L4      102144   336     1     2             220.19            3.22668e+03
/install/chk_n405-002.cluster_single_201903171128.log:WC00L2L4      102144   336     1     2             220.06            3.22855e+03
/install/chk_n405-001.cluster_single_201903170329.log:WC00L2L4      102144   336     1     2             218.29            3.25475e+03
/install/chk_n405-012.cluster_single_201903171128.log:WC00L2L4      102144   336     1     2             217.28            3.26985e+03
/install/chk_n405-010.cluster_single_201903171128.log:WC00L2L4      102144   336     1     2             216.40            3.28315e+03
/install/chk_n405-011.cluster_single_201903171128.log:WC00L2L4      102144   336     1     2             216.27            3.28525e+03
/install/chk_n405-009.cluster_single_201903170329.log:WC00L2L4      102144   336     1     2             215.91            3.29073e+03
/install/chk_n405-006.cluster_single_201903171128.log:WC00L2L4      102144   336     1     2             214.84            3.30701e+03
/install/chk_n405-008.cluster_single_201903171128.log:WC00L2L4      102144   336     1     2             213.75            3.32398e+03
/install/chk_n405-004.cluster_single_201903171128.log:WC00L2L4      102144   336     1     2             212.07            3.35020e+03
/install/chk_n405-005.cluster_single_201903171128.log:WC00L2L4      102144   336     1     2             210.89            3.36901e+03
[root@mgt43 install]#


```
## 组Linpack测试


###### 1： 测试前准备 （参考单机的测试步骤 1，2，3）

###### 2： 更新HPL.dat文件

```
[root@mgt43 ~]# pscp HPL.dat c1:/root/
n405-001: done
...
n405-010: done

# 同步hostfile到计算节点组
[root@mgt43 ~]# nodels c1 >hostfile
[root@mgt43 ~]# pscp hostfile c1:/root/
n405-003: done
...
n405-012: done

#  确认管理节点/install目录挂载完成
[root@mgt43 ~]# psh c1 mount | grep mgt
n405-001: mgt:/install on /install type nfs4 (rw,relatime,vers=4.1,rsize=1048576,wsize=1048576,namlen=255,hard,proto=tcp,port=0,timeo=600,retrans=2,sec=sys,clientaddr=10.181.5.1,local_lock=none,addr=10.181.0.1)
...
n405-012: mgt:/install on /install type nfs4 (rw,relatime,vers=4.1,rsize=1048576,wsize=1048576,namlen=255,hard,proto=tcp,port=0,timeo=600,retrans=2,sec=sys,clientaddr=10.181.5.12,local_lock=none,addr=10.181.0.1)
n405-010: mgt:/install on /install type nfs4 (rw,relatime,vers=4.1,rsize=1048576,wsize=1048576,namlen=255,hard,proto=tcp,port=0,timeo=600,retrans=2,sec=sys,clientaddr=10.181.5.10,local_lock=none,addr=10.181.0.1)

# 确认mgt:/install/chk 文件已复制到计算节点的/root/目录下
[root@mgt43 ~]# psh c1 rm -fr /root/chk
[root@mgt43 ~]# psh c1 scp -r /install/chk /root/
[root@mgt43 ~]# psh c1 ls /root/chk |xcoll
====================================
c1
====================================
cluster
create1nodebatch.sh
deviation
deviation.c
disableht_knl
enableht_knl
enablht.knl
HPL.dat
...

# 检查OPA网络准备就绪

[root@mgt43 ~]# psh n405-001  systemctl restart opafm.service

[root@mgt43 ~]# psh c1 opainfo | grep -E 'Link Quality|PortState' |xcoll
====================================
c1
====================================
   PortState:     Active
   Link Quality: 5 (Excellent)

[root@mgt43 ~]#

```
## 登录一个计算节点，开始跑压力测试


```


[root@mgt43 ~]# ssh n405-001
Last login: Sun Mar 17 03:48:32 2019 from 10.181.0.1

[root@n405-001 ~]# source /root/chk/tools_cluster.sh
[root@n405-001 ~]#

[root@n405-001 ~]# cat hostfile
n405-001
...
n405-012
[root@n405-001 ~]# cat HPL.dat
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out      output file name (if any)
6            device out (6=stdout,7=stderr,file)
1            # of problems sizes (N)
353856       Ns
1            # of NBs
336          NBs
0            PMAP process mapping (0=Row-,1=Column-major)
1            # of process grids (P x Q)
4            Ps
6            Qs
16.0         threshold
1            # of panel fact
0            PFACTs (0=left, 1=Crout, 2=Right)
1            # of recursive stopping criterium
4            NBMINs (>= 1)
1            # of panels in recursion
2            NDIVs
1            # of recursive panel fact.
0            RFACTs (0=left, 1=Crout, 2=Right)
1            # of broadcast
0            BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM,6=Psh,7=Spush,8=Psh2)
1            # of lookahead depth
0            DEPTHs (>=0)
0            SWAP (0=bin-exch,1=long,2=mix)
1            swapping threshold
1            L1 in (0=transposed,1=no-transposed) form
1            U  in (0=transposed,1=no-transposed) form
0            Equilibration (0=no,1=yes)
8            memory alignment in double (> 0)


[root@n405-001 ~]# mpirun -np 24 -ppn 2 -genvall -f /root/hostfile   /root/chk/run_TLP_sky | tee /install/rack5_C1_group.log


012个节点的组测试时间约13分钟，针对96G的内存节点而言

 99.51  352128   0.006   0.001   0.000   0.009   21.12   3042      0  67.97     277.34   37800.95  79.8   8.1  57 2.816 2.395 n405-003[4,0,4]
 99.61  352464   0.007   0.000   0.000   0.008   15.88   6537      0  50.32     199.31   37801.20 103.5   9.0  60 2.791 2.395 n405-006[11,1,5]
 99.70  352800   0.006   0.001   0.000   0.007   13.88   3415      0  44.25     132.96   37806.67  86.5   7.5  58 2.798 2.394 n405-007[12,2,0]
 99.80  353136   0.006   0.000   0.000   0.008    8.54   6715      0  50.76      66.00   37800.14  71.7   8.3  60 2.793 2.395 n405-010[19,3,1]
 99.89  353472   0.005   0.001   0.000   0.007    5.47   3747      0  52.89      27.12   37805.63  91.6   8.7  57 2.795 2.394 n405-002[2,0,2]
 99.99  353808   0.001   0.000   0.000   0.001    0.00   7638      4  30.59       8.48   37811.60  79.9  10.0  64 2.825 2.393 n405-005[9,1,3]
Peak Performance =   40496.62 GFlops /  1687.36 GFlops per node
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR00L2L4      353856   336     4     6             781.69            3.77882e+04
HPL_pdgesv() start time Sun Mar 17 03:54:46 2019

HPL_pdgesv() end time   Sun Mar 17 04:07:48 2019

        HPL Efficiency by CPU Cycle   84.543%
        HPL Efficiency by BUS Cycle   66.668%
--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=        0.0028939 ...... PASSED



第二组的结果：
 99.89  353472   0.006   0.001   0.000   0.007    5.18   3665      0  54.50      26.11   38005.22  81.7   8.2  56 2.792 2.394 n405-014[2,0,2]
 99.99  353808   0.001   0.000   0.000   0.001    0.00   7555      4  30.79       8.66   38005.22 127.5   9.6  67 2.829 2.397 n405-017[9,1,3]
Peak Performance =   40464.27 GFlops /  1686.01 GFlops per node
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR00L2L4      353856   336     4     6             777.45            3.79941e+04
HPL_pdgesv() start time Sun Mar 17 12:05:07 2019

HPL_pdgesv() end time   Sun Mar 17 12:18:04 2019

        HPL Efficiency by CPU Cycle   80.552%
        HPL Efficiency by BUS Cycle   66.937%


```



#### 如果开机到组测试，参考命令：

```

 1127  psh n405-001  systemctl restart opafm.service
 1128  pscp HPL.dat c2:/root/
 1129  psh c2 mount mgt:/install /install
 1130  psh c2 scp -r /install/chk /root/
 1131  pscp HPL.dat c2:/root/
 1132  nodels c2 >hostfile
 1133  cat hostfile
 1134  pscp hostfile  c2:/root/
 1136  cat tu_single_run.sh
 1137  psh c2 hugeadm --create-global-mounts --set-recommended-shmmax
 1138  psh c2 cpupower frequency-set -g performance


   26  source /root/chk/tools_cluster.sh
   28  cat hostfile
   29  cat HPL.dat
   31  mpirun -np 24 -ppn 2 -genvall -f /root/hostfile   /root/chk/run_TLP_sky | tee /install/rack5_C1_group.log

```


## 240W CPU 测试的主要区别在于：
##### 1： CPU 不是常规的运行功率
##### 2： 每一个节点运行任务，即 2 MPI task per node  ,即process per node (ppn) 为2 
##### 3： 由第二点所知，P * Q  = MPI 任务数，如12个节点，每个节点是2个mpi任务，则P * q = 12 * 2 = 24 
##### 4:  基于chulho的LRZ测试结果发现，NB = 336的时候成绩较好些
