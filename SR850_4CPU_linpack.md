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
# End 
