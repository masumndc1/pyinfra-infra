from pyinfra import local, host

# Include other operation files
local.include("operations/pkg.py")

if "web_server" in host.groups:
    local.include("operations/nginx.py")
