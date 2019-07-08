# Lenovo ThinkSystem SR850 4 sockets 384G Single Node Linpack Test

## configure
```
Intel 8268 CPU x4
Memory 16G 24x , Total 384GB

```
## HPL.dat
```
[root@mgt50 4socket]# cat HPL.dat
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
[root@mgt50 4socket]#


```
## run 4 MPI process in the single node  


```
[root@mgt50 4socket]# cat run_sr850_TLP_sky
export MPI_PER_NODE=4
export MPI_RANK_FOR_NODE=$((PMI_RANK % MPI_PER_NODE))


    export HPL_LARGEPAGE=2

    case ${MPI_RANK_FOR_NODE} in
    0)
    export HPL_HOST_NODE=0
    ;;
    1)
    export HPL_HOST_NODE=1
    ;;
    2)
    export HPL_HOST_NODE=2
    ;;
    3)
    export HPL_HOST_NODE=3
    ;;
    esac
/root/HPL/xhpl_lrz

```

## single node linpack run scripts

```

[root@mgt50 4socket]# ls
HPL.dat  run_sr850_TLP_sky  sr850_single_node.sh

[root@mgt50 4socket]# cat sr850_single_node.sh
PATH=$PATH:/root/HPL:
export LD_LIBRARY_PATH=/root/HPL

export I_MPI_FALLBACK=disable
#export I_MPI_FABRICS=dapl
export HPL_HWPREFETCH=1
export HNAME=`hostname`
#export I_MPI_OFA_ADAPTER_NAME='mlx5_0'
fmt=`date +%Y%m%d%H%M%S`
#mkdir -p /install/linpack
mount | grep mgt >/dev/null
if [ $? -ne 0 ];then
        echo -e "Start to mount the mgt node for log store "
        mount mgt:/install /install
fi
mount | grep mgt
hostname -s >hostfile
mkdir -p /install/linpack
#
mpirun -genvall -np 4 -ppn 4 -f hostfile    /root/HPL/run_sr850_TLP_sky  | tee -a /install/linpack/node_${HNAME}_single_${fmt}.log
```
# test result example
```
[root@node11 HPL]# bash sr850_single_node.sh 

97.74  199680   0.008   0.003   0.006   0.022   57.81   2451    917  30.83     798.66    5925.75  86.0  10.0  84 3.446 2.394 node11[0,0,0]
97.93  200064   0.008   0.003   0.005   0.022   55.36   2415    862  31.20     677.69    5925.63  86.2  10.2  90 3.503 2.395 node11[3,1,1]
98.12  200448   0.007   0.003   0.005   0.019   55.79   2448    944  32.84     641.16    5925.53  86.8  10.1  84 3.456 2.394 node11[0,0,0]
98.31  200832   0.007   0.003   0.003   0.019   49.36   2507    875  32.37     532.45    5925.43  86.2  10.0  90 3.531 2.395 node11[3,1,1]
98.50  201216   0.006   0.002   0.003   0.017   49.74   2622    941  31.03     490.22    5925.34  78.8   9.0  84 3.463 2.395 node11[0,0,0]
98.68  201600   0.006   0.002   0.002   0.016   43.20   2773    861  32.28     392.25    5925.24  77.1   8.8  90 3.547 2.394 node11[3,1,1]
98.87  201984   0.005   0.001   0.002   0.014   41.43   2870    920  31.29     344.59    5925.17  74.8   8.8  84 3.466 2.395 node11[0,0,0]
99.06  202368   0.006   0.001   0.001   0.013   34.15   3052    846  34.18     253.63    5925.09  84.3   9.3  90 3.548 2.394 node11[3,1,1]
99.25  202752   0.005   0.001   0.001   0.011   30.80   3021    797  31.89     204.03    5925.03  62.7   7.1  84 3.474 2.395 node11[0,0,0]
99.44  203136   0.005   0.001   0.001   0.011   23.08   3093    657  32.15     125.87    5924.96  66.8   7.8  90 3.565 2.394 node11[3,1,1]
99.62  203520   0.004   0.001   0.000   0.008   17.69   2930      4  31.02      83.21    5924.91  66.3   7.7  83 3.462 2.394 node11[0,0,0]
99.81  203904   0.004   0.001   0.000   0.008    8.67   3056      0  33.56      28.12    5924.86  69.5   8.3  88 3.418 2.394 node11[3,1,1]
Peak Performance =    6036.02 GFlops /  1509.00 GFlops per node
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR00L2L4      204288   384     2     2             959.71            5.92245e+03
HPL_pdgesv() start time Fri Jun 28 09:32:07 2019

HPL_pdgesv() end time   Fri Jun 28 09:48:06 2019

        HPL Efficiency by CPU Cycle   87.592%
        HPL Efficiency by BUS Cycle   67.048%
--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=        0.0038237 ...... PASSED
================================================================================

Finished      1 tests with the following results:
              1 tests completed and passed residual checks,
              0 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.
```
#  ---END--- 
