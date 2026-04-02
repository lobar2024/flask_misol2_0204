from flask import Flask, render_template

app = Flask(__name__)

temperature = 30

@app.route('/weather')
def weather_page():

    return render_template(
        'weather.html', temperature = temperature
    )


if __name__ == '__main__':
    app.run(debug=True)
