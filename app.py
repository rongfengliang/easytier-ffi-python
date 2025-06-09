import easytier
import time
easy = easytier.EasyTier()

with open("app.yaml","r") as f:
    config = f.read()

result = easy.parse_config(config)
if result != 0:
    print("Error parsing configuration:", easy.get_error_msg())
    exit(1)
else:
    print("Configuration parsed successfully.")

result = easy.run_network_instance(config)

if result == 0:
    print("Network instance started successfully.")
    while True:
        time.sleep(1)
        print("Running network instance...")