import time
from pyinfra import logger, host

from pyinfra.operations import apt, yum, zypper
from pyinfra.facts.server import LinuxDistribution

start = time.time()
distro = host.get_fact(LinuxDistribution)
os_name = distro["name"]
packages = host.data.get("extra_pkgs", []) + host.data.get("common_pkgs", [])

# Update package list and install packages
if os_name in ["Debian", "Ubuntu"]:
    apt.packages(
        name="Install packages",
        packages=packages,
        update=True,
        _sudo=True,
    )

elif os_name in ["CentOS", "RedHat", "AlmaLinux"]:
    yum.packages(
        name="Install packages",
        packages=packages,
        update=True,
        _sudo=True,
    )

elif os_name in ["openSUSE Tumbleweed"]:
    zypper.packages(
        name="Install packages",
        packages=packages,
        update=True,
        latest=True,
        _sudo=True,
    )

duration = time.time() - start
logger.info(f"Installation took {time.time() - start:.2f}s")
