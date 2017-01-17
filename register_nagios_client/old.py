import os, sys, requests
import logging, json, re

EC2_METADATA = "http://169.254.169.254/latest"
MONITOR_SERVER = "http://localhost:7070/nagios/new"

class NagiosService(object):
    def __init__(self):
        
        for i in self.fetchClientCommand():
            logging.warning(i[1:-1])
        #logging.warning(self.fetchClientCommand())

    def getInstanceIP(self):
        instanceInfo = requests.get(EC2_METADATA + '/dynamic/instance-identity/document')
        return instanceInfo.json()

    def sendService(self):
        return json.dumps({"server_ip": self.getInstanceIP(), "service_info":self.nagiosServiceInfo()})

    def nagiosServiceType(self):
        self.nagiosServicesArray("solr")

    def fetchClientCommand(self):
        nagiosCommands = []
        with open('/etc/nagios/nrpe.cfg') as test:
            for line in test:
                line = line.strip()
                if re.search('command\[', line):
                    line = line.strip()
                    line = re.findall('\[.*\]', line)
                    for i in line:
                        nagiosCommands.append(i)
        return nagiosCommands


    def nagiosServiceInfo(self):
        for i in self.fetchClientCommand():
            pass

    def nagiosServicesArray(self, serviceName):
        if serviceName == 'solr':
            return [
                        { "description": "PING", "command": "check-host-alive" },
                        { "description": "Solr", "command": "check_tcp!8983" },
                        { "description": "CPU Load", "command": "check_nrpe_1arg!check_load" },
                        { "description": "Users", "command": "check_nrpe_1arg!check_users" },
                        { "description": "/ Space", "command": "check_nrpe_1arg!check_disk1" },
                        { "description": "Zombie Process", "command": "check_nrpe_1arg!check_zombie_procs" },
                        { "description": "Total Process", "command": "check_nrpe_1arg!check_total_procs" },
                        { "description": "SSH", "command": "check_ssh_port!2222" }
                    ]

if __name__ == '__main__':
    nagios_node = NagiosService()