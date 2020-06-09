"""
A simple datacenter topology script for Mininet.

    [ s1 ]================================.
      ,---'       |           |           |
    [ Sw1_c1 ]=.  [ Sw1_c2 ]=.  [ Sw1_c3 ]=.  [ Sw1_c4 ]=.
    [ PC1c1 ]-|  [ PC1c2 ]-|  [ PC1c3 ]-|  [ PC1c4 ]-|
    [ PC2c1 ]-|  [ PC2c2 ]-|  [ PC2c3 ]-|  [ PC2c4 ]-|
    [ PC3c1 ]-|  [ PC3c2 ]-|  [ PC3c3 ]-|  [ PC3c4 ]-|
    [ PC4c1 ]-'  [ PC4c2 ]-'  [ PC4c3 ]-'  [ PC4c4 ]-'
"""

from mininet.topo import Topo
from mininet.util import irange

class DatacenterBasicTopo( Topo ):
    "Datacenter topology with 4 hosts per rack, 4 racks, and a root switch"

    def build( self ):
        self.racks = []
        rootSwitch = self.addSwitch( 's1' )
        for i in irange( 1, 4 ):
            rack = self.buildRack( i )
            self.racks.append( rack )
            for switch in rack:
                self.addLink( rootSwitch, switch )

    def buildRack( self, loc ):
        "Build a rack of hosts with a top-of-rack switch"

        dpid = ( loc * 16 ) + 1
        switch = self.addSwitch( 'Sw1_c%s' % loc, dpid='%x' % dpid )

        for n in irange( 1, 4 ):
            host = self.addHost( 'PC%sc%s' % ( n, loc ) , ip='10.0.0.%s' % (n + (4 * (loc - 1)) ), mac='00:00:00:00:00:%s' % (n + (4 * (loc - 1)) ) )
            self.addLink( switch, host )

        # Return list of top-of-rack switches for this rack
        return [switch]

# Allows the file to be imported using `mn --custom <filename> --topo dcbasic`
topos = {
    'dcbasic': DatacenterBasicTopo
}
