# List of all servers
# pyinfra inventory format:
# hosts = {
#     "hostname": {"data": {...}},
# }

cloud_servers = [
    "cloud-ubu",
    # "cloud-hpc",
    # ("devstack", {"ssh_port": 22}),  # Host with custom data
]

incus_nodes = [
    ("sys-alma9-dev1", {"extra_pkgs": ["snapd"], "web_user": "nginx"}),
    ("sys-deb12-dev1", {"extra_pkgs": ["snapd"]}),
    ("sys-deb13-dev1", {"extra_pkgs": ["snapd"]}),
    ("sys-suse-dev1"),
    ("sys-ubu24-dev1", {"extra_pkgs": ["snapd"]}),
]

web_server = (
    ["sys-alma9-dev1", "sys-ubu24-dev1"],
    {
        "web_port": 8080,
        "domain_name": "masum.com",
        "env": "prod",
        "max_client": 32,
    },
)

monitor_server = ["lap-macmini"]

monitor_nodes = [
    ("puppet-dev1", {"ip": "192.168.5.55"}),
    ("puppet-dev2", {"ip": "192.168.5.181"}),
    ("puppet-dev3", {"ip": "192.168.5.80"}),
    ("puppet-prod1", {"ip": "192.168.5.211"}),
    ("puppet-prod2", {"ip": "192.168.5.146"}),
    ("puppet-prod3", {"ip": "192.168.5.223"}),
    ("puppetmaster", {"ip": "192.168.5.176"}),
    ("sys-alma9-dev1", {"ip": "192.168.5.26"}),
    ("sys-deb12-dev1", {"ip": "192.168.5.212"}),
    ("sys-deb13-dev1", {"ip": "192.168.5.86"}),
    ("sys-suse-dev1", {"ip": "192.168.5.154"}),
    ("sys-ubu24-dev1", {"ip": "192.168.5.87"}),
]
