rm run_pid.txt
nohup python3 app/mickapp.py &
jobs -p > run_pid.txt