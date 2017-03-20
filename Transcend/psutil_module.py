import psutil
while True:
    print(psutil.cpu_stats())
    print(psutil.cpu_count())
    print(psutil.disk_partitions())
    print(psutil.disk_usage('/'))
    print(psutil.disk_io_counters(perdisk=False))
    print(psutil.users())
    print(psutil.process_iter())
    for i in range(3):
        print(psutil.cpu_times_percent(interval=1, percpu=True))
        print(psutil.cpu_percent(interval=1, percpu=True))
    print(psutil.pids())
    p = psutil.Process(1)
    print(p.name())
