# pyinfra-infra
practise on pyinfra

# execution of code

```
❯ pyinfra inventory.py operations/nginx.py -y --limit web_server
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [sys-ubu24-dev1] Connected
    [sys-alma9-dev1] Connected

--> Preparing operation files...
    Loading: operations/nginx.py
    [sys-ubu24-dev1] Ready: operations/nginx.py
    [sys-alma9-dev1] Ready: operations/nginx.py

--> Skipping change detection
--> Beginning operation run...
--> Starting operation: Install nginx
    [sys-alma9-dev1] Skipped
    [sys-ubu24-dev1] Success

--> Starting operation: Install nginx
    [sys-ubu24-dev1] Skipped
    [sys-alma9-dev1] Success

--> Starting operation: upload nginx config
    [sys-ubu24-dev1] No changes
    [sys-alma9-dev1] No changes

--> Starting operation: Reload nginx
    [sys-ubu24-dev1] No changes
    [sys-alma9-dev1] No changes

--> Results:
    Operation             Hosts   Success   Error   No Change
    Install nginx         1       1         -       -
    Install nginx         1       1         -       -
    upload nginx config   2       -         -       2
    Reload nginx          2       -         -       2
    Grand total           6       2         -       4

--> Disconnecting from hosts...
```
