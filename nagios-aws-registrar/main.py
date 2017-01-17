from bottle import route, run, request,response
import requests, json, time
import logging, jinja2, os

TOKEN = "8si9LCE7EpKpVbg2Ftnm6uA4Amfn8cIRO7UquIO9WWVOkcbhGN"
NAGIOS_CFGS = '/etc/nagios3/servers.d'
NAGIOS_TEMPLATE = os.path.join(os.getcwd(), 'templates', 'nagios')
TEMPLATELOADER = jinja2.FileSystemLoader(NAGIOS_TEMPLATE)
TEMPLATEENV = jinja2.Environment(loader=TEMPLATELOADER)




@route('/ping')
def ping():
    return 'pong@' + str(time.time())


@route('/nagios/new', method='POST')
def nagiosNew():
    data = request.json
    file_name = data['service_type'] + "_" + data['instance_id']
    #logging.warning(data['service_type'])
    template = TEMPLATEENV.get_template("/" + data['service_type'] + ".jinja")
    #logging.warning(template)
    templateVars = {
        "hostname": data['service_type'] + "_" + data['instance_id'],
        "instance_ip": data['instance_ip']
    }
    #logging.warning(templateVars)
    fname = "%s.cfg" % file_name
    logging.warning(fname)
    
    if request.query.get('token','') != TOKEN:
        return json.dumps({"msgs": "Invalid Token", "status": "403"})
    else:
        with open(os.path.join(NAGIOS_CFGS, fname), 'w+') as f:
            f.write(template.render(templateVars))
        return json.dumps({"msgs": "Success Request", "status": "200"})


    


run(host='localhost', port=4000, debug=True, reloader=True)