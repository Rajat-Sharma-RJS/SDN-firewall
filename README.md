# SDN-firewall
Problem statement :  
Implement the SDN firewall in the network to obstruct traffic coming its way and filter it according to some rules. A general firewall usually protects the system from the internet.  
PC1c1, PC2c1, PC3c1 and PC4c1 should be mutually blocked.  
PC1c2, PC2c2, PC3c2 and PC4c2 should be mutually blocked.  
PC1c3, PC2c3, PC3c3 and PC4c3 should be mutually blocked.  
PC1c4, PC2c4, PC3c4 and PC4c4 should be mutually blocked.  
  
Solution :  
I have used POX from this repository https://github.com/noxrepo/pox and after downloading the zip file I have added my firewall.py file inside the pox/misc directory.  
In firewall.py file I’ve defined the rules which are responsible for the making up of the firewall.  
Then I typed below command with root access :  
$ ./pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning misc.firewall  
  
After that open a new terminal window and type  
$ mn --custom DataCenterTopologyFirewall.py --topo dcbasic --mac --switch ovs --controller remote  
( where DataCenterTopologyFirewall.py is the file where I'd build my data center topology, then type )  
mininet> pingall  
then you'll see the required output.
