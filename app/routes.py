from app import app
from flask import render_template, request, jsonify, make_response, send_file
import pandas as pd

import app.data_gen as db_requests
from config import Config

COLUMNS = ['Id', 'Initials', 'Address', 'Tel-number']

cur_table_gen, gen_seed = None, None
data = pd.DataFrame(columns=COLUMNS)

def get_generated_data(size: int):
    global data, cur_table_gen
    fake_data = [next(cur_table_gen) for _ in range(size)]
    return fake_data, data.append(
        pd.DataFrame([(user.id, user.initials, user.address, user.telnumber) for user in fake_data], columns=COLUMNS),
        ignore_index=True
    )

@app.route('/')
def home():
    context = {
        'size': request.args.get('size', 20),
        'seed': request.args.get('seed', 1)
    }

    return render_template('home.html', **context)

@app.route('/api/generate_fake_data')
def generate_fake_data():
    global cur_table_gen, gen_seed, data
    try:
        size = int(request.args.get('size'), 20)
    except Exception as e:
        return make_response(jsonify({'message': e.__str__()}), 403)
    
    fake_data, data = get_generated_data(size)
    
    return make_response(
        jsonify({'data': [data.to_dict() for data in fake_data]}),
        200,
    )

@app.route('/api/refresh_and_generate_fake_data')
def refresh_and_generate_fake_data():
    global cur_table_gen, gen_seed, data
    try:
        seed = int(request.args.get('seed', 0))
        size = int(request.args.get('size'), 20)
    except Exception as e:
        return make_response(jsonify({'message': e.__str__()}), 403)
    
    cur_table_gen = db_requests.gen_fake_data(seed)
    gen_seed = seed
    data = pd.DataFrame(columns=COLUMNS)
    
    fake_data, data = get_generated_data(size)
    
    return make_response(
        jsonify({'data': [data.to_dict() for data in fake_data]}),
        200,
    )
    

@app.route('/download')
def download_excel():
    file_path = Config.EXCEL_PATH + 'excel_data.xlsx'
    with pd.ExcelWriter(file_path) as writer:
        data.to_excel(writer)
    
    return send_file(file_path, as_attachment=True)