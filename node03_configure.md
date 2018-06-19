# the configuration of the node03 is 
```

[root@mgt1 ~]# lsdef node03
Object name: node03
    arch=x86_64
    bmc=node03-xcc
    chain=runcmd=bmcsetup,shell
    cpucount=96
    cputype=Intel(R) Xeon(R) Platinum 8160 CPU @ 2.10GHz
    currchain=boot
    currstate=netboot rhels7.4-x86_64-compute
    disksize=sda:480GB
    groups=21perswitch,ipmi,compute,all,lab,CPOMxxxxx,MFGxxxxx,4nodeperrack
    installnic=mac
    ip=172.20.101.3
    mac=08:94:ef:4e:fb:e0
    memory=193081MB
    mgt=ipmi
    mpa=smm02
    mtm=7X21CTO1WW
    netboot=xnba
    nfsserver=172.20.0.1
    ondiscover=nodediscover
    os=rhels7.4
    postbootscripts=otherpkgs
    postscripts=syslog,remoteshell,syncfiles
    primarynic=mac
    profile=compute
    provmethod=myopa74
    serial=J3002DTH
    serialflow=hard
    serialport=0
    serialspeed=115200
    slotid=1
    status=booted
    statustime=05-09-2018 17:02:54
    supportedarchs=x86,x86_64
    switch=switch1
    switchport=51
    updatestatus=synced
    updatestatustime=01-12-2018 16:15:04
```
