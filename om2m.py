import requests
import sys
from uuid import getnode as get_mac

server = 'http://140.113.66.98:8080'

def create_application(app_name):
    url = server + '/~/in-cse'
    headers={
        'X-M2M-Origin': 'admin:admin',
        'Content-Type': 'application/xml;ty=2',
        'X-M2M-NM': app_name
    }
    data='<om2m:ae xmlns:om2m="http://www.onem2m.org/xml/protocols">\
              <api>app-sensor</api>\
              <lbl>Tpye/sensor Category/temperature Location/home</lbl>\
              <rr>false</rr>\
          </om2m:ae>'
    r = requests.post(url, headers=headers, data=data)
    return r.status_code

def create_container(app_name, con_name):
    url = server + '/~/in-cse/in-name/' + app_name
    headers={
        'X-M2M-Origin': 'admin:admin',
        'Content-Type': 'application/xml;ty=3',
        'X-M2M-NM': con_name
    }
    data='<om2m:cnt xmlns:om2m="http://www.onem2m.org/xml/protocols">\
          </om2m:cnt>'
    r = requests.post(url, headers=headers, data=data)
    return r.status_code

def create_content_instance(app_name, con_name, con_ins_data):
    url = server + '/~/in-cse/in-name/' + app_name + '/' +  con_name
    headers={
        'X-M2M-Origin': 'admin:admin',
        'Content-Type': 'application/xml;ty=4',
    }
    data='<om2m:cin xmlns:om2m="http://www.onem2m.org/xml/protocols">\
              <cnf>message</cnf>\
              <con>\
                  %s\
              </con>\
          </om2m:cin>' % con_ins_data
    r = requests.post(url, headers=headers, data=data)
    return r.status_code

def subscribe(app_name, con_name):
    sub_url = server + '/~/in-cse/in-name/' + app_name + '/' + con_name
    sub_headers={
        'X-M2M-Origin': 'admin:admin',
        'Content-Type': 'application/xml;ty=23',
        'X-M2M-NM': 'SUB'
    }
    sub_data='<m2m:sub xmlns:m2m="http://www.onem2m.org/xml/protocols">\
                <nu>http://localhost:1400/monitor</nu>\
                <nct>2</nct>\
              </m2m:sub>'
    r = requests.post(sub_url, headers=sub_headers, data=sub_data)
    # print(r.text)
    return r.status_code

def get_data(app_name, con_name):
    url = server + '/~/in-cse/in-name/' + app_name + '/' +  con_name + '/la'
    headers = {
        'X-M2M-Origin': 'admin:admin'
    }

    r = requests.get(url, headers=headers)
    begin = r.text.find("<con>") + 5
    end = r.text.find("</con>") - 1
    data = r.text[begin:end].strip().split(' ')
    return data

def help():
    print('create application     : python3 om2m.py app <application>')
    print('create container       : python3 om2m.py con <application> <container>')
    print('create content instance: python3 om2m.py ins <application> <container> <data>')
    print('subscribe              : python3 om2m.py sub <application> <container>')
    print('get last data          : python3 om2m.py get <application> <container>')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        help()
    elif sys.argv[1] == 'app':
        print(create_application(sys.argv[2]))
    elif sys.argv[1] == 'con':
        print(create_container(sys.argv[2], sys.argv[3]))
    elif sys.argv[1] == 'ins':
        print(create_content_instance(sys.argv[2], sys.argv[3], sys.argv[4]))
    elif sys.argv[1] == 'sub':
        print(subscribe(sys.argv[2], sys.argv[3]))
    elif sys.argv[1] == 'get':
        print(get_data(sys.argv[2], sys.argv[3]))
    else:
        help()
