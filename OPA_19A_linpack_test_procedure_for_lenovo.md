# OPA BR19A linpack test procedure for lenovo
#
# diskless image for OPA network 
```
[root@mgt ~]# cd /install/netboot/rhels7.5/x86_64/opa741/
[root@mgt opa741]# md5sum kernel initrd-stateless.gz rootimg.cpio.gz
36eff2be463ab8e70518c802647a96c5  kernel
f350f37053f4b06140a00dde002df96d  initrd-stateless.gz
12e75e45801b27597713baad991bc98a  rootimg.cpio.gz
[root@mgt opa741]# ll
total 708732
-rw------- 1 root root  39883439 May  9 01:32 initrd-stateless.gz
-rwxr-xr-x 1 root root   6635920 May  9 01:32 kernel
-rw-r--r-- 1 root root 679213274 May  9 01:32 rootimg.cpio.gz
[root@mgt opa741]#

[root@mgt opa741]# tar czvf /tmp/opa76_19A.tgz initrd-stateless.gz kernel rootimg.cpio.gz
initrd-stateless.gz
kernel
rootimg.cpio.gz
[root@mgt opa741]# ll /tmp/opa76_19A.tgz
-rw-r--r-- 1 root root 709273123 May  9 03:13 /tmp/opa76_19A.tgz
[root@mgt opa741]# md5sum /tmp/opa76_19A.tgz
612dde01a47e31d5f09903c101651834  /tmp/opa76_19A.tgz


```
#### deploy the diskless image to the compute node 
```
[root@mgt ~]# nodeset n03-n04 osimage=opa741
n03: netboot rhels7.5-x86_64-compute
n04: netboot rhels7.5-x86_64-compute

[root@mgt ~]# rsetboot  n03-n04  net -u
n03: Network
n04: Network

[root@mgt ~]# rpower  n03-n04 reset
n04: reset
n03: reset
[root@mgt ~]#


```
#### enable the hugepage settings for all compute node 
```
[root@mgt ~]# psh n03-n04 "bash /root/HPL/enable_hugepages"
[root@mgt ~]# psh n03-n04 "free -g "
n03:               total        used        free      shared  buff/cache   available
n03: Mem:            188         180           6           1           1           5
n03: Swap:             0           0           0
n04:               total        used        free      shared  buff/cache   available
n04: Mem:            188         181           5           1           1           4
n04: Swap:             0           0           0
[root@mgt ~]#


```

#### bring up the OPA interface by start the opafm service 
```
[root@mgt ~]# ssh n03
Last login: Thu May  9 11:50:46 2019 from mgt.cluster
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
   Xmit Data:                  0 MB Pkts:                   16
   Recv Data:                  0 MB Pkts:                   16
   Link Quality: 5 (Excellent)
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


```

#### check the HPL.dat 
```
[root@n03 HPL]# cat HPL.dat
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


``` 
### check the hostfile (all hostname of compute node that join the linpack test )
```
[root@n03 HPL]# cat hostfile
n03
n04


```
### run the scripts to get the result 

```
[root@n03 HPL]# cat mgt_opa2node.sh
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
mpirun -genvall -np 4 -ppn 2 -f hostfile    /root/HPL/run_TLP_sky  | tee -a 2node_cluster_opa_${fmt}.log
[root@n03 HPL]#

### 
```
[root@n03 HPL]# bash mgt_opa2node.sh
Start to mount the mgt node for log store
mgt:/install on /install type nfs4 (rw,relatime,vers=4.1,rsize=1048576,wsize=1048576,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=172.20.103.3,local_lock=none,addr=172.20.0.1)
Skylake architecture(B) has been selected.
HPL[n03] : HT (2) is enabled.
HPL[n03] : numa node No.  0 is active.
Active Core :    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
Active Numa :    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
...

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0



```
