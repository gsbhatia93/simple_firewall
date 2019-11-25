"""

author: gsbhatia@umich.edu
task: network firewall to access to packets
illumino coding task

"""

import csv
from netaddr import IPNetwork, IPAddress

class Firewall:

    def __init__(self, csv_file_path):
        self.rules = csv.reader(open(csv_file_path,'r'))
                        
    def access_packets(self, direction, protocol, port, ip_address):                      
        '''
            function for access / block network packets based on rules
            input:
                direction (string)   : inbound or outbound
                protocol (string)    : tcp or udp
                port (integer)       : [1,65535]
                ip_address (integer) : ip_v4 address
            output:
                True  --> packet accepted
                False --> packet rejected
        ''' 
        status = False
        for rule in self.rules:
            print(rule)
            if(status):
                break
            if(rule[0] == direction):
                if(rule[1] == protocol):
                    if(self.check_port(rule[2],port)):
                        if(self.check_ip(rule[3], ip_address)):
                            status = True
                        else:
                            print("ip v4 check failed", )
                            status = False
                            
                    else:
                        print("port check failed")
                        status = False
                        continue
                else:
                    print("protocol check failed", rule[1], " ", port)
                    status = False
                    continue
            else:
                print(" direction check failed", rule[0], " ", direction)
                status= False
                continue
        return status
                                
    def check_port(self, port_rule, port_in):
        '''
            checks port is valid or not
            input: 
                port_rule : either in singular or in range
                port_in   : input port of the packet
            output:
                True / False
        '''
        status = False
        if("-" not in port_rule):
            if(int(port_rule==port_in) == int(port_in)):
                return True;
            else:
                return False;
        port_min, port_max = port_rule.split("-")
        port_min  = int(port_min)
        port_max  = int(port_max)
        port_in = int(port_in)
        if(port_in>= port_min and port_in <= port_max):
            return True;
        else:
            return False
                        
    def check_ip(self, ip_rule, ip_in):
        '''
            checks ip address is valid or not
            input: 
                ip_rule : either in singular or in range
                ip_in   : input ip_v4_address of the packet
            output:
                True / False
        '''
        if("-" not in port_rule):
            if(int(port_rule==port_in) == int(port_in)):
                return True;
            else:
                return False;
        
        start_ip,end_ip = ip_rule.split("-")
        start_ip = [int(x) for x in start_ip.split('.')]
        end_ip   = [int(x) for x in end_ip.split('.')]
        ip_in    = [int(x) for x in in_ip.split('.')]
        
        if(in_ip[0] >= start_ip[0] and in_ip[0] <= end_ip[0]):
            if(in_ip[1] >= start_ip[1] and in_ip[1] <= end_ip[1]):
                if(in_ip[2] >= start_ip[2] and in_ip[2] <= end_ip[2]):
                    if(in_ip[3] >= start_ip[3] and in_ip[3] <= end_ip[3]):
                        return True;
                    else:
                        return False
                return False
            return False
        return False

'''

using class for processing

'''

firewall = Firewall("rules.csv")

test_data = [
    ['inbound','tcp','90','192.168.1.2'],
    "inbound,tcp,80,192.168.1.2",
    "inbound,udp,53,192.168.3.1"    
]


t2 = test_data[2].split(",")
firewall.access_packets(t2[0],t2[1],t2[2],t2[3])