import time
from pyinfra import logger, host

from pyinfra.operations import apt, yum, zypper
from pyinfra.facts.server import LinuxName
# from pyinfra.facts.server import LinuxDistribution

true = yes = True
start = time.time()
distro = host.get_fact(LinuxName)
packages = ["htop", "vim", "snapd"]
# distro = host.get_fact(LinuxDistribution)

# Update package list and install packages
if distro in ["Debian", "Ubuntu"]:
    apt.packages(
        name="Install vim, snapd, and htop",
        packages=packages,
        # packages that comes from hosts or group vars
        # packages=host.data.packages,
        update=True,
        _sudo=yes,
    )

elif distro in ["CentOS", "RedHat", "AlmaLinux"]:
    yum.packages(
        name="Install vim, snapd, and htop",
        packages=packages,
        update=True,
        _sudo=True,
    )

elif distro in ["openSUSE Tumbleweed"]:
    zypper.packages(
        name="Install vim, and htop",
        packages=["htop", "vim"],
        update=True,
        latest=True,
        _sudo=True,
    )

# Using .get() for optional data
# if host.data.get("install_nginx"):
# Run nginx operations...
# pass

duration = time.time() - start
logger.info(f"Installation took {time.time() - start:.2f}s")
