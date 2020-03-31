from flask import Flask, request, jsonify
app = Flask(__name__)
 
@app.route('/userLogin', methods = ['POST'])
def userLogin():
    user = request.get_json()#json 데이터를 받아옴
    # additional information
    user["Test"]="test"
    return jsonify(user)# 받아온 데이터를 다시 전송
 
@app.route('/environments/<language>')
def environments(language):
    return jsonify({"language":language})
 
 
if __name__ == "__main__":
    app.run(debug=True)