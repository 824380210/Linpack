# OPA Network Linpack Test instruction

## demo cluster configuration 
```
- 2 compute node in a groups : n03.cluster and n04.cluster
- opa network 
- compute node configure: CPU   :8160 x2 
                          Memory:16GB *12 
                          
```
# when start to test your OPA cluster ,you should update your HPL.dat and hostfile base on the real order configurations 

# create the OPA network netboot osimage
```
[root@mgt opa76]# md5sum /root/opa76_19A_20190514.tgz
685caa05a47ba72b0fc1cf01749c3042  /root/opa76_19A_20190514.tgz

[root@mgt ~]#  mkdef -t osimage -o opa76  --template  rhels7.6-x86_64-netboot-compute   rootimgdir=/install/netboot/rhels7.6/x86_64/opa76
1 object definitions have been created or modified.

[root@mgt ~]# mkdir -p /install/netboot/rhels7.6/x86_64/opa76

[root@mgt ~]# cd /install/netboot/rhels7.6/x86_64/opa76

[root@mgt opa76]# tar zxvf /root/opa76_19A_20190514.tgz
kernel
initrd-stateless.gz
rootimg.cpio.gz


```
# netboot the compute node with the opa76 osimage
```
[root@mgt ~]# nodeset n03-n04 osimage=opa76
n03: netboot rhels7.6-x86_64-compute
n04: netboot rhels7.6-x86_64-compute
[root@mgt ~]# rsetboot n03-n04 net -u
n03: Network
n04: Network
[root@mgt ~]# rpower n03-n04 off
n03: off
n04: off
[root@mgt ~]# rpower n03-n04 on
n03: on
n04: on
[root@mgt ~]#


```
# monitor the compute node till all netboot osimage is load,up and running 
```

[root@mgt ~]# psh n03-n04 echo OK
n03: OK
n04: OK

```

# updatet the compute node HPL.dat and hostlist file 
```
[root@mgt ~]# cat HPL.dat
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
[root@mgt ~]# pscp HPL.dat n03-n04:/root/HPL/
n03: done
n04: done

[root@mgt ~]# nodels n03-n04 >hostfile
[root@mgt ~]# pscp hostfile n03-n04:/root/HPL/
n03: done
n04: done
[root@mgt ~]# cat hostfile
n03
n04


```
# check the OPA network adapter is up and active
```
[root@mgt ~]# ssh n03
Last login: Tue Jul 16 10:59:30 2019 from mgt.cluster
[root@n03 ~]# service opafm restart
Redirecting to /bin/systemctl restart opafm.service
[root@n03 ~]# opainfo
hfi1_0:1                           PortGID:0xfe80000000000000:0011750101701541
   PortState:     Active
   LinkSpeed      Act: 25Gb         En: 25Gb
   LinkWidth      Act: 4            En: 4
   LinkWidthDnGrd ActTx: 4  Rx: 4   En: 3,4
   LCRC           Act: 14-bit       En: 14-bit,16-bit,48-bit       Mgmt: True
   LID: 0x00000001-0x00000001       SM LID: 0x00000001 SL: 0
         QSFP Copper,       3m  Hitachi Metals    P/N IQSFP26C-30       Rev 01
   Xmit Data:                  0 MB Pkts:                   18
   Recv Data:                  0 MB Pkts:                   18
   Link Quality: 5 (Excellent)
[root@n03 ~]# opa
opa-arptbl-tuneup   opafmcmd            opagetvf_env        opa_osd_exercise    opapacketcapture    opasaquery
opaautostartconfig  opafmcmdall         opahfirev           opa_osd_load        opapmaquery         opasmaquery
opacapture          opafmconfigpp       opainfo             opa_osd_perf        opaportconfig       opasystemconfig
opaconfig           opafmvf             opa-init-kernel     opa_osd_query       opaportinfo         opatmmtool
opafabricinfo       opagetvf            opa_osd_dump        opa_osd_query_many  oparesolvehfiport
[root@n03 ~]# opafabricinfo
Fabric 0:0 Information:
SM: n03 hfi1_0 Guid: 0x0011750101701541 State: Master
Number of HFIs: 2
Number of Switches: 0
Number of Links: 1
Number of HFI Links: 1              (Internal: 0   External: 1)
Number of ISLs: 0                   (Internal: 0   External: 0)
Number of Degraded Links: 0         (HFI Links: 0   ISLs: 0)
Number of Omitted Links: 0          (HFI Links: 0   ISLs: 0)
-------------------------------------------------------------------------------
[root@n03 ~]#

[root@mgt ~]# psh n03-n04 opainfo | grep -E 'PortState|LinkSpeed|LinkWidth|Link Quality' |xcoll
====================================
n04,n03
====================================
   PortState:     Active
   LinkSpeed      Act: 25Gb         En: 25Gb
   LinkWidth      Act: 4            En: 4
   LinkWidthDnGrd ActTx: 4  Rx: 4   En: 3,4
   Link Quality: 5 (Excellent)


```
# Login one compute node in the same groups to run the linpack test 
```

ot@mgt ~]# ssh n04
Last login: Tue Jul 16 11:02:38 2019 from mgt.cluster
[root@n04 ~]# cd HPL
[root@n04 HPL]# cat HPL.dat
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
[root@n04 HPL]# cat hostfile
n03
n04

[root@n04 HPL]# cat mgt_opa2node.sh
PATH=$PATH:/root/HPL:/root/HPL/intel64/bin:

export LD_LIBRARY_PATH=/root/HPL/intel64/lib

export I_MPI_FALLBACK=disable
export I_MPI_FABRICS=shm:tmi
export I_MPI_TMI_PROVIDER=psm2
export I_MPI_ROOT=/root/HPL/

export HPL_HWPREFETCH=1
export HNAME=`hostname`
fmt=`date +%Y%m%d%H%M%S`
#mkdir -p /install/linpack
mount | grep mgt >/dev/null
if [ $? -ne 0 ];then
        echo -e "Start to mount the mgt node for log store "
        mount mgt:/install /install
fi
mount | grep mgt
mkdir -p /install/linpack

#export I_MPI_OFA_ADAPTER_NAME='mlx5_0'
mpirun -genvall -np 4 -ppn 2 -f hostfile    /root/HPL/run_TLP_sky  | tee -a /install/linpack/$(hostname -s)_2node_cluster_opa_${fmt}.log
[root@n04 HPL]# bash mgt_opa2node.sh

```
# after the linpack run done ,check the test result 
## pass score should be more than 65% in HPL efficiency for both CPU Cycle and BUS Cycle

```
andom number generator performance :   4440 M words/cycle
Highest Memory BW : 87.007 GB/sec on n04
Lowest  Memory BW : 85.315 GB/sec on n03

  Frac     N     PFact   Bcast    Swap  Update   PPerf BcstBW SwapBW   CPU      Kernel      Total Powr   Dpwr Tmp CFreq Ufreq WhoamI [rank,row,col]
  0.00       0   0.240   0.126   0.338   0.367   83.80   2383      0   0.00      54.79      83.80 111.2  10.4  78 2.462 2.390 n03[0,0,0]
  0.19     384   0.317   0.182   0.382   6.055   63.30   1648    850  81.60    5283.65    4695.53 170.4  13.3  69 1.789 1.487 n04[3,1,1]
  0.38     768   0.325   0.179   1.307   6.603   61.61   1675    409  76.02    4826.89    4530.81 153.3  12.9  82 1.760 1.575 n03[0,0,0]
  0.56    1152   0.340   0.371   0.395   7.177   58.72    807    769  70.63    4424.25    4632.84 149.6  13.4  72 1.538 1.442 n04[3,1,1]
  0.75    1536   0.362   0.185   1.382   7.327   55.13   1607    182  68.44    4317.18    4430.15 149.5  12.2  83 1.754 1.508 n03[0,0,0]
  0.94    1920   0.344   0.894   0.386   7.135   57.89    333    787  70.64    4416.43    4566.19 149.6  13.3  77 1.540 1.426 n04[3,1,1]
...
...
...
 98.87  201984   0.014   0.002   0.001   0.020   16.30   2766   1417  65.59     239.67    4300.08  85.3   6.8  80 2.254 2.394 n03[0,0,0]
 99.06  202368   0.008   0.001   0.001   0.017   23.06   3000   1268  42.21     199.51    4300.03  73.2   6.5  86 3.343 2.394 n04[3,1,1]
 99.25  202752   0.012   0.001   0.001   0.016   12.73   2963   1171  65.81     139.05    4299.98  84.7   6.8  79 2.189 2.394 n03[0,0,0]
 99.44  203136   0.007   0.001   0.001   0.014   15.35   3229   1035  41.33      97.56    4299.93  78.2   6.8  86 3.361 2.394 n04[3,1,1]
 99.62  203520   0.010   0.001   0.000   0.013    7.47   3065      6  61.63      52.36    4299.89  88.1   7.2  78 2.124 2.394 n03[0,0,0]
 99.81  203904   0.007   0.001   0.000   0.011    5.48   3260      0  51.66      21.30    4299.86  69.3   6.0  84 3.242 2.394 n04[3,1,1]
Peak Performance =    4530.81 GFlops /  1132.70 GFlops per node
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR00L2L4      204288   384     2     2            1322.30            4.29845e+03
HPL_pdgesv() start time Tue Jul 16 11:17:46 2019

HPL_pdgesv() end time   Tue Jul 16 11:39:49 2019

        HPL Efficiency by CPU Cycle   78.291%
        HPL Efficiency by BUS Cycle   67.068%
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
