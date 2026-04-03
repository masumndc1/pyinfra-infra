from pyinfra import local, host

# Include other operation files
local.include("operations/pkg.py")

if "web_server" in host.groups:
    local.include("operations/nginx.py")

# if "sys-alma9-dev1" in host.name:
#    local.include("operations/pkg.py")
