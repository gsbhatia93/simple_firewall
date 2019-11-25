# simple_firewall

This code sample is for creating basic firewall structure in Python. At the core is the class Firewall that is initailised with 
a set of rules, input as a CSV file.

After the initialization, we can begin processing packets. Packets are checked for 4 different parameter. 
#1 Direction <br>
#2 protocol  <br>
#3 port is within range or not. <br>
#4 ipv4 address is within range or not <br>
To server the purpose I have created a function, access_packets that checks these values. Helper functions like check_port and check_ip are also created to help with the same.
 <br> <br> <br>
Improvements:  <br>
#1 Multithreading to check input packet for rule - each thread picks up a batch of rules and checks the packet to the rules. If it passes either of the rules, then we let the packet go. <br>
#2 Space optimization of doing pre-processing before hand. <br>
#3 saving the rules to a dictionary format - right now it simply read from the csv file. <br>
#4 Tree check paradigm: saving the rules as a tree structure so, that the same checks are not performed multiple times for every packets. That would invovle saving rules in a graphical manner. The root node will check for 'direction', then the next layer checks for 'protocol', and similary flowing down to the leaf nodes, each containing ip address rules.  <br> This will entail heavy pre-processing of the rules fetched from the csv file for faster processing of each packet.


<br>
firewall.py contains the code, the .ipynb file was created for easier debugging.
                            


TEAM TO JOIN: -     rubinder.singh@illumio.com, Data Team Engineer

