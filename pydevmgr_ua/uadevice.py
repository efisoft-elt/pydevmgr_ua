from pydevmgr_core import BaseDevice, record_class
from .uacom import UaComHandler
from .config import uaconfig
from .uainterface import UaInterface
from .uanode import UaNode
from .uarpc import UaRpc
from .uaengine import UaEngine
from pydantic import AnyUrl, Field

@record_class
class UaDevice(BaseDevice):
    Node = UaNode
    Rpc = UaRpc
    Interface = UaInterface
    Engine = UaEngine
    com_handler = UaComHandler
    
    class Config(BaseDevice.Config, UaEngine.Config):
        Node = UaNode.Config
        Interface = UaInterface.Config
        Rpc = UaRpc.Config

        type: str = "Ua"

    def connect(self):
        """ Connect to the OPC-UA client """
        return self.com_handler.connect(self.engine)
        
    def disconnect(self):
        """ Connect from the  OPC-UA client """
        return self.com_handler.disconnect(self.engine)
    
    def is_connected(self):
        return self.com_handler.is_connect(self.engine)
    
    
