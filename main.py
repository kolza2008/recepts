import flask

import db

app = flask.Flask(__name__) 


@app.route('/new_recept', methods=["POST"])
def new_recept_by_text():
  if not flask.request.form.get('type'):
    name = flask.request.form.get('name')
    text = flask.request.form.get('text').replace('\n', '<br>')
  return str(db.new_recept(data=text, name=name)) #f"Added recepts with name {name} and with inside {text}"

@app.route('/get_recept/<uid>', methods=["POST", "GET"]) 
def get_recept(uid):
  data = db.get_recept_by_id(uid)
  if flask.request.method == 'GET':
    return flask.render_template("recept.html", title=data[1], content=data[2]) 
  return flask.jsonify(data)

@app.route('/new_recept/text') 
def form_new_text():
    return flask.render_template("new_recept_by_text.html")


db.disp.start()
app.run('0.0.0.0')
