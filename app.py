from flask import Flask
from flask import render_template,request,flash,url_for,redirect,session
import os

from copy import copy





app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')

@app.route("/user/<username>")
def profile(username):
	return render_template("profile.html",name = username)


@app.route("/header/")
def header():
	return render_template("header.html")


@app.route("/output/",methods=['GET','POST'])
def output():
	
	

	return render_template("output.html")

@app.route("/solved_sud/",methods=["GET",'POST'])
def solved():
	try:
		lst = [[],[],[],[],[],[],[],[],[]]
		lstnew = [[],[],[],[],[],[],[],[],[]]
		
		count = 0
		if request.method == "POST":
			inp = request.form.getlist("num")
			for i in range(0,81):
				inp[i] = int(inp[i])
			#print inp
			for r in range(0,9):
				for c in range(0,9):
					lst[r].append(inp[count])
					count = count +1
			#print lst
			import info
			#print info.grids
			
			
			info.grids = lst
			#print info.grids

			#print info.grids
			import sudoku_solver 
			sudoku_solver.grid = lst
			#print info.grids
			#print sudoku_solver.grid
			sol = sudoku_solver.run()
			#print sol
			#print sudoku_solver.grid
		
			
			

			return render_template("solved_sud.html",lst=sol,inp = inp)

			#return redirect(url_for("solved",lst = sol,name = 23))
	except Exception as e:
		print e.message


#class Registrationform(Form):
#	username = TextField("Username",[validators.Length(min=4,max = 20)])
#	email = TextField("Email address",[validators.Length(min=6,max='50')])
#	password = PasswordField('Password',[validators.Required(),
#		validators.EqualTo('confirm',message="wrong ")])
#	confirm = PasswordField('Repeat password')
#	accept_tos  = BooleanField("i accept",[validators.Required()])



#@app.route("/register/",methods = ["GET","POST"])
#def registerpage():
#	try:
#		form = Registrationform(request.form)
#		if request.method =="POST" and form.validate():
#			username = form.username.data
#			email = form.email.data
#			password = sha256_crypt.encrypt((str(form.password.data)))
#
#		return render_template("register.html",form=form)
#
#		session["logged_in"] = True
#		session["username"] = username
#	except:
#		pass



#@app.route("/login/",methods = ['GET','POST'])
#def login():
#	error =None
#	try:
#		if request.method =="POST":
#			attem_username = request.form["username"]
#			attem_password = request.form["password"]
#			writetext(attem_username)
#			
#
#
#			if attem_username == "admin" and attem_password =="password":
#				return redirect(url_for('profile',username = attem_username))
#			else:
#				return redirect(url_for("index"))	
#
#		return render_template("login.html",error=error)		
#	except:
#		return redirect(url_for("aab",username ="asd"))	


if __name__ == '__main__' :
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0',port=port)

