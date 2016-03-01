# -*- coding: utf-8 -*-
import logging, time


def log(name):
    logging.basicConfig(
    level=logging.DEBUG,
    format='\n\n%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='run.log',
    filemode='a')

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter('%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s'))
    logging.getLogger('').addHandler(console)

    #logging.debug('debug message')
    logging.info('test_case : %s' %name)
    #logging.warning('warning message')
    #logging.error("error message")
    #logging.critical("critical message")


#log('myself')

def mylog(name, result):
    string = ''
    ISOTIMEFORMAT='%Y-%m-%d %X'
    string += '\n\n' + time.strftime( ISOTIMEFORMAT, time.localtime(time.time())) + '\n'\
              +'test_case : %s' %name +'\n' + 'test_result : \n%s' % result
    with open('run.log', 'ab') as file:
        file.write(string)
        file.close()
