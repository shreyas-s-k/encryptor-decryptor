from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def my_form_post():
    result=""
    text = request.form['text']
    message=text
    if request.form['submit'] == 'Encrypt':	
        if text=="":
            return render_template('error.html')
        else:		
            for i in range(len(message)):
                result=result+chr(ord(message[i])-2)
            return render_template('result.html',result=result,res="Encrypted",op="Encryption")
    else:
        if text=="":
            return render_template('error.html')		
        else:		
            for i in range(len(message)):
                result=result+chr(ord(message[i])+2)
            return render_template('result.html',result=result,res="Decrypted",op="Decryption")		
			
if __name__ == "__main__":
    app.run()





	
