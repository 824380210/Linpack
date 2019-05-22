#!/usr/local/bin/python35
# -*- coding: utf-8 -*-
"""
THis scripts is use to setup the whole rack before run the Cluster level linpack test on the MS Gen6 rack 
01: check the Rack Manager IP 
02: check the Rack Manager for the compute node ,and build the SLOT ID to MAC address Mapping and MAC to SLOT ID Mapping
03: check the /var/lib/dhcp/dhcpd.lease file to get the MAC to IP Mapping
04: SLOTID2MAC + MAC2DHCP => ID2DHCP 
05: configure the passwordless from L1 server to compute node (so use same id_rsa,id_rsa.pub,authorized_keys for all compute node )
06: configure the compute node hostname
07: configure the compute node Linpack IP 172.30.101.ID/16
08: configure the hugepages settings for all compute node 
09: extract the HPL.tgz to all compute node's :/root/HPL/
10: update the /etc/hosts for all compute node 
11: 
12:
13:
14:


"""
import sys
import UTP 
import Helper
import logging
import Misc
import sys
import subprocess
import os

# slot ID to MAC,DHCP,Linpack IP,Hostname Mapping
ID2MAC   = {}
MAC2ID   = {}
MAC2DHCP = {}
ID2DHCP  = {}

# support MS gen6 rack type 
support_rack = [24,36,16]

# static Mapping for ID to Linpack IP address
ID2IP = {
        "1":"172.30.101.1",
        "2":"172.30.101.2",
        "3":"172.30.101.3",
        "4":"172.30.101.4",
        "5":"172.30.101.5",
        "6":"172.30.101.6",
        "7":"172.30.101.7",
        "8":"172.30.101.8",
        "9":"172.30.101.9",
        "10":"172.30.101.10",
        "11":"172.30.101.11",
        "12":"172.30.101.12",
        "13":"172.30.101.13",
        "14":"172.30.101.14",
        "15":"172.30.101.15",
        "16":"172.30.101.16",
        "17":"172.30.101.17",
        "18":"172.30.101.18",
        "19":"172.30.101.19",
        "20":"172.30.101.20",
        "21":"172.30.101.21",
        "22":"172.30.101.22",
        "23":"172.30.101.23",
        "24":"172.30.101.24",
        "25":"172.30.101.25",
        "26":"172.30.101.26",
        "27":"172.30.101.27",
        "28":"172.30.101.28",
        "29":"172.30.101.29",
        "30":"172.30.101.30",
        "31":"172.30.101.31",
        "32":"172.30.101.32",
        "33":"172.30.101.33",
        "34":"172.30.101.34",
        "35":"172.30.101.35",
        "36":"172.30.101.36",
        "37":"172.30.101.37",
        "38":"172.30.101.38",
        "39":"172.30.101.39",
        "40":"172.30.101.40",
        "41":"172.30.101.41",
        "42":"172.30.101.42",
        "43":"172.30.101.43",
        "44":"172.30.101.44",
        "45":"172.30.101.45",
        "46":"172.30.101.46",
        "47":"172.30.101.47",
        "48":"172.30.101.48"
        }

# Static Mapping for Slot ID to Hostname 
ID2NAME = {
        "1":"node1.cluster",
        "2":"node2.cluster",
        "3":"node3.cluster",
        "4":"node4.cluster",
        "5":"node5.cluster",
        "6":"node6.cluster",
        "7":"node7.cluster",
        "8":"node8.cluster",
        "9":"node9.cluster",
        "10":"node10.cluster",
        "11":"node11.cluster",
        "12":"node12.cluster",
        "13":"node13.cluster",
        "14":"node14.cluster",
        "15":"node15.cluster",
        "16":"node16.cluster",
        "17":"node17.cluster",
        "18":"node18.cluster",
        "19":"node19.cluster",
        "20":"node20.cluster",
        "21":"node21.cluster",
        "22":"node22.cluster",
        "23":"node23.cluster",
        "24":"node24.cluster",
        "25":"node25.cluster",
        "26":"node26.cluster",
        "27":"node27.cluster",
        "28":"node28.cluster",
        "29":"node29.cluster",
        "30":"node30.cluster",
        "31":"node31.cluster",
        "32":"node32.cluster",
        "33":"node33.cluster",
        "34":"node34.cluster",
        "35":"node35.cluster",
        "36":"node36.cluster",
        "37":"node37.cluster",
        "38":"node38.cluster",
        "39":"node39.cluster",
        "40":"node40.cluster",
        "41":"node41.cluster",
        "42":"node42.cluster",
        "43":"node43.cluster",
        "44":"node44.cluster",
        "45":"node45.cluster",
        "46":"node46.cluster",
        "47":"node47.cluster",
        "48":"node48.cluster"
        }
# Get the Rack Manager IP from the DHCP leases file ,and it use the find_rm way as Jimmy provide but remove some limitations 
def get_rm_ip():
    '''
    check the /var/lib/dhcp/dhcpd.lease file to find out the active Rack Manager IP address 
    example : find_rm.py in UTP 
    '''
    logging.info(' 1:          Find RackManager', section=True)
    rm_ip = ''
    for ip, lease_data in Misc.get_all_dhcp_leases().items():
        mac  = lease_data.get('hardware ethernet')
        if mac.startswith('f01dbc') and lease_data.get('binding state') == 'active':
            logging.info("Found RackManager IP: {} MACAddress:{}".format(ip, mac))
            rm_ip = ip
    if not rm_ip:
        raise Exception("No RackManager IP found in this L1 server")
    else:
        return rm_ip

# myrun_cmd should be replace by Helper.run cmd      
def myrun_cmd( cmd,timeout=30 ):
    proc = subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout)
    if proc.returncode != 0:
        raise Exception("cmd run failed with {}".format(cmd))
    else:
        return(proc.stdout)
#
def get_id2mac(ip):
    '''
    login the Rack manager and run cmd 'show manager inventory'

    '''
    slotid2mac = {}
    mac2slotid = {}
    p = Helper.ssh_run('show manager inventory', ip, 'root', '$pl3nd1D')
    rsp = p.stdout
#    print(rsp) 
    for lines in rsp.split('\r\n'):
        if 'True' in lines and 'Success' in lines:
             _,SW_Port,port_status,present,slot_id,mac,complete_code = lines.split('|')
             #print("{} have {}".format(slot_id,mac))
             mac = mac.strip().replace(':','')
             slot_id = slot_id.strip()
             slotid2mac[slot_id] = mac
             logging.info("slot id is {:2} and mac is {}".format(slot_id,mac))
             mac2slotid[mac] = slot_id
    return (slotid2mac,mac2slotid)


# get the compute node's IP from the lease file 
def get_compute_node_dhcp_ip(ID2MAC):
    mac2dhcp = {}
    for id in sorted(ID2MAC.keys(),key=int):
        mac = ID2MAC[id]
        rsp = Misc.get_dhcp_lease(ID2MAC[id])
        logging.info("Found Slot ID {:2}  with  MAC {} and with IP is {}".format(id,mac,rsp['lease']))
        mac2dhcp[mac]= rsp['lease']
    return mac2dhcp
#


#MAC2DHCP = get_compute_node_dhcp_ip(SLOTID2MAC)
# from SLOTID2MAC ,MAC2DHCP TO GET SLOTID2DHCP DICTIONARY
def get_slotid_to_ip():
    '''
    MAC2ID : only compute node MAC install in rack 
    MAC2DHCP : include the MAC that not the compute node .like Rack manger ,switch and so on
    
    '''
    id2dhcp = {}
    mac_list = list(MAC2DHCP.keys())
    for mac in MAC2ID.keys():
        if mac in mac_list:
            id2dhcp[MAC2ID[mac]] = MAC2DHCP[mac]
        else:
            raise Exception("MAC not found in MAC2DHCP tables")


    return id2dhcp

#
# 
def update4rack_linpack(slotid):
    '''
    from slot ID to get the DHCP IP ,then copy the id_rsa,id_rsa.pub authorized_keys to compute node
    setup the linpack ip 
    tar the linpack tar file 

    '''
def update_passwordless(dict):
    ssh = Helper.SSHClient()
    for id in sorted(dict.keys(),key=int):
        #logging.info("the current compute node in Slot ID {} with IP is  {}".format(id,dict[id]))
        ssh.connect(dict[id], 'root', 'passw0rd',retain_public_key=True)
        cmd = 'ip a | grep  ' + dict[id]
        proc = ssh.run(cmd)

        logging.info("update the passwordless authentication on compute node in SLOT ID {} ".format(id))

# 
# set hostname base on the slot id where the compute node install into the rack
def set_hostname(ID):
    name = ID2NAME[ID]
    IP   = ID2DHCP[ID]
    cmd = "ssh  " + IP  + "    hostname  " + name
    p = myrun_cmd(cmd)

# 
# get hostname by the ID
def get_hostname(ID):
    IP   = ID2DHCP[ID]
    cmd = "ssh  " + IP  + "    hostname  "
    proc =   Helper.run(cmd)
    p    =  proc.stdout
    msg = "slot ID is {:2} and hostname check is {}".format(ID,p.strip())
    logging.info(msg)
#
def update_rsa_to_compute_node(ID):
    """
    update the rsa key to compute node
    """
    IP = ID2DHCP[ID]
    cmd1 = "scp /root/.ssh/id_rsa " + IP + ":/root/.ssh/"
    cmd2 = "scp /root/.ssh/id_rsa.pub " + IP + ":/root/.ssh/"
    cmd3 = "scp /root/.ssh/authorized_keys " + IP + ":/root/.ssh/"
    cmdlist = [cmd1,cmd2,cmd3]
    for cmd in cmdlist:
        Helper.run(cmd)
    msg = "upate keys authentication in compute node : slot ID: {:2} and IP is {}".format(ID,IP)
    logging.info(msg)

def update_linpack_ip(id):
    IP = ID2DHCP[id]
    NIP = ID2IP[id]
    cmd1 = "ssh " + IP +  "   \" if ! ip a | grep  " + NIP  + " ; then ip addr add dev eth0 " + NIP +"/16; fi \" "
    Helper.run(cmd1)
    cmd2 = "ssh " + NIP  + "  ls  "
    Helper.run(cmd2)
    msg = "Linpack IP setup done on the compute node in slot ID {:2} with IP {}".format(id,NIP)
    logging.info(msg)

def linpack_setup(id):
    '''
    Linpack setup include :
    1: extract the HPL.tgz
    2: /etc/hosts update
    3: hugepages scripts run 
    4: 
    '''
    NIP = ID2IP[id]
    cmd =  "ssh " + NIP  + " cd /root; tar zxvf /dfcxact/product/common/linpack/HPL.tgz"
    Helper.run(cmd)
    msg = "update the HPL.tgz file to compute node {}".format(ID2NAME[id])
    logging.info(msg)

def update_hugepages(id):
    NIP = ID2IP[id]
    cmd = "ssh " + NIP  + "  bash /dfcxact/product/common/linpack/enable_hugepages"
    Helper.run(cmd)
    msg = "update the hugepage settings on  compute node {}".format(ID2NAME[id])
    logging.info(msg)


def update_hosts(id):
    NIP = ID2IP[id]
    cmd = "ssh " + NIP  + "  scp  /dfcxact/product/common/linpack/hosts /etc/hosts"
    Helper.run(cmd)
    msg = "update   compute node {}  /etc/hosts for name resolutions ".format(ID2NAME[id])
    logging.info(msg)

def check_support_rack(dict):
    node_number = len(dict.keys())
    if node_number not in support_rack:
        raise Exception("the cureent rack is not in the support list ,check the node is good or check with TE ")

def check_manual_linpack():
    if os.path.exist('manual_linpack'):
        logging.info("xxxxxxxxxxxxxxxxxxxxxx")

def check_memory(id2mac):
    '''
    from ID2MAC get the first blade that install in the rack
    from ID2IP to get the IP of the compute node
    check the compute node install DIMM size
    '''
    #IP = '172.30.101.1'
    #cmd = "ssh 172.30.101.1 dmidecode -t 17 | grep Size | grep MB|uniq"
    ID = list(sorted(id2mac.keys(),key=int))[0]
    IP = ID2IP[ID]
    cmd = " ssh " + IP + "        dmidecode -t 17 | grep Size | grep MB|uniq"
    proc = Helper.run(cmd)
    if '8192' in proc.stdout:
        size = '8G'
    elif '16384' in proc.stdout:
        size = '16G'
    elif '32768' in proc.stdout:
        size = '32G'
    elif '65536' in proc.stdout:
        size = '64G'
    else:
        raise Exception("Not Support Memory install")
    return size  

def create_hostfile(id2mac):
    with open('/tmp/hostfile','w') as fh:
        for id in sorted(id2mac.keys(),key=int):
            msg = "node" + id +"\n"
            fh.write(msg)

    logging.info("hostfile create successfully in /tmp/hostfile")
    ID = list(sorted(id2mac.keys(),key=int))[0]
    IP = ID2IP[ID]
    cmd = "scp /tmp/hostfile  " + IP + ":/root/HPL/"
    proc = Helper.run(cmd)
    logging.info("update hostfile to {} successfully ".format(IP))

def update_hpl_dat(id2mac):
    """
    from ID2MAC to get how many  node installa in the system
    get compute node DIMM Size
    """
    node_num = len(id2mac.keys())
    if node_num not in support_rack:
        raise Exception("Found {0} nodes install in this rack ,and it is not support to run linpack with {0} nodes".format(node_num))
    MSize = check_memory(id2mac)

    fh = "HPL.dat." + MSize +"_" +str(node_num)
    file = '/dfcxact/product/common/linpack/' + fh
    for id in sorted(id2mac.keys(),key=int):
        ip = ID2IP[id]
        cmd = "ssh " + ip  + " \"scp " + file + "  /root/HPL/HPL.dat \""
        proc = Helper.run(cmd)
        logging.info("update HPL.dat to compute node {:2} => {:15} successfully ".format(id,ip))


def get_first_compute_node(id2mac):
    id_list = list(id2mac.keys())
    first_id = sorted(id_list,key=int)[0]
    logging.info("The first compute node  install in SLOT {} and IP is {} ".format(first_id,ID2IP[first_id]))
    return ID2IP[first_id]



def create_linpack_script(id2mac):
    node_num = len(id2mac.keys())
    if os.path.exists('/dfcxact/mtsn/tmp_linpack.log'):
        pass
    msg = """    PATH=$PATH:/root/HPL:
    export LD_LIBRARY_PATH=/root/HPL

    export I_MPI_FALLBACK=disable
    export I_MPI_FABRICS=shm:tcp
    export HPL_HWPREFETCH=1
    export HNAME=`hostname -s`
    """
    msg1 = "mpirun -genvall -np {} -ppn 2 -f hostfile  -genv I_MPI_NETMASK  eth0  /root/HPL/run_TLP_sky  | tee /dfcxact/mtsn/tmp_linpack.log\n".format(node_num*2)
    with UTP.open_file('/tmp/run_linpack.sh',mode='w',scope='l1') as fh:
        fh.write(msg)
        fh.write(msg1)


def upload_linpack_script():
    IP = get_first_compute_node(ID2MAC)
    cmd = "scp  /tmp/run_linpack.sh  " + IP +":/root/HPL/"
    Helper.run(cmd)
    logging.info("Linpack scripts have been upload to {} successfully ".format(IP))

def run_linpack():
    IP = get_first_compute_node(ID2MAC)
    cmd = "ssh  "   + IP + " \"cd /root/HPL/; bash /root/HPL/run_linpack.sh\""
    Helper.run(cmd,timeout=4000)
    logging.info("Linpack scripts have been ==RUN== on {} successfully ".format(IP))

def check_linpack_result():
    cpu_cycle = 0 
    bus_cycle = 0
    logging.info("Check the Rack Level linpack result")
    with open('/dfcxact/mtsn/tmp_linpack.log')  as fh:
        for line in fh.readlines():
            if 'HPL Efficiency by CPU Cycle' in line:
                cpu_cycle = line.split()[5].replace('%','').strip()
                msg1 = line
                logging.info(line)
            if 'HPL Efficiency by BUS Cycle' in line:
                bus_cycle = line.split()[5].replace('%','').strip()
                logging.info(line)
                msg2 = line
            if 'R00L2L' in line:
                logging.info(line)
                msg3  = line

    if int( float( cpu_cycle) ) >65 and int( float( bus_cycle ) ) > 64:
        msg = " Rack Level Linpack Test pass"
        logging.info(msg)
    else:
        msg = "Rack Level Linpack Test FAIL !!!!"
        logging.info(msg)
        logging.info(msg3)
        logging.info(msg1)
        logging.info(msg2)

        raise Exception("Linpack result check Failed ,Wrong test result ")


def main():
    msg = "Only 24 node per rack or 36 node per rack are support now "
    logging.warn(msg,section=True)
    global ID2MAC,MAC2ID,MAC2DHCP,ID2DHCP 
    rm_ip = get_rm_ip()
    
    logging.info("2:  Check  RackManager SLOT ID to MAC ",section=True )
    # Get the Slot ID to MAC mappings and MAC to ID mapping
    ID2MAC,MAC2ID = get_id2mac(rm_ip)
    #for slotid in sorted(ID2MAC.keys(),key=int):
    #    logging.info("compute node in slot {:2}  have MAC {}".format(slotid,ID2MAC[slotid]))
    
    # check_support_rack(ID2MAC)
    create_linpack_script(ID2MAC)
    # sys.exit(0)
    # 
    logging.info("3:  check the MAC to the DHCP IP mappping",section=True)
    MAC2DHCP = get_compute_node_dhcp_ip(ID2MAC)
    logging.info("4:  check the SLOT ID  to the DHCP IP mappping",section=True)
    ID2DHCP = get_slotid_to_ip()
    for id in sorted(ID2DHCP.keys(),key=int):
        msg = "compute node in SLOT ID:{:2}  with DHCP IP is {}".format(id,ID2DHCP[id])
        logging.info(msg)
    #
    #
    logging.info("5:  Update the compute node for SSH passwordless authentications ",section=True)
    update_passwordless(ID2DHCP)
    
    logging.info("5.1 Update all compute node with same L1's id_rsa,authenticated_keys,id_rsa.pub",section=True)
    # update the key authentication on all node  
    for id in sorted(ID2DHCP.keys(),key=int):
        update_rsa_to_compute_node(id)
    
    
    # set compute node hostname 
    #
    logging.info(" 6:  Update the compute node Hostname for MPI linpack run requiremenet ",section=True)
    for id in ID2DHCP.keys():
        set_hostname(id)
    
    
    logging.info(" 6.1  Check the compute node Hostname for MPI process run requirement ",section=True)
    # get the compute node hostname 
    for id in sorted(ID2DHCP.keys(),key=int):
        get_hostname(id)
    
    logging.info ("7: setup the linpack IP for the compute node ",section=True)
    for id in sorted(ID2DHCP.keys(),key=int):
        update_linpack_ip(id) 
    MSize = check_memory(ID2MAC)
    if MSize:
        logging.info("this rack with compute node with {}  DIMM Memory install ".format(MSize),section=True)
    
    logging.info ("8: setup the linpack Hugepages    for the compute node ",section=True)
    for id in sorted(ID2DHCP.keys(),key=int):
        update_hugepages(id)
    
    logging.info ("9: extract  HPL.tgz to  the compute node ",section=True)    
    for id in sorted(ID2DHCP.keys(),key=int):
        linpack_setup(id)
    
    logging.info("10: update the /etc/hosts file for name resolutions ", section=True)
    for id in sorted(ID2DHCP.keys(),key=int):
        update_hosts(id)
    
    logging.info("11: Update the HPL.dat file to all compute node",section=True)
    update_hpl_dat(ID2MAC)
    
    logging.info("12: Update the hostfile file to first compute node ",section=True)
    ip = get_first_compute_node(ID2MAC)
    create_hostfile(ID2MAC)
    
    logging.info("13: Update the linpack scripts to the first compute node  ",section=True)
    upload_linpack_script()
    
    logging.info("14: run the Linpack scripts in compute node ",section=True)
    run_linpack()
    logging.info("15: check the linpack result in L1 server   ",section=True)
    check_linpack_result()
    #

main()    
#check_linpack_result()
