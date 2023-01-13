from pydevmgr_ua import UaInterface, UaNode, UaCom
from pydevmgr_ua.uadevice import UaDevice

def test_node_engine_creation():
    
    class I(UaInterface):
        n = UaNode.Config(suffix="n")

    i = I(prefix="MAIN.i")
    
    assert i.n.engine.client == i.engine.client

def test_parse_of_node():
    class I(UaInterface):
        n = UaNode.Config(suffix="n")

    class D(UaDevice):
        i = I.Config(prefix="i")
     
    d = D("d", prefix="d")
    
    assert d.engine.client == d.i.engine.client 
    assert d.i.engine.client == d.i.n.engine.client
    assert d.engine.localnode_values is d.i.n.engine.localnode_values 


