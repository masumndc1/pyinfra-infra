from pyinfra import host, inventory
from pyinfra.operations import files
from pyinfra.facts.server import LinuxDistribution, Hostname

distro = host.get_fact(LinuxDistribution)
host_name = host.get_fact(Hostname)
group_data = inventory.get_group_data("monitor_nodes")
server_ip = group_data.get("monitor_server_ip")

for node in inventory.get_group("monitor_nodes"):
    node_name = node.name
    ip = node.data.get("ip")
    # print(f"node: {node_name}, ip: {ip}")
    files.template(
        name="upload nagios node config",
        src="templates/nagios_hosts.cfg.j2",
        dest=f"/root/{node_name}.cfg",
        node_name=node_name,
        server_name=host_name,
        server_ip=server_ip,
        ip=ip,
        _sudo=True,
    )
