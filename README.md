# easytier-ffi python cffi learning

## running 

* build

```code
 python -m build --wheel
```

* app.yaml

```code
instance_name = "xxxxx"
instance_id = "xxxxx"
dhcp = true
listeners = [
    "tcp://0.0.0.0:11010",
    "udp://0.0.0.0:11010",
    "wg://0.0.0.0:11011",
]
rpc_portal = "0.0.0.0:0"

[network_identity]
network_name = "xxxxx"
network_secret = "xxxxx"

[[peer]]
uri = "tcp://xxxxx:11010"

[flags]
```