import flask
import db

app = flask.Flask(__name__) 

@app.route('/api/new_recept/by_url/<url>')
def new_recept_by_url(url):
  return f"Added recepts by url {url}"

@app.route('/api/new_recept/by_txt/<name>/<text>')
def new_recept_by_text(text, name):
  db.new_recept(data=text, name=name)
  return f"Added recepts with name {name} and with inside {text}"
 
@app.route('/api/get_recept/<id_> ') 
def get_recept(id_):
  return db.get_recept_by_id(id_) 



db.disp.start()
app.run('0.0.0.0')