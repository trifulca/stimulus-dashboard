from sanic import Sanic
from templates import render

app = Sanic()
app.static('/static', './static')

@app.route('/', methods=["HEAD", "GET"])
async def hello_world(request):
    return render("home.html", nombre="pepe")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True)
