#   Debug the MicroSoft Linpack Test 


# if we failed in the 24 node group Level ( same as we said as Rack Level ) Linpack Test,then try to do the single node linpack as below

# Single node level stress test procedure 
### 1: login the compute node 
```
[root@L1linux97146 bin]# ssh 192.168.14.41
root@192.168.14.41's password:                         <=== the default password is passw0rd 
Last login: Thu Jun 13 06:36:13 2019 from gateway

```
### 2: extract the HPL.tgz to the root directory 

```
[root@localhost ~]# tar zxvf /dfcxact/product/common/linpack/HPL.tgz
./HPL/
./HPL/run_TLP_sky
./HPL/run_smp
./HPL/HPL.dat
./HPL/xhpl_lrz
./HPL/libmpi.so
./HPL/mpirun
./HPL/mpivars.sh
./HPL/mpiexec.hydra
./HPL/pmi_proxy
```

### 3: enable the hugepage settings 
```
[root@localhost ~]# cd HPL
[root@localhost HPL]# bash  /dfcxact/product/common/linpack/enable_hugepages
```
### 4: update the HPL.dat 
```
[root@localhost HPL]# vim HPL.dat



```
### 5: run the stress test 
```
[root@localhost HPL]# bash run_smp |tee  bad_mem_node3.log
```
### 6: open another terminal to monitor the /var/log/message output 
###### very import in step 6 to capture the errors info 
```
[root@L1linux97146 ~]# ssh 192.168.14.41
root@192.168.14.41's password:
Last login: Thu Jun 13 06:37:08 2019 from gateway
[root@localhost ~]# tailf /var/log/messages
Jun 13 06:37:08 localhost systemd: Starting User Slice of root.
Jun 13 06:37:08 localhost systemd-logind: New session 4 of user root.
Jun 13 06:37:08 localhost systemd: Started Session 4 of user root.
```

# if we can not find out the failed issue in the singel node linpack in 1 loop ,then try to run the single node linpack for more loop so it can get enough stress ,see example for 30 loop single node linpack test 
```
Example scripts to run 5 hrs 

[root@L1linux97146 ~]# cat 5hr_linpack.sh
#!/bin/bash
cd /root
tar xzvf  /dfcxact/product/common/linpack/HPL.tgz
cd HPL/
sed -i 's/101760       Ns/144384       Ns/g' HPL.dat
bash /dfcxact/product/common/linpack/enable_hugepages
#bash run_smp | tee /dfcxact/mtsn/
name=`ifconfig eth0 | grep ether |awk '{print $2}'|sed  's/://g'`
hname="MAC${name}"
for a in `seq 1 30`
do
fmt=` date +%Y%m%d%H%M%S`
bash run_smp | tee /dfcxact/mtsn/MAC_${name}_${fmt}.log
done





```


## exmaple of the failed message 
```
Jun 14 20:03:13 localhost kernel: mce: [Hardware Error]: Machine check events logged
Jun 14 20:03:13 localhost kernel: EDAC MC0: 1 CE memory read error on CPU_SrcID#0_MC#0_Chan#0_DIMM#0 (channel:0 slot:0 page:0x6c01e4 offset:0x800 grain:32 syndrome:0x0 -  err_code:0101:0090 socket:0 imc:0 rank:0 bg:2 ba:2 row:8d49 col:210)
Jun 14 20:03:13 localhost mcelog: Running trigger `dimm-error-trigger'
Jun 14 20:03:13 localhost mcelog: Corrected memory errors on page 6c01e4000 exceed threshold 10 in 24h: 10 in 24h
Jun 14 20:03:13 localhost mcelog: Location SOCKET:0 CHANNEL:0 DIMM:? []
Jun 14 20:03:13 localhost mcelog: Running trigger `page-error-trigger'
Jun 14 20:03:13 localhost mcelog: Offlining page 6c01e4000
Jun 14 20:03:13 localhost mcelog: corrected DIMM memory error count exceeded threshold: 10 in 24h
Jun 14 20:03:13 localhost mcelog: Corrected memory errors on page 6c01e4000 exceed threshold 10 in 24h: 10 in 24h
Jun 14 20:03:13 localhost mcelog: Location: SOCKET:0 CHANNEL:0 DIMM:? []
Jun 14 20:03:13 localhost mcelog: Location: SOCKET:0 CHANNEL:0 DIMM:? []
Jun 14 20:03:13 localhost kernel: soft offline: 0x6c01e4: migration failed 1, type 2fffff00008000
Jun 14 20:03:13 localhost kernel: ------------[ cut here ]------------
Jun 14 20:03:13 localhost kernel: kernel BUG at mm/hugetlb.c:1261!
Jun 14 20:03:13 localhost kernel: invalid opcode: 0000 [#1] SMP
Jun 14 20:03:13 localhost kernel: Modules linked in: arc4 md4 nls_utf8 cifs ccm rpcsec_gss_krb5 auth_rpcgss nfsv4 dns_resolver nfs lockd grace fscache sha512_ssse3 sha512_generic drbg ansi_cprng sd_mod sg ib_isert(OE) iscsi_target_mod target_core_mod crc_t10dif crct10dif_generic skx_edac intel_powerclamp coretemp ib_srpt(OE) intel_rapl ib_srp(OE) iosf_mbi rpcrdma(OE) svcrdma(OE) scsi_transport_srp(OE) xprtrdma(OE) kvm_intel qat_c62x rdma_ucm(OE) intel_qat kvm ib_iser(OE) irqbypass libiscsi crc32_pclmul dh_generic ghash_clmulni_intel ahci ib_ipoib(OE) nvme ib_ucm(OE) aesni_intel libahci scsi_transport_iscsi rsa_generic lrw iTCO_wdt gf128mul authenc iTCO_vendor_support glue_helper ablk_helper ib_uverbs(OE) wmi mei_me libata i2c_i801 ib_umad(OE) nvme_core i2c_core lpc_ich ftdi_sio mei cryptd shpchp pcspkr rdma_cm(OE) ipmi_si
Jun 14 20:03:13 localhost kernel: ipmi_devintf nfit ib_cm(OE) ipmi_msghandler libnvdimm iw_cm(OE) tpm_crb acpi_pad acpi_power_meter ip_tables mlx5_ib(OE) ib_core(OE) mlx5_core(OE) mlx_compat(OE) crct10dif_pclmul mlxfw(OE) crct10dif_common devlink crc32c_intel ptp pps_core sunrpc [last unloaded: amifldrv_mod]
Jun 14 20:03:13 localhost kernel: CPU: 77 PID: 1776 Comm: mcelog Tainted: P           OE  ------------   3.10.0-862.el7.x86_64 #1
Jun 14 20:03:13 localhost kernel: Hardware name: Microsoft C201E      /C201E      , BIOS C2010.BS.3F31.GN1 10/02/2018
Jun 14 20:03:13 localhost kernel: task: ffff97fb98070000 ti: ffff97fb457a0000 task.ti: ffff97fb457a0000
Jun 14 20:03:13 localhost kernel: RIP: 0010:[<ffffffffb1be33f4>]  [<ffffffffb1be33f4>] free_huge_page+0x1e4/0x200
Jun 14 20:03:13 localhost kernel: RSP: 0018:ffff97fb457a3d50  EFLAGS: 00010213
Jun 14 20:03:13 localhost kernel: RAX: 0000000000000000 RBX: fffffd055b000000 RCX: 0000000000000012
Jun 14 20:03:13 localhost kernel: RDX: 0000000040000000 RSI: ffffffffb2b92520 RDI: fffffd055b000000
Jun 14 20:03:13 localhost kernel: RBP: ffff97fb457a3d78 R08: ffffffffb2b83ca8 R09: ffff97f04d137f00
Jun 14 20:03:13 localhost kernel: R10: 0000000000000a2e R11: ffff97fb457a3afe R12: ffffffffb2b83c60
Jun 14 20:03:13 localhost kernel: R13: 0000000000000000 R14: 0000000000000000 R15: ffff97fb457a3f18
Jun 14 20:03:13 localhost kernel: FS:  00007f47fc32e740(0000) GS:ffff97fb9c540000(0000) knlGS:0000000000000000
Jun 14 20:03:13 localhost kernel: CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Jun 14 20:03:13 localhost kernel: CR2: 00007f47fc117770 CR3: 0000002fd9e70000 CR4: 00000000007607e0
Jun 14 20:03:13 localhost kernel: DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
Jun 14 20:03:13 localhost kernel: DR3: 0000000000000000 DR6: 00000000fffe0ff0 DR7: 0000000000000400
Jun 14 20:03:13 localhost kernel: PKRU: 55555554
Jun 14 20:03:13 localhost kernel: Call Trace:
Jun 14 20:03:13 localhost kernel: [<ffffffffb2109e2d>] __put_compound_page+0x25/0x28
Jun 14 20:03:13 localhost kernel: [<ffffffffb2109e65>] put_compound_page+0x35/0x174
Jun 14 20:03:13 localhost kernel: [<ffffffffb1ba21e5>] put_page+0x45/0x50
Jun 14 20:03:13 localhost kernel: [<ffffffffb1be80a0>] putback_active_hugepage+0xd0/0xf0
Jun 14 20:03:13 localhost kernel: [<ffffffffb1c13bbb>] soft_offline_page+0x4db/0x580
Jun 14 20:03:13 localhost kernel: [<ffffffffb1e86c65>] store_soft_offline_page+0xa5/0xe0
Jun 14 20:03:13 localhost kernel: [<ffffffffb1e6d3cb>] dev_attr_store+0x1b/0x30



```
