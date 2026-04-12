import time
from pyinfra import logger, host

from pyinfra.operations import apt, yum, zypper, files
from pyinfra.facts.server import LinuxDistribution

start = time.time()
distro = host.get_fact(LinuxDistribution)
os_name = distro["name"]
major = distro["major"]

# Update package list and install packages
if os_name in ["Debian", "Ubuntu"]:
    files.download(
        name="add openvox gpg key",
        src="https://apt.voxpupuli.org/openvox-keyring.gpg",
        dest="/usr/share/keyrings/openvox-keyring.gpg",
        _sudo=True,
    )
    files.template(
        name="create repo file for openbolt",
        src="templates/openbolt.j2",
        dest="/etc/apt/sources.list.d/openbolt.list",
        mode="644",
        os_name=os_name,
        major=major,
        _sudo=True,
    )
    apt.packages(
        name="Install openbox agent",
        packages=["openvox-agent"],
        update=True,
        _sudo=True,
    )

elif os_name in ["CentOS", "RedHat", "AlmaLinux"]:
    files.template(
        name="create repo file for openbolt",
        src="templates/openbolt.j2",
        dest="/etc/yum.repos.d/openbolt.repo",
        mode="644",
        os_name=os_name,
        major=major,
        _sudo=True,
    )
    yum.packages(
        name="Install openbolt agent",
        packages=["openvox-agent"],
        update=True,
        _sudo=True,
    )

elif os_name in ["openSUSE Tumbleweed"]:
    files.template(
        name="create repo file for openbolt",
        src="templates/openbolt.j2",
        dest="/etc/zypp/repos.d/openbolt.repo",
        mode="644",
        os_name=os_name,
        major=major,
        _sudo=True,
    )
    zypper.packages(
        name="Install openbolt agent",
        packages=["openvox-agent"],
        update=True,
        latest=True,
        _sudo=True,
    )

duration = time.time() - start
logger.info(f"Installation took {time.time() - start:.2f}s")
