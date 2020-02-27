#!/usr/bin/env python3 
# 
# CopyRight ? 2016
# Function : Benchmark hpl-calculate (http://hpl-calculator.sourceforge.net/hpl-calculations.php)
# Author: liuhao14@lenovo.com
# Date : 2016-12-24
# Version : 2016-12-24_v1.0
# Version History: 
#    2018-03-19 15:17:02 Bug Fixed . Per Cycle : Operations.
#    2017-08-21 16:56:00 For purley: NB should be 384 , PxQ = total nodes .
import sys
import os
import getopt
import math

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--node", dest="node",action = "store",type="int",
                help="Number of Nodes (e.g. 3168)")
parser.add_option("-p", "--cpu", dest="cpu",action = "store",type="int",default="2",
                help="CPUs per node (e.g. 2) Default=2")
parser.add_option("-c", "--core", dest="core",action = "store",type="int",
                help="Cores Per Node (e.g. 24)")
parser.add_option("-s", "--speed", dest="speed",type="float",
                help="Speed Per Core (GHz) (e.g. 2.5)")
parser.add_option("-m", "--memory", dest="memory",action = "store",type="int",
                help="Memory Per Node (GB) (e.g. 96)")
parser.add_option("-o", "--operations", dest="operations",action = "store",type="int",
                help="Operations Per Cycle (e.g. 16) Default=16")
parser.add_option("-t", "--target", dest="target",action = "store",default="normal",
                help="target: [normal] system or [purley]")
(options, args) = parser.parse_args()

if len(sys.argv) == 1 or options.node is None or options.core is None or options.memory is None or options.speed is None or options.target is None:
    parser.print_help()
    sys.exit(1)



if options.target == 'normal':
    # Rpeak
    # node x core x cpu x cycle
    if options.operations is None:
    	options.operations = 16
    # print the detail information 
    print('Generate the HPL data:'.center(70,'*'))
    print('Number of Nodes        {}'.format(options.node))
    print('CPU per Node           {}'.format(options.cpu))
    print('Cores Per Node         {}'.format(options.core))
    print('Speed Per Core (GHz)   {}'.format(options.speed))
    print('Memory Per Node (GB)   {}'.format(options.memory))
    print('Operations Per Cycle   {}'.format(options.operations))
    print('Product Name:          {}'.format(options.target))
    rpeak = options.node * options.core * options.speed * options.operations
    print('System performance (Rpeak) in GFLOPS'.center(70,'*'))
    # print(int(rpeak))
    def rpeak_value(rpeak):
        i = 50
        temp_rpeak = {}
        while True:
            i = i + 2
            if i == 102:
                break
            temp_rpeak[i] = str(int(i/100 * rpeak)) 
        return temp_rpeak

    result = rpeak_value(int(rpeak))
    for i in sorted(result.keys()):
        print('Rpeak:{:>3}% = {}'.format(i,result[i]))
    # Total number of processors in your grid: 
    def get_p_q(processors_grid):
        i = 1
        p_q_temp = []
        p_q_temp.append('P  x  Q')
        while True:
            n = int(processors_grid / i)
            if n != 2:
                if n/2 + 1 < i:
                    break
                else:
                    p_q_temp.append('{:<2} x {:<3}'.format(i,n))
            else:
                p_q_temp.append('{:<2} x {:<3}'.format(i,n))
            i = i * 2
        return p_q_temp

    # Base on the website P x Q should be : processors_grid = options.node * options.core
    #processors_grid = options.node * options.core
    #total_processors = 'Total number of processors in your grid: {0}'.format(processors_grid)
    #print(total_processors.center(70,'*'))

    # Now base on the total CPU nunbers
    total_cpu = options.node * options.cpu
    title_total_cpu = 'Total number of CPUs in your linpack group: {0}'.format(total_cpu)
    print(title_total_cpu.center(70,'*'))

    pq_value = get_p_q(total_cpu)
    print('PxQ Base on total CPUs'.center(70,'*'))
    for i in pq_value:
        print(i)
        
    #N/NB values
    print('N/NB values with N=192'.center(70,'*'))
    n_sqrt = math.sqrt((options.node * options.memory * 1024 * 1024 * 1024)/8)
    def n_nb_value(n_sqrt):
        i = 50
        nb = 192
        temp_nb = {}
        while True:
            i = i + 1
            if i == 102:
                break
            temp_nb[i] = '{} {}'.format(nb,int(n_sqrt / nb * i / 100) * nb)
        return temp_nb
    result = n_nb_value(n_sqrt)
    for i in sorted(result.keys()):
        print('N/NB:{:>3}% = {}'.format(i,result[i]))
elif options.target == 'purley':
    # Rpeak
    # node x core x cpu x cycle
    if options.operations is None:
    	options.operations = 32
    # print the detail information 
    print('Generate the HPL data:'.center(70,'*'))
    print('Number of Nodes        {}'.format(options.node))
    print('CPU per Node           {}'.format(options.cpu))
    print('Cores Per Node         {}'.format(options.core))
    print('Speed Per Core (GHz)   {}'.format(options.speed))
    print('Memory Per Node (GB)   {}'.format(options.memory))
    print('Operations Per Cycle   {}'.format(options.operations))
    print('Product Name:          {}'.format(options.target))
    rpeak = options.node * options.core * options.speed * options.operations
    print('System performance (Rpeak) in GFLOPS'.center(70,'*'))
    # print(int(rpeak))
    def rpeak_value(rpeak):
        i = 50
        temp_rpeak = {}
        while True:
            i = i + 2
            if i == 102:
                break
            temp_rpeak[i] = str(int(i/100 * rpeak)) 
        return temp_rpeak

    result = rpeak_value(int(rpeak))
    for i in sorted(result.keys()):
        print('Rpeak:{:>3}% = {}'.format(i,result[i]))
    # Total number of processors in your grid: 
    def get_p_q(total_nodes):
        i = 1
        p_q_temp = []
        p_q_temp.append('P  x  Q')
        while True:
            n = int(total_nodes / i)
            if n != 2:
                if n/2 + 1< i:
                    break
                else:
                    p_q_temp.append('{:<2} x {:<3}'.format(i,n))
            else:
                p_q_temp.append('{:<2} x {:<3}'.format(i,n))
            i = i * 2
        return p_q_temp

    pq_value = get_p_q(options.node)
    print('PxQ base on total nodes'.center(70,'*'))
    for i in pq_value:
        print(i)
        
    #N/NB values
    print('N/NB values with N=384'.center(70,'*'))
    n_sqrt = math.sqrt((options.node * options.memory * 1024 * 1024 * 1024)/8)
    def n_nb_value(n_sqrt):
        i = 50
        nb = 384
        temp_nb = {}
        while True:
            i = i + 2
            if i == 102:
                break
            temp_nb[i] = '{} {}'.format(nb,int(n_sqrt / nb * i / 100) * nb)
        return temp_nb
    result = n_nb_value(n_sqrt)
    for i in sorted(result.keys()):
        print('N/NB:{:>3}% = {}'.format(i,result[i]))
else:
    parser.print_help()
    sys.exit(1)
    

