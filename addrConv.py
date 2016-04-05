#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
 
parser = argparse.ArgumentParser(description='This is an address conversion tool')

parser.add_argument('--Logical','-L',action='store_true', default=False, dest='logical', help='Calculate the logical address from either the cluster address or the physical address. Either –c or -p must be given\n',required=False)

parser.add_argument('--physical','-P',action='store_true', default=False, dest='physical',help='Calculate the physical address from either the cluster addressor the logical address. Either –c or –l must be given.', required=False)

parser.add_argument('--cluster','-C',action='store_true', default=False, dest='cluster', help='Calculate the cluster address from either the logical address or the physical address. Either –l or –p must be given.',required=False)

parser.add_argument('--byte-address','-B',action='store_true', default=False,dest='byteAdd',help='Instead of returning sector values for the conversion, this returns the byte address of the calculated value, which is the number of sectors multiplied by the number of bytes per sector.',required=False)



parser.add_argument('--partition-start=offset','-b offset',type=int, default=0, dest='offset',help='This specifies the physical address (sector number) of the start of the partition, and defaults to 0 for ease in working with images of a single partition. The offset value will always translate into logical address 0.', required=False)

parser.add_argument('--sector-size=bytes','-s bytes',dest='secSizeBytes',help='When the –B option is used, this allows for a specification ofbytes per sector other than the default  512. Has no affect on output without –B.',required=False)



parser.add_argument('--logical-known=address','-l address',dest='logAddknow',help='This specifies the known logical address for calculating either a cluster address or a physical address. When used with the –L option, this simply returns the value given for address.',required=False)

parser.add_argument('--physical-known=','-p address',type=int,dest='phyAddknow',help=' This specifies the known physical address for calculating either a cluster address or a logical address. When used with the –P option, this simply returns the value given for address.',required=False)

parser.add_argument('--cluster-known=address','-c address',dest='cluAddknow',help='This specifies the known cluster address for calculating either a logical address or a physical address. When used with the –C option, this simply returns the value given for address. Note that options –k, -r, -t, and –f must be provided with this option.',required=False)

parser.add_argument('--cluster-size=sectors','-k sectors',dest='cluSize', help=' This specifies the number of sectors per cluster.',required=False)

parser.add_argument('--reserved=sectors','-r sectors',dest='resSect',help='This specifies the number of reserved sectors in the partition.',required=False)

parser.add_argument('--fat-tables=tables','-t tables',dest='fatTable',help='This specifies the number of FAT tables, which is usually 2.',required=False)

parser.add_argument('--fat-length=sectors','-f sectors',dest='fatLength',help='This specifies the length of each FAT table in sectors.',required=False)


args = parser.parse_args()

if args.logical:
	data = args.phyAddknow - args.offset
	print data
if args.physical:


if args.cluster:


if args.byteAdd:
	#return byte address version
	print data
#if statement for the big ones then do something
 
## show values ##
