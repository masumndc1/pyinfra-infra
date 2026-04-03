from pyinfra import local

# Include other operation files
local.include("operations/pkg.py")
local.include("operations/nginx.py")
