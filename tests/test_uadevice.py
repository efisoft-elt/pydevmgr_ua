from pydevmgr_ua import UaDevice
import time
from opcua import ua, Server
server = Server()
#server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
server.set_endpoint("opc.tcp://localhost:4840")

# setup our own namespace, not really necessary but should as spec
uri = "http://examples.freeopcua.github.io"
idx = server.register_namespace(uri)

# get Objects node, this is where we should put our nodes
objects = server.get_objects_node()

# populating our address space
myobj = objects.add_object(idx, "MyObject")
myvar = myobj.add_variable('ns={};s=MyVariable'.format(idx), "MyVariable", 6.7)
myvar.set_writable()    # Set MyVariable to be writable by clients

# starting!
server.start()

try:
    
    
    count = 0
    while True:
        time.sleep(1)
        count += 0.1
        myvar.set_value(count)
finally:
    #close connection, remove subcsriptions, etc
    server.stop()
