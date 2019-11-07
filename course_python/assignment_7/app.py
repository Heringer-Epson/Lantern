import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from appliances import Appliance_Item
from catalog import catalog

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/listing')
def listing():
    return render_template('list.html', listing=catalog)
    
@app.route('/search_appliance', methods=['POST', 'GET'])
def search_appliance():
    if request.method=='POST':
        search_name = request.form.get('appliance_name')
        try:
            appliance_obj = catalog[search_name]
            return render_template('search_output.html', obj=appliance_obj)
        except:
            return """<h1> "{}" not found, please try again. </h1>
                   """.format(search_name)

@app.route('/update_status/<appliance>', methods=['POST', 'GET'])
def update_status(appliance):
    if request.method=='POST':
        switch_status = request.form.get('switch_status')
        appliance_obj = catalog[appliance]
        appliance_obj.change_status(switch_status)
        return '''<h1> {} is now {} </h1>'''.format(appliance_obj.name,
                                                    appliance_obj.status)

if __name__=='__main__':
    app.run(debug=True)
