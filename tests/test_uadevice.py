from pydevmgr_ua import UaDevice
from pydevmgr_core import BaseManager

def test_engine_creation_from_manager():

    class D(UaDevice):
        ...

    class M(BaseManager):
        d = D.Config(prefix="D")

    m = M('m' )
    m.d
    assert m.engine.localdata is m.d.engine.localdata 

def test_engine_creation_from_device():

    class D(UaDevice):
        ...
    
    class PD(UaDevice):
        d = D.Config(prefix="D")



    pd = PD('m', prefix="PD" )
    assert pd.d.engine.prefix == "PD.D"
    assert pd.engine.client  == pd.d.engine.client 

