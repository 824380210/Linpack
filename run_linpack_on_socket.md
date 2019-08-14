#  RUN LINPACK TEST ON THE SOCKET(CPU)

### if we have singel node linpack failed or low performance ,then we need to find out which CPU(socket) cause bad performance 
### example of linpack failed
```

Peak Performance =    2120.62 GFlops /  1060.31 GFlops per node
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR00L2L4      102144   384     1     2             349.99            2.03000e+03
HPL_pdgesv() start time Thu Aug  1 13:21:06 2019

HPL_pdgesv() end time   Thu Aug  1 13:26:56 2019

        HPL Efficiency by CPU Cycle   92.971%
        HPL Efficiency by BUS Cycle   77.063%
--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   870806.8870057 ...... FAILED
||Ax-b||_oo  . . . . . . . . . . . . . . . . . =           2.362954
||A||_oo . . . . . . . . . . . . . . . . . . . =       25726.202361
||A||_1  . . . . . . . . . . . . . . . . . . . =       25729.833221
||x||_oo . . . . . . . . . . . . . . . . . . . =           9.301089
||x||_1  . . . . . . . . . . . . . . . . . . . =      168175.098487
||b||_oo . . . . . . . . . . . . . . . . . . . =           0.499999
================================================================================

Finished      1 tests with the following results:
              0 tests completed and passed residual checks,
              1 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.

```
### example bad performance VS good performance
```
# 2 sockets linpack run but bad performance 
 
Random number generator performance :   3151 M words/cycle
Highest Memory BW : 94.277 GB/sec on a5node55
Lowest  Memory BW : 93.889 GB/sec on a5node55

  Frac     N     PFact   Bcast    Swap  Update   PPerf BcstBW SwapBW   CPU      Kernel      Total Powr   Dpwr Tmp CFreq Ufreq WhoamI [rank,row,col]
  0.00       0   0.280   0.118   0.201   0.398   50.77   3581      0   0.00      35.63      50.77 125.9  12.8  64 3.543 2.388 a5node55[0,0,0]
  0.27     384   0.489   0.175   0.221   7.106   28.96   2417   1021  44.06    2247.21    2008.32 133.1  13.1  57 1.465 1.518 a5node55[1,0,1]
  0.53     768   0.366   2.792   0.226   4.152   38.60    151    929  79.77    3825.68    3496.82 272.7  15.3  73 2.738 1.525 a5node55[0,0,0]
  0.80    1152   0.518   0.155   0.203   8.203   27.16   2707   1032  40.40    1925.84    1974.20 132.9  13.2  57 1.341 1.851 a5node55[1,0,1]
  1.06    1536   0.372   6.943   0.201   7.586   37.76     60   1031  80.24    2071.49    2596.02 186.7  12.3  64 3.230 1.907 a5node55[0,0,0]
  1.33    1920   0.525   0.157   0.205   7.703   26.68   2659   1018  40.22    2029.12    1971.71 133.5  13.8  56 1.335 1.837 a5node55[1,0,1]
...
 99.47  143616   0.004   0.001   0.000   0.009   17.36   4632     17  32.43      74.38    1971.03  64.8   8.9  54 2.797 2.394 a5node55[0,0,0]
 99.73  144000   0.004   0.000   0.000   0.007   10.65   4602      0  32.05      34.36    1971.02  55.9   8.7  62 2.792 2.395 a5node55[1,0,1]
Peak Performance =    3496.82 GFlops /  1748.41 GFlops per node
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WC00L2L4      144384   384     1     2            1018.44            1.97031e+03
HPL_pdgesv() start time Wed Aug 14 03:41:18 2019

HPL_pdgesv() end time   Wed Aug 14 03:58:17 2019

        HPL Efficiency by CPU Cycle   39.096%
        HPL Efficiency by BUS Cycle   40.252%
--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=        0.0039120 ...... PASSED
================================================================================

Finished      1 tests with the following results:
              1 tests completed and passed residual checks,
              0 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.
================================================================================

# 1 socket linpack run with good performance 

Random number generator performance :   1570 M words/cycle
Highest Memory BW : 142.832 GB/sec on a5node55
Lowest  Memory BW : 142.832 GB/sec on a5node55

  Frac     N     PFact   Bcast    Swap  Update   PPerf BcstBW SwapBW   CPU      Kernel      Total Powr   Dpwr Tmp CFreq Ufreq WhoamI [rank,row,col]
  0.00       0   0.332   0.067   0.514   0.399   42.80      0      0   0.00      35.55      42.80 118.7  11.1  67 3.609 2.388 a5node55[0,0,0]
  0.27     384   0.561   0.100   0.479   8.823   25.21      0    818  73.48    1809.83    1631.26 270.4  14.3  72 2.509 2.217 a5node55[0,0,0]
  0.53     768   0.552   0.103   0.551   9.329   25.56      0    875  70.30    1702.51    1665.22 246.6  14.2  69 2.464 1.553 a5node55[0,0,0]
  0.80    1152   0.583   0.107   0.555   9.429   24.15      0    760  68.86    1675.53    1663.67 239.3  14.6  69 2.453 1.366 a5node55[0,0,0]
  1.06    1536   0.579   0.106   0.543   9.356   24.24      0    752  68.95    1679.50    1670.26 239.3  14.7  69 2.453 1.366 a5node55[0,0,0]
  1.33    1920   0.577   0.108   0.567   9.420   24.27      0    766  68.52    1659.19    1666.65 239.3  14.9  69 2.459 1.371 a5node55[0,0,0]
  1.60    2304   0.577   0.106   0.541   9.316   24.20      0    732  68.55    1668.62    1667.88 239.3  15.0  69 2.459 1.370 a5node55[0,0,0]
  1.86    2688   0.574   0.106   0.559   9.262   24.25      0    765  68.78    1669.42    1666.48 239.3  14.8  69 2.459 1.370 a5node55[0,0,0]
  2.13    3072   0.574   0.106   0.549   9.199   24.19      0    738  68.98    1671.65    1668.24 239.3  14.8  69 2.456 1.368 a5node55[0,0,0]
  2.39    3456   0.572   0.106   0.521   9.226   24.22      0    751  68.55    1657.82    1669.79 239.3  15.1  69 2.468 1.376 a5node55[0,0,0]
  2.66    3840   0.571   0.105   0.535   9.022   24.21      0    788  68.92    1686.03    1668.57 239.3  14.8  69 2.462 1.372 a5node55[0,0,0]
  2.93    4224   0.570   0.104   0.526   9.009   24.18      0    765  69.44    1679.20    1670.44 239.3  14.5  69 2.454 1.365 a5node55[0,0,0]
  3.19    4608   0.567   0.103   0.548   8.917   24.25      0    776  69.70    1687.25    1670.57 239.3  14.3  69 2.453 1.364 a5node55[0,0,0]
  3.46    4992   0.564   0.102   0.539   8.832   24.28      0    744  69.40    1694.18    1672.24 239.3  14.5  69 2.459 1.369 a5node55[0,0,0]
  3.72    5376   0.563   0.103   0.507   8.851   24.25      0    753  69.43    1681.38    1675.00 239.3  14.6  69 2.460 1.371 a5node55[0,0,0]
  3.99    5760   0.561   0.103   0.529   8.834   24.27      0    799  69.51    1675.33    1674.68 239.3  14.5  70 2.457 1.368 a5node55[0,0,0]
  4.26    6144   0.560   0.101   0.500   8.601   24.27      0    763  69.97    1711.17    1677.22 239.3  14.2  69 2.455 1.366 a5node55[0,0,0]
  4.52    6528   0.557   0.101   0.498   8.608   24.31      0    805  69.84    1700.21    1678.52 239.3  14.3  69 2.458 1.369 a5node55[0,0,0]
  4.79    6912   0.557   0.102   0.486   8.584   24.26      0    807  69.64    1695.63    1679.38 239.3  14.6  69 2.459 1.370 a5node55[0,0,0]

# 1 socket linpack run with bad  performance

HPL warning[a5node55] : Memory is too fragmented. Ratio is  50.01% (  221980 /   443904)
Random number generator performance :   1136 M words/cycle
Highest Memory BW : 141.971 GB/sec on a5node55
Lowest  Memory BW : 141.971 GB/sec on a5node55

  Frac     N     PFact   Bcast    Swap  Update   PPerf BcstBW SwapBW   CPU      Kernel      Total Powr   Dpwr Tmp CFreq Ufreq WhoamI [rank,row,col]
  0.00       0   0.331   0.067   0.475   0.399   42.88      0      0   0.00      35.61      42.88  87.9  10.9  55 3.308 2.393 a5node55[0,0,0]
  0.27     384   0.609   0.088   0.480  16.849   23.24      0    887  38.25     947.68     897.24 130.6  12.1  54 1.290 1.900 a5node55[0,0,0]
  0.53     768   0.628   0.090   0.473  17.319   22.49      0    874  37.47     917.07     905.31 131.8  12.6  54 1.260 1.986 a5node55[0,0,0]
  0.80    1152   0.626   0.091   0.479  17.535   22.47      0    886  37.06     900.95     904.22 132.3  12.8  54 1.247 2.041 a5node55[0,0,0]
  1.06    1536   0.624   0.090   0.471  17.358   22.49      0    871  37.02     905.28     904.61 132.7  12.9  54 1.246 2.051 a5node55[0,0,0]
  1.33    1920   0.625   0.090   0.480  17.252   22.40      0    884  37.15     905.96     903.68 132.7  12.9  54 1.249 2.057 a5node55[0,0,0]
  1.60    2304   0.617   0.089   0.470  17.153   22.65      0    865  37.24     906.25     905.09 132.6  12.9  54 1.253 2.039 a5node55[0,0,0]
  1.86    2688   0.619   0.089   0.468  17.041   22.50      0    881  37.21     907.33     905.40 132.5  12.9  54 1.252 2.040 a5node55[0,0,0]
  2.13    3072   0.621   0.089   0.470  16.919   22.37      0    882  37.17     908.91     905.84 132.4  12.9  54 1.250 2.040 a5node55[0,0,0]
  2.39    3456   0.617   0.089   0.466  16.757   22.44      0    876  37.28     912.71     906.19 132.5  12.9  54 1.255 2.039 a5node55[0,0,0]
  2.66    3840   0.611   0.087   0.456  16.694   22.62      0    880  37.42     911.20     907.17 132.9  12.9  54 1.260 2.039 a5node55[0,0,0]
  2.93    4224   0.607   0.089   0.466  16.570   22.68      0    899  37.48     913.01     907.17 132.8  12.9  53 1.260 2.044 a5node55[0,0,0]
...
 99.20  143232   0.005   0.000   0.000   0.011   23.66      0   4251  32.97     125.26     946.01  68.1   8.6  61 3.205 2.394 a5node55[0,0,0]
 99.47  143616   0.004   0.000   0.000   0.009   17.88      0   3141  32.34      78.65     946.01  63.6   8.7  60 3.109 2.394 a5node55[0,0,0]
 99.73  144000   0.003   0.000   0.000   0.006   11.09      0     17  31.40      37.09     946.01  68.3   9.9  58 2.795 2.394 a5node55[0,0,0]
Peak Performance =     946.09 GFlops /   946.09 GFlops per node
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WC00L2L4      144384   384     1     1            2122.20            9.45554e+02
HPL_pdgesv() start time Wed Aug 14 04:21:20 2019

HPL_pdgesv() end time   Wed Aug 14 04:56:42 2019

        HPL Efficiency by CPU Cycle   94.060%
        HPL Efficiency by BUS Cycle   38.887%
--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=        0.0039082 ...... PASSED
================================================================================

Finished      1 tests with the following results:
              1 tests completed and passed residual checks,
              0 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.
================================================================================


```
# how to run on single socket

### 1: update the  HPL.dat with P=Q=1 with normal other parameter as we do in general process 
```
# normal HPL.dat 

================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR00L2L4      102144   384     1     2             349.99            2.03000e+03


# single socket HPL.dat

================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WC00L2L4      144384   384     1     1            2122.20            9.45554e+02

```
###  2: hostfile should be same for single socket and 2 socket single node linpack 
#
###  3: update the run cpu 0  script as below
```
# the normal run linpack on 2 socket script
[root@S02MGT16 HPL]# cat  mgt_edr2node.sh
PATH=$PATH:/root/HPL:
export LD_LIBRARY_PATH=/root/HPL
export I_MPI_FALLBACK=disable
export I_MPI_FABRICS=dapl
export HPL_HWPREFETCH=1
export HNAME=`hostname`
export I_MPI_OFA_ADAPTER_NAME='mlx5_0'
fmt=`date +%Y%m%d%H%M%S`
VMIP=172.20.0.1
mount | grep $VMIP >/dev/null
if [ $? -ne 0 ];then
    echo -e "Start to mount the mgt node for log store "
    mount -t nfs $VMIP:/install /install
fi
mount | grep $VMIP
mkdir -p /install/linpack
mpirun -genvall -np 2 -ppn 2 -f hostfile /root/HPL/run_TLP_sky |& tee -a /install/linpack/Chassis_${HNAME}_cluster_${fmt}.log
umount /install
#
# the single CPU0 linpack run script 
[root@S02MGT16 HPL]# cat mgt_edr2node_cpu0.sh
PATH=$PATH:/root/HPL:
export LD_LIBRARY_PATH=/root/HPL
export I_MPI_FALLBACK=disable
export I_MPI_FABRICS=dapl
export HPL_HWPREFETCH=1
export HNAME=`hostname`
export I_MPI_OFA_ADAPTER_NAME='mlx5_0'
fmt=`date +%Y%m%d%H%M%S`
VMIP=172.20.0.1
mount | grep $VMIP >/dev/null
if [ $? -ne 0 ];then
    echo -e "Start to mount the mgt node for log store "
    mount -t nfs $VMIP:/install /install
fi
mount | grep $VMIP
mkdir -p /install/linpack
mpirun -genvall -np 1 -ppn 1 -f hostfile /root/HPL/run_TLP_sky_cpu0 |& tee -a /install/linpack/Chassis_${HNAME}_cluster_${fmt}.log
umount /install

# show the different about the normal linpack and single socket linpacu
[root@S02MGT16 HPL]# diff mgt_edr2node.sh mgt_edr2node_cpu0.sh
17c17
< mpirun -genvall -np 2 -ppn 2 -f hostfile /root/HPL/run_TLP_sky |& tee -a /install/linpack/Chassis_${HNAME}_cluster_${fmt}.log
---
> mpirun -genvall -np 1 -ppn 1 -f hostfile /root/HPL/run_TLP_sky_cpu0 |& tee -a /install/linpack/Chassis_${HNAME}_cluster_${fmt}.log
[root@S02MGT16 HPL]#


```
### 4: specify the CPU that to run linpack
```
# normal stress test on both CPU
[root@S02MGT16 HPL]# cat run_TLP_sky


export MPI_PER_NODE=2
export MPI_RANK_FOR_NODE=$((PMI_RANK % MPI_PER_NODE))


    export HPL_LARGEPAGE=2

    case ${MPI_RANK_FOR_NODE} in
    0)
    export HPL_HOST_NODE=0
    ;;
    1)
    export HPL_HOST_NODE=1
    ;;
    esac

/root/HPL/xhpl_lrz
# cpu 0 sterss 
[root@S02MGT16 HPL]# cat run_TLP_sky_cpu0


export MPI_PER_NODE=1
export MPI_RANK_FOR_NODE=$((PMI_RANK % MPI_PER_NODE))


    export HPL_LARGEPAGE=0

    export HPL_HOST_NODE=0

/root/HPL/xhpl_lrz

# show the different between the normal linpack and special linpack  
[root@S02MGT16 HPL]# diff run_TLP_sky run_TLP_sky_cpu0
3c3
< export MPI_PER_NODE=2
---
> export MPI_PER_NODE=1
7c7
<     export HPL_LARGEPAGE=2
---
>     export HPL_LARGEPAGE=0
9,10d8
<     case ${MPI_RANK_FOR_NODE} in
<     0)
12,16d9
<     ;;
<     1)
<     export HPL_HOST_NODE=1
<     ;;
<     esac



```

###
### 5:  run the single script 
```
 mgt_edr2node_cpu0.sh

```

### 6 run on the CPU1 
```
[root@S02MGT16 HPL]# diff mgt_edr2node_cpu0.sh  mgt_edr2node_cpu1.sh
17c17
< mpirun -genvall -np 1 -ppn 1 -f hostfile /root/HPL/run_TLP_sky_cpu0 |& tee -a /install/linpack/Chassis_${HNAME}_cluster_${fmt}.log
---
> mpirun -genvall -np 1 -ppn 1 -f hostfile /root/HPL/run_TLP_sky_cpu1 |& tee -a /install/linpack/Chassis_${HNAME}_cluster_${fmt}.log
[root@S02MGT16 HPL]# diff run_TLP_sky_cpu0 run_TLP_sky_cpu1
9c9
<     export HPL_HOST_NODE=0
---
>     export HPL_HOST_NODE=1
[root@S02MGT16 HPL]#


[root@S02MGT16 HPL]# diff run_TLP_sky_cpu0 run_TLP_sky_cpu1
9c9
<     export HPL_HOST_NODE=0
---
>     export HPL_HOST_NODE=1
[root@S02MGT16 HPL]# cat mgt_edr2node_cpu1.sh
PATH=$PATH:/root/HPL:
export LD_LIBRARY_PATH=/root/HPL
export I_MPI_FALLBACK=disable
export I_MPI_FABRICS=dapl
export HPL_HWPREFETCH=1
export HNAME=`hostname`
export I_MPI_OFA_ADAPTER_NAME='mlx5_0'
fmt=`date +%Y%m%d%H%M%S`
VMIP=172.20.0.1
mount | grep $VMIP >/dev/null
if [ $? -ne 0 ];then
    echo -e "Start to mount the mgt node for log store "
    mount -t nfs $VMIP:/install /install
fi
mount | grep $VMIP
mkdir -p /install/linpack
mpirun -genvall -np 1 -ppn 1 -f hostfile /root/HPL/run_TLP_sky_cpu1 |& tee -a /install/linpack/Chassis_${HNAME}_cluster_${fmt}.log
umount /install
[root@S02MGT16 HPL]#



```
