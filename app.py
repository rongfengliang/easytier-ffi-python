import easytier
import time
from easytier._easytier_cffi import ffi
easy = easytier.EasyTier()

with open("app.yaml","r") as f:
    config = f.read()

result = easy.parse_config(config)
if result != 0:
    print("Error parsing configuration:", easy.get_error_msg())
    exit(1)
else:
    print("Configuration parsed successfully.")

max_length = 10
result = easy.run_network_instance(config)

infos = ffi.new("KeyValuePair[]", max_length)


if result == 0:
    print("Network instance started successfully.")
    while True:
        time.sleep(3)
        ret = easy.libeasytier.collect_network_infos(infos, max_length)
        for i in range(ret):
            key = ffi.string(infos[i].key).decode()
            value = ffi.string(infos[i].value).decode()
            print(f"{key}: {value}")
        print("Running network instance...")