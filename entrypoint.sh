#!/bin/bash
exec python /home/root/manage.py run_tests &&
exec python /home/root/manage.py show_urls &&
exec python /home/root/manage.py run_server
