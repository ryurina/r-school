from model import *


@app.after_request
def add_header(response):
    response.headers["X-UA-Compatible"] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/students/")
def students():
    all_students = Students.query.order_by(Students.username).all()
    return render_template("students.html", students=all_students)

@app.route("/students/@<username>/")
def profile(username):
    all_students = Students.query.order_by(Students.username).all()
    information = None
    for i in range(len(all_students)):
        if all_students[i].username == username:
            information = all_students[i]

    return render_template("profile.html", student=information)

@app.route("/signup/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        lastname = request.form["lastname"]
        firstname = request.form["firstname"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]
        birthday = request.form["birthday"]
        address = request.form["address"]
        grade = request.form["grade"]
        status = request.form["status"]
        image = request.files["image"]

        bday = birthday.split("-")
        birth = date(int(bday[0]), int(bday[1]), int(bday[2]))

        img_name = str(uuid.uuid1()) + os.path.splitext(image.filename)[1]
        image.save(os.path.join('static/img/profile', img_name))
        hashed_password = sha256(password.encode()).hexdigest()

        new_student = Students(username=username,
                                lastname=lastname,
                                firstname=firstname,
                                email=email,
                                phone=phone,
                                password=hashed_password,
                                birthday=birth,
                                address=address,
                                profile=img_name,
                                grade=grade,
                                status=status)
        try:
            db.session.add(new_student)
            db.session.commit()
            student_links = "/students/{}/".format(username)
            return redirect(student_links)
        except:
            return render_template("signup.html")
    return render_template("signup.html")

@app.route("/login/")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

