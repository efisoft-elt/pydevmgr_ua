from pydevmgr_ua.uacom import UaComRpcNode, UaCom, uaconfig

if __name__ == "__main__":
    try:
        uaconfig.default_address = "toto" # must return an error
    except ValueError:
        pass
    else:
        assert False 
        
    uaconfig.default_address = "opc.tcp://localhost:4840"
    uaconfig.namespace = 4
    
    com = UaCom(prefix="A")
    assert com.config.address == uaconfig.default_address
    ncom = com.nodecom('B')
    assert str(ncom.nodeid) == "StringNodeId(ns=4;s=A.B)"
    rcom = com.rpccom('C', 'M')    
    assert rcom._method_id == '4:M'
    scom = com.subcom("D")
    assert scom._prefix == "A.D" 
    
    
    
