from pydevmgr_ua import UaNode
from pydevmgr_ua.uacom import UaComHandler, UaCom
import opcua


class UaComMockup(UaComHandler):
    
    @staticmethod 
    def get_attribute(engine, a):
        variant=  getattr(engine, "__uaattr__", {}).get(a, None)
        return variant.Value.Value 

    @staticmethod
    def set_attribute(engine, a, value):
        if not hasattr(engine, "__uaattr__"):
            engine.__uaattr__ = {}
        engine.__uaattr__[a] = value
        
    
UaNode.com_handler = UaComMockup       


def test_uanode_empty_init():
    node = UaNode("node_name")
    assert node.engine.client is None
    assert not node.config.suffix

def test_uanode_engine_as_uaclient():
    c = opcua.Client("opc.tcp://localhost:4840") 
    node = UaNode( com=c)
    assert node.engine.client == c
    assert isinstance( node.engine.node_client, opcua.Node)
    assert node.sid

def test_uanode_engine_as_dict():
    c = {'address':'opc.tcp://localhost:4840', 'namespace':6, 'prefix':'my_parent'}
    node = UaNode(com=c, suffix="my_node")
    assert isinstance( node.engine.node_client, opcua.Node)
    assert str(node.engine.node_id).find("ns=6")>-1  
    assert node.engine.node_name == 'my_parent.my_node'


def test_node_get_set():
    node = UaNode()
    
    node.set("hello")
    node.get()
    
    assert node.get() == "hello"    


def test_node_localdata_is_parent_localdata():
    com = UaCom()
    node = UaNode( com = com)
    assert node.engine.localdata is com.localdata
    
