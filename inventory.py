# List of all servers
cloud_servers = [
    "cloud-ubu",
    "cloud-hpc",
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
