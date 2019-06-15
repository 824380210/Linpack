# edr76 Linpack Run WI 
#
#
#### netboot the edr76 image 
```
[root@mgt ~]# lsdef -t osimage | grep edr
myedr741  (osimage)           -------------   this is the edr76 image content even the name show here is myedr741 
[root@mgt ~]# nodeset edr osimage=myedr741
n01: netboot rhels7.5-x86_64-compute
n02: netboot rhels7.5-x86_64-compute
[root@mgt ~]# rsetboot edr net -u
n01: Network
n02: Network
[root@mgt ~]# rpower edr reset
n01: reset
n02: reset
```

#### Login one node to active the Infiniband Link 
```
[root@mgt ~]# ssh n01
Last login: Sat Jun 15 12:39:00 2019 from mgt.cluster
[root@n01 ~]# cd HPL
[root@n01 HPL]# service  openibd restart
Unloading HCA driver:                                      [  OK  ]
Loading HCA driver and Access Layer:                       [  OK  ]
[root@n01 HPL]# service  opensmd restart
Restarting opensmd (via systemctl):                        [  OK  ]
[root@n01 HPL]#

[root@n01 HPL]# iblinkinfo
CA: n02 HCA-1:
      0xec0d9a03003d62be      4    1[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       2   17[  ] "MF0;SB7700:MSB7700/U1" ( )
CA: mgt mlx5_0:
      0x248a070300928186      3    1[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       2   36[  ] "MF0;SB7700:MSB7700/U1" ( )
Switch: 0x506b4b0300820910 MF0;SB7700:MSB7700/U1:
           2    1[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2    2[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2    3[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2    4[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2    5[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2    6[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2    7[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2    8[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2    9[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2   10[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2   11[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2   12[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2   13[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2   14[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2   15[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2   16[  ] ==(                Down/ Polling)==>             [  ] "" ( )
           2   17[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       4    1[  ] "n02 HCA-1" ( )
           2   18[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       1    1[  ] "n01 HCA-1" ( )
```

### update the HPL.dat / hostfile 
```
[root@n01 HPL]# cat hostfile
n01
n02
[root@n01 HPL]# cat HPL.dat      (2 node , and each node run 2 xhpl process ,so P=Q=2 ) 
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
[root@n01 HPL]#
```

#### run the linpack and check the result 
```
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
[root@n01 HPL]# bash mgt_edr2node.sh
Start to mount the mgt node for log store
mgt:/install on /install type nfs4 (rw,relatime,vers=4.1,rsize=1048576,wsize=1048576,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=172.20.103.1,local_lock=none,addr=172.20.0.1)
Skylake architecture(B) has been selected.
HPL[n01] : numa node No.  0 is active.
...

Peak Performance =    4726.59 GFlops /  1181.65 GFlops per node
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR00L2L4      204288   384     2     2            1266.20            4.48891e+03
HPL_pdgesv() start time Sat Jun 15 12:42:45 2019

HPL_pdgesv() end time   Sat Jun 15 13:03:51 2019

        HPL Efficiency by CPU Cycle   86.928%
        HPL Efficiency by BUS Cycle   70.085%
--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=        0.0038237 ...... PASSED
================================================================================

Finished      1 tests with the following results:
              1 tests completed and passed residual checks,
              0 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.
================================================================================

```
### Options setup the hugepages settings before the Linpack (should be enable in all compute node )
```
psh n01-n02 bash /root/HPL/enable_hugepages 

# this is options operations ,you can try if the test result is not so good as expected 









```
