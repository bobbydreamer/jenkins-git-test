import platform,socket,re,uuid,json,psutil,logging

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        info['coresPhysical']=psutil.cpu_count(logical=False)
        info['coresLogical']=psutil.cpu_count(logical=True)
        info['frequencyCurrent']=psutil.cpu_freq().current
        info['frequencyMax']=psutil.cpu_freq().max
        info['cpuUtilization']=psutil.cpu_percent(interval=1)
        info['availableRAMgb']=round(psutil.virtual_memory().available/1000000000, 2)
        info['usedRAMgb']=round(psutil.virtual_memory().used/1000000000, 2)
        return json.dumps(info, indent=2)
    except Exception as e:
        logging.exception(e)

print(getSystemInfo())