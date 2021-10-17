import flask
import db

app = flask.Flask(__name__) 

@app.route('/api/new_recept/by_url/<url>')
def new_recept_by_url(url):
  return f"Added recepts by url {url}"

@app.route('/api/new_recept/by_txt', methods=["POST"])
def new_recept_by_text():
  name = flask.request.form.get('name')
  text = flask.request.form.get('text')
  db.new_recept(data=text, name=name)
  return f"Added recepts with name {name} and with inside {text}"
    
@app.route('/api/new_recept/by_file')
def new_recept_by_file():
    return (403)


@app.route('/get_recept/<uid>') 
def get_recept(uid):
  data = db.get_recept_by_id(uid)
  return flask.render_template("recept.html", title=data[1], content=data[2]) 

@app.route('/new_recept/text') 
def form_new_text():
    return flask.render_template("new_recept_by_text.html")


db.disp.start()
app.run('0.0.0.0')