from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

# Spécifie le port pour Replit
os.environ['PORT'] = '8080'

# Liste de liens aléatoires
liste_liens = [
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=KLtx44onh0bB3jKeoJSFx8uh%2BBlUw2T78KJlzh%2FEetd5cpenFlqs3JCTbCI7AFrN&expiry=V6RBC5AkAxiRo6HQyLoNtA%3D%3D&mac=76d69c2deaf422685104ddbbfa166117e2401c9031e47395fed4ee379e4eb60c",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=aMQca13W2gIZknWQL3wCaqfzBy%2FT3VUznOJlLa5Pe2AAtERCd%2ByAoq177IPzJIRl&expiry=7wkxB%2FiW75pRz5pOFQ4a5A%3D%3D&mac=ecfdf667c5134f0d11bde347602c853076ae708eb50f2c046a97f344190ffaec",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=YbmP4jyaCCVQ9M8dQKXDG5nDxcQocDEm3qbqoqX4y23SxIERPB30KZVwwiRAxVsy&expiry=iUFDVaz8GwKZoEylMxAXFw%3D%3D&mac=b768c13e7086deeaf0c8abe693c382818c0fa7a3dace43d0306d6ef1ccff3dcc"
]

@app.route('/')
def lien_aleatoire():
    lien = random.choice(liste_liens)
    return jsonify({"lien": lien})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)
