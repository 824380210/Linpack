# HPL.dat file 
```

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
1            Ps
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

```
# hostfile 
```
node03
node04
```
# parameters for OPA networks
```
[root@node03 cluster]# cat tools_cluster.sh
. /opt/intel/compilers_and_libraries_2018.1.163/linux/mpi/intel64/bin/mpivars.sh  intel64
#. /opt/intel/compilers_and_libraries_2018.1.163/linux/bin/compilervars.sh intel64
#
#export OMP_NUM_THREADS=68
export I_MPI_FALLBACK=disable
#export I_MPI_FABRICS=shm
export I_MPI_FABRICS=shm:tmi
export I_MPI_TMI_PROVIDER=psm2

#export I_MPI_PIN_CELL=core
#export PSM2_IDENTIFY=1
#export PSM2_RCVTHREAD=0
#export HFI_NO_CPUAFFINITY=1
#export I_MPI_PIN_PROCESSOR_LIST=7

#export I_MPI_EAGER_THRESHOLD=128000

export HPL_CHECKSUM=0
export HPL_PIN_PROCESSOR_LIST=3

```

# test Scripts 
```
[root@node03 cluster]# cat run_2node.sh
#!/bin/bash
source ./tools_cluster.sh
# . /root/peter/cluster/tools_cluster.sh
fmt=`date +%Y%m%d%H%M`
echo -e " make sure all OPA port is up and running "
#echo -e "ln -s /usr/lib/systemd/system/opafm.service /etc/systemd/system/multi-user.target.wants/opafm.service"
# systemctl restart opafm.service
# opainfo
# opafabricinfo
#
echo -e "Test log is store in the /tmp/linpack_${fmt}.log"
echo -e "\n\n***********************************************************************************************\n"
mpirun -genvall -f hostfile -np 2 -ppn 1 /opt/intel/compilers_and_libraries_2018.1.163/linux/mkl/benchmarks/mp_linpack/xhpl_intel64_dynamic | tee /tmp/linpack_${fmt}.log
#
echo -e "***********************************************************************************************"
echo -e "\n\n\nTest log is store in the /tmp/linpack_${fmt}.log\n\n\n"



``` 
