from flask import Flask, request
import whisper

# Create a Flask server instance
server = Flask(__name__)

model = whisper.load_model("base")


#port
port = 3000

#step1 -Create a Router
@server.route('/dowloadUrl/<url>', methods=['POST'])
def audioDownloadURL(url):
    print('URL :::::', url)
    result = model.transcribe("https://customization-data-8807-dev-ed.scratch.file.force.com/sfc/dist/version/download/?oid=00DO4000000Nwgv&ids=068O4000000IWxs&d=%2Fa%2FO40000003m8A%2FNnamHLEiEtGuMQyShdFeA6Y..KAzUgZhWwPYy4E.c8w&asPdf=false")
    print('Text :::::', result["text"])

    return {'audioText':result["text"] }


# Run the Flask server
if __name__ == '__main__':
    server.run(host='0.0.0.0', port=port)

