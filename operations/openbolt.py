import time
from pyinfra import logger, host

from pyinfra.operations import apt, yum, zypper, files
from pyinfra.facts.server import LinuxDistribution

start = time.time()
distro = host.get_fact(LinuxDistribution)
os_name = distro["name"]
version_id = distro["release_meta"]["VERSION_ID"]
major = distro["major"]

# Update package list and install packages
if os_name in ["Debian", "Ubuntu"]:
    files.download(
        name="add openvox gpg key",
        src="https://apt.voxpupuli.org/openvox-keyring.gpg",
        dest="/usr/share/keyrings/openvox-keyring.gpg",
        _sudo=True,
    )
    apt.repo(
        name="Install openbolt repo",
        src=f"deb [signed-by=/usr/share/keyrings/openvox-keyring.gpg] https://apt.voxpupuli.org {os_name.lower()}{version_id} openvox8",
        filename="openvox",
        _sudo=True,
    )
    apt.packages(
        name="Install openbox agent",
        packages=["openvox-agent"],
        update=True,
        _sudo=True,
    )

elif os_name in ["CentOS", "RedHat", "AlmaLinux"]:
    yum.repo(
        name="Install openbolt repo",
        src=f"https://yum.voxpupuli.org/openvox8/el/{major}/$basearch",
        _sudo=True,
    )
    yum.packages(
        name="Install openbolt agent",
        packages=["openvox-agent"],
        update=True,
        _sudo=True,
    )

elif os_name in ["openSUSE Tumbleweed"]:
    zypper.repo(
        name="Install openbolt repo",
        src="https://yum.voxpupuli.org/openvox8/el/8/$basearch",
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
