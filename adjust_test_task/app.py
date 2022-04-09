from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
import pandas as pd

# if imported, this name is used
app = Flask(__name__)
app.config.from_object(Config)

# connect app and db
db = SQLAlchemy(app)


class Dataset(db.Model):
    __tablename__ = 'dataset'
    id = db.Column(db.Integer, primary_key=True)  # unique key for each item
    date = db.Column(db.Date, nullable=False)
    channel = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(2), nullable=False)
    os = db.Column(db.String(10), nullable=False)
    impressions = db.Column(db.Integer, nullable=False)
    clicks = db.Column(db.Integer, nullable=False)
    installs = db.Column(db.Integer, nullable=False)
    spend = db.Column(db.Float, nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    cpi = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.id} {self.date} {self.channel} {self.country} {self.os} {self.impressions} {self.clicks}' \
               f'{self.installs} {self.spend} {self.revenue}'


# two auxiliary functions

# checks if query form was filled with data
def check_query(_request):
    _query = ''

    # query extraction depends on where it comes from
    if _request.method == 'GET':
        string = _request.query_string.decode('utf=8')  # decode bytes
        if string.strip():  # ignore empty strings
            _query = string.split('query=')[1]
    else:
        string = _request.form['query']
        if string.strip():
            _query = string

    return _query


# processes raw query for sqlalchemy
def process_query(_query):

    try:
        _result = db.session.execute(_query)
    except Exception as e:
        return f"Error while processing your SQL query. Please, make sure it's correct.\n{e}"

    df = pd.DataFrame(data=_result.fetchall(), columns=_result.keys())
    return df


# routes

@app.route('/main_page/')
def main_page():
    return render_template('main_page.html')


# redirect to the main page
@app.route('/')
def host_url():
    return redirect('main_page')


# displays dataset and takes queries to work with it
# can take queries from the query form as well as urls
@app.route('/database_interaction/', methods=['POST', 'GET'])
def database_interaction():
    sample_dataset = Dataset.query.all()
    query = check_query(request)

    # if got a query, redirect it to be processed and display the result
    if query:
        return redirect(url_for('retrieve_data', _query=query))

    return render_template('db.html', list=sample_dataset)


# displays result of the processed query
@app.route('/database_interaction/result', methods=['POST', 'GET'])
def retrieve_data():

    # redirect query here to be processed
    _query = request.args.get('_query')
    result = process_query(_query)

    # in case there is an error
    if type(result) != str:
        return render_template('result.html', tables=[result.to_html(index=False)])
    else:
        result = result.split('\n')
        return render_template('result_error.html', text=result[0], error=result[1])


# run server, display errors (debug=True) if needed
def main():
    app.run(debug=False)


# if imported, don't execute
if __name__ == '__main__':
    main()
