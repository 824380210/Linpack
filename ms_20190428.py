#!/usr/local/bin/python3.6
#
#
# step 1 : read the chassis node MAC and Locations 
# step 2 : check the node's IP
#
import subprocess
import logging
id_ip= {    "3":"172.30.101.1",
            "4":"172.30.101.2", 
            "5":"172.30.101.3", 
            "6":"172.30.101.4", 
            "7":"172.30.101.5", 
            "8":"172.30.101.6", 
            "9":"172.30.101.7", 
            "10":"172.30.101.8", 
            "11":"172.30.101.9", 
            "12":"172.30.101.10", 
            "13":"172.30.101.11", 
            "14":"172.30.101.12", 
            "27":"172.30.101.13", 
            "28":"172.30.101.14", 
            "29":"172.30.101.15", 
            "30":"172.30.101.16", 
            "31":"172.30.101.17", 
            "32":"172.30.101.18", 
            "33":"172.30.101.19", 
            "34":"172.30.101.20", 
            "35":"172.30.101.21", 
            "36":"172.30.101.22", 
            "37":"172.30.101.23", 
            "38":"172.30.101.24" 
            }
#
id_hostname = {
               "3":"node01.cluster",
               "4":"node02.cluster",
               "5":"node03.cluster",
               "6":"node04.cluster",
               "7":"node05.cluster",
               "8":"node06.cluster",
               "9":"node07.cluster",
               "10":"node08.cluster",
               "11":"node09.cluster",
               "12":"node10.cluster",
               "13":"node11.cluster",
               "14":"node12.cluster",
               "27":"node13.cluster",
               "28":"node14.cluster",
               "29":"node15.cluster",
               "30":"node16.cluster",
               "31":"node17.cluster",
               "32":"node18.cluster",
               "33":"node19.cluster",
               "34":"node20.cluster",
               "35":"node21.cluster",
               "36":"node22.cluster",
               "37":"node23.cluster",
               "38":"node24.cluster"
               }

def myrun_cmd( cmd,timeout=10 ):
    proc = subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout)
    if proc.returncode != 0:
        raise Exception("cmd run failed with {}".format(cmd))
    else:
        return(proc.stdout)
#
#cmd = "arp | grep f0:1d:bc | awk '{print $1 }'| grep 192.168"
def get_ip_by_mac(mac_address):
    mac = mac_address.lower()
    cmd = " arp | grep " + mac  + " | awk '{print $1}' | head -n 1 "
    rsp  = myrun_cmd(cmd,timeout=10)
    return rsp.strip()
# update the arp table with nmap scan
def update_arp():
    cmd1 = "nmap -p22 --system-dns 192.168.11.0/24"
    cmd2 = "nmap -p22 --system-dns 192.168.14.0/24"
    proc1 = subprocess.run(cmd1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    proc2 = subprocess.run(cmd2,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#

# get the mac to IP mapping due to DHCP reason
mac2ip = {}
def create_mac_ip():
    cmd = "arp | grep 28:16|awk '{print$1,$3}'"
    rsp = myrun_cmd(cmd,timeout=5)
    for line in rsp.decode().split('\n'):
        if "28:16" in line:
            ip,mac  = line.split()
            new_ip  = ip.strip()
            new_mac = mac.strip()
            mac2ip[new_mac] = new_ip
def set_compute_node_passwordless(sid):
    print("run passwordless setting on node in Slot {}".format(sid))
    ip =  id2current_IP[sid]
    cmd = "/usr/bin/expect /root/bin/set_compute_node_passwordless   " + ip
    subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#   
def verify_compute_node_passwordless(sid):
    print("verify passwordless seting on node in Slot {}".format(sid))
    ip =  id2current_IP[sid]
    print("ip is  {}".format(ip))
    cmd = "ssh " + ip  + " ls -l /dfcxact/product/common/linpack "
    print(cmd)
    rsp = myrun_cmd(cmd)
    if "ssh" in rsp.decode():
        print("ip {} is passwordless ready ".format(ip))
#
update_arp()
create_mac_ip()
cmd = "arp | grep f0:1d:bc | awk '{print $1 }'| grep 192.168"
rsp = myrun_cmd(cmd)
RM_IP = rsp.decode().strip()
print("Find MS rack manager IP is {}".format(RM_IP))
#
example= """
WcsCli# show manager inventory
| SW Port | Port State | Present  |  Slot Id   |        MAC1        | Completion Code
|    1    |     ON     |  False   |     --     |         --         | DeviceNotPresent
|    2    |     ON     |  False   |     --     |         --         | DeviceNotPresent
|    3    |     ON     |   True   |      3     | 28:16:A8:FD:13:DA  |     Success
|    4    |     ON     |   True   |      4     | 28:16:A8:FD:14:D1  |     Success
|    5    |     ON     |   True   |      5     | 28:16:A8:FD:17:64  |     Success


"""
cmd = "/root/bin/get_chassis_mac " + RM_IP + "|grep True"
node_info =  myrun_cmd(cmd)
for line in node_info.decode().split('\r\n'):
    print(line)
nodelist = []
id2current_IP = {}
node_count = 0
for line in node_info.decode().split(' \r\n'):
    #print(line)
    if 'True' in line and '28:16' in line:
        _,SW_Port,port_status,present,slot_id,mac,complete_code = line.split('|')
        ip = get_ip_by_mac(mac)
        server_ip = ip.decode()
        sid = slot_id.strip()
        id2current_IP[sid]=server_ip
        #for k,v in id2current_IP.items():
        #    print("slot id is {} and IP is {}".format(k,v))
        #new_ip = tb_hosts[slot_id.strip()]
        #print("The Server on Slot {} with MAC:{},IP is {:<15}, linpack IP should be set to {}".format(slot_id,mac,server_ip,new_ip))
        set_compute_node_passwordless(sid)
        verify_compute_node_passwordless(sid)
        node_count += 1
        print("verify node is {} node ".format(node_count))
for k,v in id2current_IP.items():
    print("ID is {} and IP is {:<15}".format(k,v))
#print(node_info)
#for item in tb_hosts.keys():
#    print("slot id is {} and the new IP is {}".format(item,tb_hosts[item])) 
# start to set the hostname of the compute node
def set_hostname(slot_id):
    hostname = id_hostname[slot_id]
    ip = id2current_IP[slot_id]
    cmd = " ssh " + ip + "  hostname  " + hostname
    rsp =  myrun_cmd(cmd)
#
#  read the hostame of the compute node
def get_hostname(slot_id):
    ip = id2current_IP[slot_id]
    cmd = " ssh " + ip + "  hostname "
    rsp =  myrun_cmd(cmd)
    if "node" in rsp.decode():
        print("the compute node hostname is {}".format(rsp.decode().strip()))
    else:
        raise Exception("hostname setup failed in compute node IP {} with Slot ID {}".format(ip,slot_id))
def set_linpack_ip(slot_id):
    ip = id2current_IP[slot_id]
    new_ip = id_ip[slot_id]
    cmd1 =  "ssh  " + ip  +  "  \"   if ! ip a | grep " + new_ip + ";" + " then   ip addr  add dev eth0 " +  new_ip +"/16 "+ ";" +"fi\""
    cmd = "ssh  " + ip  + "  ip addr  add dev eth0 " +  new_ip +"/16 "
    print(cmd1)
    rsp =  myrun_cmd(cmd1)
#  check the linpack ip with hostname
def check_linpack_ip(slot_id):
    ip  = id_ip[slot_id]
    cmd = "ping -c 1 " + ip
    rsp =  myrun_cmd(cmd)
    if  "1 packets transmitted, 1 received" not in rsp.decode():
        raise Exception("Linpack IP not work as expect in {} ,Slot ID {}".format(ip,slot_id))
    else:
        print("host {} setting ok ".format(ip))
# check the linpack environment 
for k in  id2current_IP.keys():
    set_hostname(k)
    get_hostname(k)
    set_linpack_ip(k)
    check_linpack_ip(k)
#
#
# start to sync the /etc/hosts to all compute node 
#cmd = 'pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/HPL.dat.24 /root/HPL/HPL.dat "'
#cmd = 'pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/hosts  /etc/hosts "'
#rsp =  myrun_cmd(cmd)

# start to sync the hostfile to all compute node
#cmd = 'pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/hostfile  /root/HPL/ "' 
#rsp =  myrun_cmd(cmd)
# start to sync the HPL.dat file to all compute node 
#cmd = 'pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/HPL.dat.24 /root/HPL/HPL.dat "'
#rsp =  myrun_cmd(cmd)
# start to sync the cluster levle scripts to all compute node 
#cmd = 'pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/run_smp_24  /root/HPL/ "'
#rsp =  myrun_cmd(cmd)
# start to snc the cluster lelve scripts for 10 hours long time stress test to all compute node 
#cmd = 'pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/run_smp_24_10hrs  /root/HPL/ "'
#rsp =  myrun_cmd(cmd)
#
cmds = []
cmds.append('pdsh -w 172.30.101.[1-24] "cd /root; tar zxvf /dfcxact/product/common/linpack/HPL.tgz"')
cmds.append('pdsh -w 172.30.101.[1-24] "echo 0 > /sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages"')
cmds.append('pdsh -w 172.30.101.[1-24] "echo 92 > /sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages"')
cmds.append('pdsh -w 172.30.101.[1-24] "echo 0 > /sys/devices/system/node/node1/hugepages/hugepages-1048576kB/nr_hugepages"')
cmds.append('pdsh -w 172.30.101.[1-24] "echo 92 > /sys/devices/system/node/node1/hugepages/hugepages-1048576kB/nr_hugepages"')
cmds.append('pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/hosts  /etc/hosts "')
cmds.append('pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/hostfile  /root/HPL/ "')
cmds.append('pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/HPL.dat.24 /root/HPL/HPL.dat "')
cmds.append('pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/run_smp_24  /root/HPL/ "')
cmds.append('pdsh -w 172.30.101.[1-24] "scp /dfcxact/product/common/linpack/run_smp_24_10hrs  /root/HPL/ "')
#
for cmd in cmds:
    rsp =  myrun_cmd(cmd)
#
print("Linpack environment is ready for cluster level linpack test now ")
