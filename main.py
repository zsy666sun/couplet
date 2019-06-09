from bottle import route, run ,Bottle ,error ,static_file ,request 
from bottle import view , template 
import os


@route('/')
def hello():
    #return "Hello World!"
    return template('index.html')

@route('/couplet')
def couplet():
    q = request.query.q
    fo = open('decoder/q.txt',mode='w+',encoding='UTF-8')
    qq = ''
    bl = ' '
    for i in q:
        qq = qq + i + bl
    fo.write(qq)
    fo.close()
    os.system('bash decoder.sh')
    ###
    fo = open('decoder/a.txt.transformer.transformer_small.translate_up2down.beam4.alpha0.6.decodes',encoding='UTF-8')
    txt = fo.read()
    txt = txt.replace(' ','')
    fo.close()
    return txt
    ###
    #return qq

@route('/couplet_get')
def couplet_get():
    fo = open('decoder/q.txt.transformer.transformer_small.translate_up2down.beam4.alpha0.6.decodes',encoding='UTF-8')
    txt = fo.read()
    txt = txt.replace(' ','')
    fo.close()
    return txt


run(host='localhost', port=8080, debug=True)
