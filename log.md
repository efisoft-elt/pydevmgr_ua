0.4.5
=====
- Some cleanup. com is now part of UaDevice.__init__ because not anymore in BaseDevice.__init__ 
- Align to core 0.4.4

0.4.4
=====
Align to pydevmgr_core 0.4.3

0.4.3
=====
Allowing extra in UaDevice and UaInterface so they can be used in a generic way 


0.4.2
=====
- a ua_device inside a ua_device now construct the prefix and parse the communication.
It wasn't the case before. Now a UaDevice depending on an other device is automaticaly on 
the same UA server (PLC). The config (address, namespace) of the Child UaDevice are completely 
ignored.

0.4.1
=====
some fixing in core 

0.4.0
=====
Follow the reformating of pydevmgr core 

0.3.1
=====

- 2022/03/09 S.G. Add the possibility to set the host mapping inside env $UA_HOST_MAP variable
