from pyinfra import host
from pyinfra.operations import apt, files, yum, server
from pyinfra.facts.server import LinuxDistribution

distro = host.get_fact(LinuxDistribution)
os_name = distro["name"]
major = distro["major"]

if os_name in ["Debian", "Ubuntu"]:
    install_nginx = apt.packages(
        name="Install nginx",
        packages=["nginx"],
        update=True,
        _sudo=True,
    )

elif os_name in ["CentOS", "RedHat", "AlmaLinux"]:
    install_nginx = yum.packages(
        name="Install nginx",
        packages=["nginx"],
        update=True,
        _sudo=True,
    )

nginx_config = files.template(
    name="upload nginx config",
    src="templates/nginx.conf.j2",
    dest="/etc/nginx/nginx.conf",
    os_name=os_name,
    major=major,
    _sudo=True,
    _if=install_nginx.did_change,
)

server.service(
    name="Reload nginx",
    service="nginx",
    reloaded=True,
    _sudo=True,
    _if=nginx_config.did_change,
)
