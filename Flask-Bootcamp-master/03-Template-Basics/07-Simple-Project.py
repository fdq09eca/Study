# Set up your imports and your flask app.
from flask import Flask, request, render_template
import re
app = Flask(__name__)
@app.route('/')
def index():
    # This home page should have the form.
    return render_template('07-myform.html')


# This page will be the page after the form
@app.route('/report')
def report():
    username = request.args.get('user_name')
    pattern = re.compile("(?=.*[a-z])(?=.*[A-Z]).*\d$")
    match = re.match(pattern, username)

    reasons = []
    if len(username) == 0:
        reasons.append('No username is typed')
    else:
        if not username[-1].isdigit():
            reasons.append('Does not end with a number')
        if not re.match('(?=.*[a-z]).*', username):
            reasons.append('No lowercase')
        if not re.match('(?=.*[A-Z]).*', username):
            reasons.append('No uppercase')

    return render_template('07-myreport_pos.html', username = username, match = match, reasons = reasons)
    # else:
    #     return render_template('07-myreport_neg.html', username = username)

    # Check the user name for the 3 requirements.

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input
if __name__ == '__main__':
    app.run(debug=True)
