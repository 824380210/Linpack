# 安装parallel_studio_XE_2019u3版本
#####  2019-03-13 pengcz1@lenovo.com
### 1 安装操作系统，使用默认的xcat osimage模板rhels7.6-x86_64-install-compute
### 2 安装所需要的依赖包
```
[root@n01 ~]# yum install kernel-devel.x86_64 -y
[root@n01 ~]# yum install /lib64/ld-lsb-x86-64.so.3 -y
[root@n01 ~]# yum install gcc -y
[root@n01 ~]# yum install gtk2-devel gtk3-devel libXScrnSaver-devel gcc-c++ -y
[root@n01 ~]# yum install  xorg-x11-server-Xorg.x86_64 -y

```
### 3  安装parallel studi安装parallel studio XE 2019 update 3
```

1 : 解压软件包  tar zxvf 2019u3.tgz
2 : 进入对应目录并执行install.sh脚本 
[root@n01 ~]# cd parallel_studio_xe_2019_update3_cluster_edition/
[root@n01 parallel_studio_xe_2019_update3_cluster_edition]# ./install.sh
a: 在Welcome中按回车继续 
b: 在license中输入accept继续 
c: 在是否允许收集信息中选择2，拒绝
d: 检查是否满足安装要求（参考第二点的依赖包）的时候看有否报问题，如有请解决（正常应该不会报问题了）  
e: 在Licnese Activation中选择2 ，使用2. Activate with license file, or with Intel(R) Software License Manager
f: 在选择是离线激活还是intel的license manager激活的时候选择2 2. Use Intel(R) Software License Manager to find an existing license file
g: 在提示输入license server的时候输入：
    Please type the port@host for license server: 27009@172.20.103.2
    Activation completed successfully.
h: 在配置集群安装的时候选择默认  1. Finish configuring installation target [ default ]
i: 在提示32位库缺失的时候选择忽略 -- 32-bit libraries not found ->    1. Skip prerequisites [ default ]
j: 开始安装，直到完成安装
l：安装完成，检查目录/opt/intel （默认目录）

[root@n01 intel]# ls
advisor                             ipp
advisor_2019                        itac
advisor_2019.3.0.591490             itac_2019
bin                                 itac_latest
clck                                lib
clck_latest                         licenses
compilers_and_libraries             man
compilers_and_libraries_2019        mkl
compilers_and_libraries_2019.3.199  mpirt
conda_channel                       parallel_studio_xe_2019
daal                                parallel_studio_xe_2019.3.062
debugger_2019                       performance_snapshot
documentation_2019                  performance_snapshots
ide_support_2019                    performance_snapshots_2019.3.0.591499
imb                                 pstl
impi                                samples_2019
include                             tbb
inspector                           vtune_amplifier
inspector_2019                      vtune_amplifier_2019
inspector_2019.3.0.591484           vtune_amplifier_2019.3.0.591499
intelpython3

```
### 安装前提要求
```

需要在本地网络中安装intel license manager ，并运行
需要有intel 的license key 授权

# 检查intel license manager是否运行，看lmgrd进程
[root@n02 ~]# ps aux | grep lmgrd
root      55564  0.0  0.0  41408  2268 ?        S    Mar12   0:00 ./lmgrd -c /opt/intel/serverlicenses/l_LPV7WZLF_1.lic -l ./lmgrd.log
root      55565  0.0  0.0 123404  3092 ?        Ssl  Mar12   0:04 INTEL -T n02 11.15 3 -c :/opt/intel/serverlicenses/l_LPV7WZLF_1.lic: -srv EApXe869T5kBoF7cxUEm75QzhCEooH4yRh0ctf7Tx01gBWiSgHpwe3VXlVNRSf2 -daemon_port 6f67 --lmgrd_start 5c881699 -vdrestart 0
root     172310  0.0  0.0 112712   976 pts/1    S+   06:46   0:00 grep --color=auto lmgrd
# 检查lmgrd的监听端口，在这里是默认的27009端口
[root@n02 ~]# ss -ltp | grep lmgrd
LISTEN     0      128       :::27009                   :::*                     users:(("INTEL",pid=55565,fd=0),("lmgrd",pid=55564,fd=0))
[root@n02 ~]#


```

# 在这里结束 ！！！
