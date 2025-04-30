import platform 
info = {}

os_details = platform.platform ()
system_name = platform.system ()
processor_name = platform.processor ()
architecture_details = platform.architecture ()

info ["platform details"] = os_details
info ["system name"] = system_name
info ["processor name"] = processor_name
info ["architectural detail"] = architecture_details

for i, j in info.items ():
    print (i, " = ", j)






























