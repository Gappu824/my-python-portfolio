# app.py - Main Flask Application
from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

# --- HOME PAGE ---
@app.route('/')
def home():
    name = "Subhav Mittal"
    # Bonus: Display today's date using datetime module
    today = date.today().strftime("%d %B %Y")
    return render_template('home.html', student_name=name, today_date=today)

# --- ABOUT ME PAGE ---
@app.route('/about')
def about():
    return render_template('about.html')

# --- HOBBIES PAGE ---
@app.route('/hobbies')
def hobbies():
    my_hobbies = [
        "Playing Different Sports",
        "Gaming (Specifically FIFA)",
        "Eating Different Cuisines",
        "Cooking",
        "Travelling"
    ]
    return render_template('hobbies.html', hobbies=my_hobbies)

# --- CUSTOM PAGE: FIFA ---
@app.route('/fifa')
def fifa():
    return render_template('fifa.html')

# --- BONUS PAGE: PYTHON FACTS ---
@app.route('/facts')
def facts():
    return render_template('facts.html')

# --- QUIZ PAGE ---
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# --- QUIZ RESULT ---
@app.route('/result', methods=['POST'])
def result():
    # Bonus: Keep score using Python variables
    score = 0
    total_questions = 3

    if request.form.get('q1') == 'Guido van Rossum':
        score += 1
    if request.form.get('q2') == '#':
        score += 1
    if request.form.get('q3') == 'def':
        score += 1

    return render_template('result.html', score=score, total=total_questions)

# --- CONTACT PAGE ---
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    thank_you = ''
    if request.method == 'POST':
        visitor_name = request.form.get('name')
        thank_you = f'Thank you, {visitor_name}! Your message was successfully received.'
    
    return render_template('contact.html', message=thank_you)

# --- RUN THE SERVER ---
if __name__ == '__main__':
    app.run(debug=True)