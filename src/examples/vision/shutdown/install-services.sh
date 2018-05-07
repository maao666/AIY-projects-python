#!/bin/bash

scripts_dir="$(dirname "${BASH_SOURCE[0]}")"
cd "${scripts_dir}"

sudo cp shutdown_monitor.service /lib/systemd/system
systemctl enable shutdown_monitor.service
