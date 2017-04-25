import requests
import sys

if len(sys.argv) == 1:
    print('usage: python3 om2m.py 2 <application>')
    print('usage: python3 om2m.py 3 <application> <container>')
    print('usage: python3 om2m.py 4 <application> <container> <data>')

elif sys.argv[1] == '2':
    if len(sys.argv) != 3:
        print('usage: python3 om2m.py 2 <application>')
        sys.exit()
    url = 'http://140.113.66.98:8080/~/in-cse'
    headers={
        'X-M2M-Origin': 'admin:admin',
        'Content-Type': 'application/xml;ty=2',
        'X-M2M-NM': sys.argv[2]
    }
    data='<om2m:ae xmlns:om2m="http://www.onem2m.org/xml/protocols">\
              <api>app-sensor</api>\
              <lbl>Tpye/sensor Category/temperature Location/home</lbl>\
              <rr>false</rr>\
          </om2m:ae>'
    print(requests.post(url, headers=headers, data=data))

elif sys.argv[1] == '3':
    if len(sys.argv) != 4:
        print('usage: python3 om2m.py 3 <application> <container>')
        sys.exit()
    application = sys.argv[2]
    container = sys.argv[3]
    url = 'http://140.113.66.98:8080/~/in-cse/in-name/' + application
    headers={
        'X-M2M-Origin': 'admin:admin',
        'Content-Type': 'application/xml;ty=3',
        'X-M2M-NM': container
    }
    data='<om2m:cnt xmlns:om2m="http://www.onem2m.org/xml/protocols">\
          </om2m:cnt>'
    print(requests.post(url, headers=headers, data=data))

elif sys.argv[1] == '4':
    if len(sys.argv) != 5:
        print('usage: python3 om2m.py 4 <application> <container> <data>')
        sys.exit()
    application = sys.argv[2]
    container = sys.argv[3]
    url = 'http://140.113.66.98:8080/~/in-cse/in-name/' + application + '/' +  container
    headers={
        'X-M2M-Origin': 'admin:admin',
        'Content-Type': 'application/xml;ty=4',
    }
    data='<om2m:cin xmlns:om2m="http://www.onem2m.org/xml/protocols">\
              <cnf>message</cnf>\
              <con>\
                  %s\
              </con>\
          </om2m:cin>' % sys.argv[4]
    print(requests.post(url, headers=headers, data=data))
