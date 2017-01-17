import requests, json, logging, argparse


EC2_METADATA = "http://169.254.169.254/latest"


class NagiosClient(object):

    def __init__(self,servicetype, nagioServerIP, nagioServerPort):
        data = {
            "instance_id": self.getInstanceInfo()['instanceId'],
            "instance_ip": self.getInstanceInfo()['privateIp'],
            "service_type": servicetype
        }
        MONITOR_SERVER = "http://" + nagioServerIP + nagioServerPort + "/nagios/new"
        # For debuging only
        logging.warning(self.getInstanceInfo())
        logging.warning(data)
        res = requests.post(MONITOR_SERVER,data= json.dumps(data))
        logging.warning(res.status_code)

    def getInstanceInfo(self):
        return requests.get(EC2_METADATA + '/dynamic/instance-identity/document').json()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Add Nagios Client", add_help=True)
    parser.add_argument('--serviceType', action='store', dest='type', default='web', help='Please pass service type', type=str)
    parser.add_argument('--nagiosServerIP', action='store',dest='serverip', default='127.0.0.1', help='Please pass server ip', type=int)
    parser.add_argument('--nagiosServerPort', action='store',dest='port', default='4000', help='Please pass server port', type=int)
    Info = parser.parse_args()
    NagiosClient(Info.type, Info.serverip, Info.port)
