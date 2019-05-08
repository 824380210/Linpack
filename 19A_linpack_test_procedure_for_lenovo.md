# BR 19A Linpack test procedure for Lenovo scalable Infrustructure 
####
####

#### diskless image 
```
[root@mgt myedr741]# md5sum kernel initrd-stateless.gz rootimg.cpio.gz
36eff2be463ab8e70518c802647a96c5  kernel
8d5a8be5fa4299dcc1c10b6a004d686a  initrd-stateless.gz
19662f65fe68bceee6a14c065e480516  rootimg.cpio.gz


[root@mgt myedr741]# md5sum /tmp/edr76.tgz
e036ab1ce15bc775da8d93f85df9aeac  /tmp/edr76.tgz

```
#### deploy the diskless for the compute node 
```
 nodeset n01-n02 osimage=myedr741; rsetboot n01-n02 net -u ;   rpower  n01-n02 reset

```

#### update the Hugepage settings for all compute node after the compute node is up with diskless image 
```
# here is the example in my lab with 16G DIMM install * 12pcs = 192GB
# customer order should be change base on the Memory size in compute node 
# check the /root/HPL/enable_hugepages for detail
# it should be keep 8G memory for the OS 

[root@mgt ~]# psh n01-n02 /root/HPL/enable_hugepages

[root@mgt ~]# psh n01-n02 free -g
n01:               total        used        free      shared  buff/cache   available
n01: Mem:            188         180           5           1           1           5
n01: Swap:             0           0           0
n02:               total        used        free      shared  buff/cache   available
n02: Mem:            188         179           6           1           1           6
n02: Swap:             0           0           0


```

#  login a compute node and start check HPL linpack test parameters
```
[root@n01 ~]# cd HPL/
[root@n01 HPL]# cat hostfile
n01
n02

# make sure all compute node use the same HPL.dat file (so same parameters )

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


```
#  make sure all interface is bring up 
```
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

[root@n01 HPL]# iblinkinfo | grep Up
      0xec0d9a03003d62be      4    1[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       2   17[  ] "MF0;SB7700:MSB7700/U1" ( )
      0x248a070300928186      3    1[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       2   36[  ] "MF0;SB7700:MSB7700/U1" ( )
           2   17[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       4    1[  ] "n02 HCA-1" ( )
           2   18[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       1    1[  ] "n01 HCA-1" ( )
           2   36[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       3    1[  ] "mgt mlx5_0" ( )
      0xec0d9a03003d677a      1    1[  ] ==( 4X      25.78125 Gbps Active/  LinkUp)==>       2   18[  ] "MF0;SB7700:MSB7700/U1" ( )
[root@n01 HPL]#



```
#  check the scripts ,update the parameters base on the real order 
```
[root@n01 HPL]# cat edr2node.sh
PATH=$PATH:/root/HPL:
export LD_LIBRARY_PATH=/root/HPL

export I_MPI_FALLBACK=disable
export I_MPI_FABRICS=dapl
export HPL_HWPREFETCH=1
export HNAME=`hostname`
export I_MPI_OFA_ADAPTER_NAME='mlx5_0'
mpirun -genvall -np 4 -ppn 2 -f hostfile    /root/HPL/run_TLP_sky  | tee -a 2node_cluster_20190508.log

# -ppn = 2 ,so all compute node will run 2 xhpl process 
# -np = compute node number * 2 ,for example .2 compute node. so the -np =4 
```
# run the scripts  

```
[root@n01 HPL]# bash edr2node.sh

```
#  check the log , CPU Cycle >70% and BUS Cycle >64% 
```
[root@n01 HPL]#  cat 2node_cluster_20190508.log
...
Peak Performance =    4645.32 GFlops /  1161.33 GFlops per node
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR00L2L4      204288   384     2     2            1281.68            4.43468e+03
HPL_pdgesv() start time Wed May  8 10:19:50 2019

HPL_pdgesv() end time   Wed May  8 10:41:12 2019

        HPL Efficiency by CPU Cycle   85.552%
        HPL Efficiency by BUS Cycle   69.175%
--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=        0.0038237 ...... PASSED
================================================================================
#  CPU Cycle >70% and BUS Cycle >64% should be treate as PASS 

```
#  if Fail in linpack ,run the single node linpack as we do befoer,thanks 
