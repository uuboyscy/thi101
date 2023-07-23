from flask import (
    Flask,
    request,
    jsonify,
    render_template
)

import poker as p
import model

app = Flask(__name__, static_url_path="/source", static_folder="./source")


@app.route("/")
def index_page():
    return "Hello Flask!"


# /hello/Allen
# @app.route("/hello/<username>")
# def hello(username: str):
#     return "Hello %s !" % (username)


# /hello/Allen
@app.route("/hello/<username>")
def hello(username: str):
    return render_template(
        "hello.html",
        username=username,
    )


# /two_sum/3/5
@app.route("/two_sum/<int:x>/<int:y>")
def two_sum(x: int, y: int):
    return str(x + y)


# [GET] /get_employee/<str:dep_id>/<str:team_id>
# [GET] /get_employee?dep_id=xxxx&team_id=aaa
@app.route("/get_employee/<dep_id>/<team_id>")
def get_employee(dep_id: str, team_id: str):
    sql = """
        SELECT
            emp_name,
            emp_id,
            emp_dep_id,
            emp_team_id,
            emp_age
        FROM employee
        WHERE emp_dep_id = '%s' AND emp_team_id = '%s'
    """ % (dep_id, team_id)

    data = fetch_data(sql)

    return data


# /hello_get?username=Allen&age=22
@app.route("/hello_get")
def hello_get():
    username = request.args.get("username")
    age = request.args.get("age")

    if username is None:
        return "What is your name?"
    elif age is None:
        return "Hello %s." % (username)
    else:
        return "Hello %s, you are %s years old." % (username, age)


# @app.route("/hello_post", methods=["GET", "POST"])
# def hello_post():
#     result = """
#         <form action="/hello_post" method="POST">
#             <label>What is your name?</label>
#             <input name="username">
#             <button>SUBMIT</button>
#         </form>
#     """

#     request_method = request.method  # POST, GET
#     if request_method == "POST":
#         username = request.form.get("username")
#         result += """
#             <h1>Hello %s !</h1>
#         """ % (username)

#     return result


@app.route("/hello_post", methods=["GET", "POST"])
def hello_post():
    request_method = request.method
    username = request.form.get("username")

    return render_template(
        "hello_post.html",
        request_method=request_method,
        username=username,
    )


# # /poker/<int:player>
# @app.route("/poker/<int:player>")
# def poker(player: int):
#     result = p.poker(player)

#     return jsonify(result)


@app.route('/poker', methods=['GET', 'POST'])
def poker():
    request_method = request.method
    players = 0
    cards = dict()
    if request_method == 'POST':
        players = int(request.form.get('players'))
        cards = p.poker(players)
    return render_template('poker.html', request_method=request_method,
                                         cards=cards)


@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
