# List of all servers
cloud_servers = [
    "cloud-ubu",
    "cloud-hpc",
    # ("devstack", {"ssh_port": 22}),  # Host with custom data
]

incus_nodes = [
    "sys-alma9-dev1",
    "sys-deb12-dev1",
    "sys-deb13-dev1",
    "sys-suse-dev1",
    "sys-ubu24-dev1",
]

# List of database servers
# example of setting single vars of group
# db_server = (
#    ["db-1.net", "db-2.net"],  # List of hosts
#    {"db_port": 5432,          # Group data dictionary
#     "ssh_user": "ubuntu",
#     "ssh_key": "~/.ssh/id_rsa",
#     "env": "production",
#    }
# )

# example of host specific data
# Hostname string + dictionary of host-specific data
# app_servers = [
#   ("app-1.net", {"app_version": "1.2.0", "is_primary": True}),
#   ("app-2.net", {"app_version": "1.1.0", "is_primary": False}),
# ]
