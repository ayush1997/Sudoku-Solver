from flask import Flask
from flask import render_template,request,flash,url_for,redirect,session
import os

from copy import copy





app = Flask(__name__)
app.secret_key = "secret"
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

			if sudoku_solver.is_sudoku_unsolvable():
				msg = "NOT SOLVABLE, PLEASE CHECK YOUR INPUT!"
			else:
				msg = "THIS SEEMS TO BE ONE OF THE POSSIBLE ANSWERS."

			print msg
			sol = sudoku_solver.run()
			#print sol
			#print sudoku_solver.grid
			
			
			
			flash(msg)
			return render_template("solved_sud.html",lst=sol,inp = inp)

			#return redirect(url_for("solved",lst = sol,name = 23))
	except Exception as e:
		print e.message




if __name__ == '__main__' :
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0',port=port)
	#app.run(debug=True)

