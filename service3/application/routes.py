from flask import request,Response
import requests
from application import app
import random

#generates a the name of a random author 
@app.route('/get_num_one',methods=['GET'])
def get_name1():
    name2= name_four[random.randint(1,10)]
    return Response(author,mimetype='text/plain')

@app.route('/get_num_two',methods=['GET'])
def get_name2():
    name2 = name2[random.randint(10,100)]
    return Response(author,mimetype='text/plain')