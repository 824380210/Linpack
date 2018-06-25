#  setup node with hugepage settings 
```
chdef c4 -p addkcmdline="hugepagesz=1G hugepages=80 default_hugepagesz=1G"
nodeset c4 osimage=rhels7.4-x86_64-netboot-compute
rsetboot c4 net -u
rpower c4 boot
nodestat c4
```

### hugepages=80  is for 96G memory compute node only  ,you may need to update base on the compute node's Total Memory 

# update the compute node with necessary packages 
```
[root@mgt33 ~]# pscp /root/florian/hpl_hugepage/local.repo c4:/etc/yum.repos.d/
cfdv3-096g-158: done
cfdv3-096g-157: done
cfdv3-096g-159: done
cfdv3-096g-161: done
cfdv3-096g-160: done
cfdv3-096g-163: done
cfdv3-096g-162: done
cfdv3-096g-165: done
cfdv3-096g-166: done
cfdv3-096g-164: done
cfdv3-096g-167: done
cfdv3-096g-168: done
[root@mgt33 ~]# cat /root/florian/hpl_hugepage/local.repo
[base]
name=rhels74
baseurl=http://mgt/install/rhels7.4/x86_64/
enabled=1
gpgcheck=0
[root@mgt33 ~]#



[root@mgt33 hpl_hugepage]# cat setup_node
#!/bin/bash

yum install -y numactl
yum install -y cpupowerutils
yum install -y libhugetlbfs-utils

hugeadm --create-global-mounts --set-recommended-shmmax
cpupower frequency-set -g performance
[root@mgt33 hpl_hugepage]# pscp setup_node c4:/root/
cfdv3-096g-158: done
cfdv3-096g-157: done
cfdv3-096g-159: done
cfdv3-096g-160: done
cfdv3-096g-162: done
cfdv3-096g-161: done
cfdv3-096g-164: done
cfdv3-096g-163: done
cfdv3-096g-165: done
cfdv3-096g-166: done
cfdv3-096g-167: done
cfdv3-096g-168: done
[root@mgt33 hpl_hugepage]#


[root@mgt33 hpl_hugepage]# psh c4 bash /root/setup_node



```

# update the HPL.dat file 
```
Peak Performance =   21732.71 GFlops /  1811.06 GFlops per node
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR00L2L4      353664   384     3     4            1370.88            2.15123e+04

```
# update the hostfile  (should be change base on the compute name )

```
[root@cfdv3-096g-160 cluster]# cat hostfile
cfdv3-096g-157
cfdv3-096g-158
cfdv3-096g-159
cfdv3-096g-160
cfdv3-096g-161
cfdv3-096g-162
cfdv3-096g-163
cfdv3-096g-164
cfdv3-096g-165
cfdv3-096g-166
cfdv3-096g-167
cfdv3-096g-168

```
# copy the xhpl file to compute node 

```
[root@mgt33 cluster]# md5sum xhpl
fdc1e760bd838a8b5b5f5a1d45083df6  xhpl
[root@mgt33 cluster]# pwd
/root/cluster
[root@mgt33 cluster]# pscp xhpl c4:/root/peter/cluster/



``` 
#  run the xhpl scrips 


```
[root@cfdv3-096g-160 cluster]# cat 12node.sh
#source ./edr_env.sh
fmt=`date +%Y%m%d%H%M%S`
mount | grep mgt >/dev/null
if [ $? -ne 0 ];then
        echo -e "Start to mount the mgt node for log store "
        mount mgt:/install /install
fi
mount | grep mgt
#
#mpirun -genv I_MPI_FABRICS=dapl -machinefile hostfile   -genv I_MPI_FALLBACK=disable -genv I_MPI_OFA_ADAPTER_NAME='mlx5_0' -np 2 -ppn 1 /opt/intel/compilers_and_libraries_2017.5.239/linux/mkl/benchmarks/mp_linpack/xhpl_intel64_dynamic | tee /install/linpack-${fmt}.log
mpirun -genv I_MPI_FABRICS=dapl -machinefile hostfile -genv  I_MPI_DEBUG=5 -genv HPL_LARGEPAGE=2  -genv I_MPI_FALLBACK=disable -genv I_MPI_OFA_ADAPTER_NAME='mlx5_0' -np 12 -ppn 1 ./xhpl| tee /install/linpack-${fmt}.log
# mpirun -genv I_MPI_FABRICS=dapl -genv I_MPI_FALLBACK=disable -genv I_MPI_OFA_ADAPTER_NAME='mlx5_0'  -machinefile hostfile -np 2 -ppn 1 /opt/intel/compilers_and_libraries_2018.1.163/linux/mkl/benchmarks/mp_linpack/xhpl_intel64_static | tee /install/static_74_edr.log
echo -e "LOG FILE IS  /install/linpack-${fmt}.log  \n"


[root@cfdv3-096g-160 cluster]# md5sum xhpl
fdc1e760bd838a8b5b5f5a1d45083df6  xhpl
[root@cfdv3-096g-160 cluster]#

```
### -genv  I_MPI_DEBUG=5   for more debug message purpose 
### -genv HPL_LARGEPAGE=2  ???? (Will update when I know it  )

```
HPL_LARGEPAGE
	

Defines the memory mapping to be used for the Intel Xeon processor.
	

0 or 1:

    0 - normal memory mapping, default.

    1 - memory mapping with large pages (2 MB per page mapping). It may increase performance.


```
[HPL_LARGEPAGE info ](https://software.intel.com/en-us/mkl-linux-developer-guide-environment-variables)

# the source code for the linpack run 
## xhpl code is a special version ,and not the GA version from Intel Parallel studio 


```
[root@mgt33 cluster]# pwd
/root/cluster
[root@mgt33 cluster]# ll
total 1828
-rwxr-xr-x 1 root root    1021 Jun 25 13:59 12node.sh
-rwxr-xr-x 1 root root     644 Jun 25 13:59 edr_env.sh
-rwxr-xr-x 1 root root     180 Jun 25 13:59 hostfile
-rwxr-xr-x 1 root root    1155 Jun 25 13:59 HPL.dat
-rw-r--r-- 1 root root    1133 Jun 25 13:59 HPL.dat.12
-rwxr-xr-x 1 root root    1155 Jun 25 13:59 HPL.dat.oc2
-rwxr-xr-x 1 root root    1072 Jun 25 13:59 run_2node_EDR.sh
-rwxr-xr-x 1 root root     856 Jun 25 13:59 run_2node.sh
-rwxr-xr-x 1 root root     554 Jun 25 13:59 tools_cluster.sh
-rwxr-xr-x 1 root root 1832768 Jun 25 13:59 xhpl
[root@mgt33 cluster]#

```

