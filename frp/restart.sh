#!/bin/sh
ps -efww|grep -w 'frpc'|grep -v grep|cut -c 9-15|xargs kill -9
sleep 1s
nohup /home/kimroniny/frp/frp_0.33.0_linux_amd64/frpc -c /home/kimroniny/frp/frp_0.33.0_linux_amd64/frpc.ini 2>&1 > log &
