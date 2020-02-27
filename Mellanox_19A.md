# 
```

[root@mgt ~]#  nodeset n01-n02 osimage=myedr741; rsetboot n01-n02 net -u ;   rpower  n01-n02 reset
n01: netboot rhels7.5-x86_64-compute
n02: netboot rhels7.5-x86_64-compute
n02: Network
n01: Network
n02: reset
n01: reset
[root@mgt ~]# psh n01-n02 "bash /root/HPL/enable_hugepages"
[root@mgt ~]# psh n01-n02 "free -g |grep Mem"
n01: Mem:            188         180           5           1           1           5
n02: Mem:            188         181           5           1           1           5
[root@mgt ~]# ssh n03
Last login: Thu May  9 11:51:50 2019 from mgt.cluster
[root@n03 ~]# exit
logout
Connection to n03 closed.
[root@mgt ~]# ssh n01
[root@n01 ~]# cd HPL/
[root@n01 HPL]# service opensmd restart
Restarting opensmd (via systemctl):                        [  OK  ]
[root@n01 HPL]# ibstat
CA 'mlx5_0'
        CA type: MT4115
        Number of ports: 1
        Firmware version: 12.23.1020
        Hardware version: 0
        Node GUID: 0xec0d9a03003d677a
        System image GUID: 0xec0d9a03003d677a
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 100
                Base lid: 1
                LMC: 0
                SM lid: 1
                Capability mask: 0x2651e84a
                Port GUID: 0xec0d9a03003d677a
                Link layer: InfiniBand
[root@n01 HPL]# iblinkinfo
iblinkinfo     iblinkinfo.pl
[root@n01 HPL]# iblinkinfo  | grep Up
      0xec0d9a03003d62be      4    1[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       2   17[  ] "MF0;SB7700:MSB7700/U1" ( )
      0x248a070300928186      3    1[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       2   36[  ] "MF0;SB7700:MSB7700/U1" ( )
           2   17[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       4    1[  ] "n02 HCA-1" ( )
           2   18[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       1    1[  ] "n01 HCA-1" ( )
           2   36[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       3    1[  ] "mgt mlx5_0" ( )
      0xec0d9a03003d677a      1    1[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       2   18[  ] "MF0;SB7700:MSB7700/U1" ( )
[root@n01 HPL]# cat hostfile
n01
n02
[root@n01 HPL]# cat HPL.dat
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out      output file name (if any)
6            device out (6=stdout,7=stderr,file)
1            # of problems sizes (N)
204288       Ns
1            # of NBs
384          NBs
0            PMAP process mapping (0=Row-,1=Column-major)
1            # of process grids (P x Q)
2            Ps
2            Qs
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
[root@n01 HPL]# cat mgt_edr2node.sh
PATH=$PATH:/root/HPL:
export LD_LIBRARY_PATH=/root/HPL

export I_MPI_FALLBACK=disable
export I_MPI_FABRICS=dapl
export HPL_HWPREFETCH=1
export HNAME=`hostname`
export I_MPI_OFA_ADAPTER_NAME='mlx5_0'
fmt=`date +%Y%m%d%H%M%S`
#mkdir -p /install/linpack
mount | grep mgt >/dev/null
if [ $? -ne 0 ];then
        echo -e "Start to mount the mgt node for log store "
        mount mgt:/install /install
fi
mount | grep mgt
mkdir -p /install/linpack
#
mpirun -genvall -np 4 -ppn 2 -f hostfile    /root/HPL/run_TLP_sky  | tee -a /install/linpack/node_${HNAME}_cluster_${fmt}.log
[root@n01 HPL]#

```
