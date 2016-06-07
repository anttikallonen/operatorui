#!/bin/bash
python /home/root/manage.py run_tests &&
python /home/root/manage.py show_urls &&
python /home/root/manage.py run_server
