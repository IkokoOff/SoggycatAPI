from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

# Spécifie le port pour Replit
os.environ['PORT'] = '8080'

# Liste de liens aléatoires
liste_liens = [
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=1QjI8HJRqDeAXFtPv9j%2FMC6Zsuw6bMVwZu8%2FLT2QbJqr%2B%2BI%2BsouutvSDjmJOPibd&expiry=Z5Lw1OWF7N5WnUwZKsyi2w%3D%3D&mac=3404de9f27109babb597c1f5454a2e7f27059bf8b0e49b5f9501425e17935b98",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=sOg7g8DpDXOICeRne4EYmaZCHBdPt8iu8RQwiUSYU6jlyvq7Fac6ahbS1cDYojpC&expiry=qUFAy5cETGZ3RJ1ePU%2BoAA%3D%3D&mac=c98079ce2c0c73d8c006247141a3faafbbb9f4f772bd94a844a8865de0371d85",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=KLmSCXx%2F5Shb4NPDvxs2i87OR4FKGAotWqnheZqVXVeoL6SFmXS2IsU%2F8qxhaGnf&expiry=mGTemXOMrnrBphc0inOBSA%3D%3D&mac=ef9e2082e7bcdd47aa1efe437ff0314ea436c3081013ed382f0db05c131329de",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=qbNTHPX5ZBWrtjqsiJ4dMxTJ56pYHh4Gump3Mo%2FBX94HJkn7OFaDK%2FXPRTGx5zz8&expiry=GxF8Mts%2FJ%2FK2TS5FhUNROA%3D%3D&mac=6f62e5c1fd8ce6904435ccbe6628c97593b329a0b66ad22f0a8545f1c4ed516d",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=9rKnTqmPChPNrd%2FWTziGFsuwb%2F6r14rNKoS6PjiYl1mflV2KGr%2BgwAibVysB%2Bjdh&expiry=GCeZX2zsWlX6tC8Eh5RUxA%3D%3D&mac=26a37e4f46803c5eec172c7fc3cfb0daeed32bec02c2fa4ab8faa8dc6bc4b61a",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=g3ag27vFj0CX7zydWcUK23tnaqhTCyHrGPPeZfSXxtqaQd9gfHAhKOpfnb8PHNFI&expiry=t%2FVRlMLb14C2VdCWAw72ZA%3D%3D&mac=574a8eed5f45a1c76b4b30d972b9b635b4b45fae6605c73a60d9c52e2e67361e",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=GzRHFhduEPXh8DrY%2BrfHbhoFv1k2juu7GjkF6WSQvqPET5xCQkWlBXYaofiFXKsd&expiry=eNoI0zcwdvxUQlXqgK%2FSvQ%3D%3D&mac=0c6696cc12db6debe10306546733711be93d02e8d192b1788914c82507741c05",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=6eKVC6VTWDOs58xw7Bhf9a4V7IyIJqaM%2FaNjWs9dIcXRPZQ9veqMvABLISi0tBzp&expiry=LP53wCDg89c6fvgPN3kStA%3D%3D&mac=eec86a6a58bcac2dcb55380129e89453c9c12d51f33f0e62b31c61caaadf1c31",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=%2FdRXHfcYgvNSGPVnNAr0wShMDkE%2BTiEEU2j%2BydtPOZuAtclyEG4mNsATBFdzSFMT&expiry=SKq7Q8K%2FkJNXXZQv8XCTdw%3D%3D&mac=7845089f9a60346c638b02da9fcdcb7f77d00dcf7ed3fb7f9919ac4f1755a3ad",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=33NZzhCD9P97G3Sk7qbTm0bDFg1%2Fl0bFgy0x50VSIzgCyYVb%2B7LvBTlw1yYbZosb&expiry=%2BSaCFKPkRqQ%2Bi4SadJ54Cw%3D%3D&mac=4915ee1455fc408915e595d50d898e466511dbcce2883b5a455d4588725d231e",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=ne2IeB1MlocGBnuR9eyafgcwknLQ2J6nmm%2FA72rtXflq15kTbPXT9NZes0wRozIU&expiry=m2DjP2Gc7MlV6sovONjzCw%3D%3D&mac=178dbe9723e66366dabb46b689144b2b92bed7a78eb66c20ef2e4b34e3483318",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=EsM7zKwORjL3vURn%2FCcEFTAMBAYsdiZEvLN53lqf1B1FCAEckuC4gfyRtZl6Pq9d&expiry=VMCIJDiKoF7uce27XhFu4Q%3D%3D&mac=7f3c23974ae23bf26a37c5f6402f11467a2388c3dc34429e5581af97a925cad2",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=Nt37bJUELyph3eHY2Gt3tVUbyJYwl7h%2F27MUfje9oLoToHwV2vARpWw2t0TW0rG3&expiry=%2BrKosPcS%2BgLz8m71xqhQ4g%3D%3D&mac=28c20bdc7f7f91f3cc6e3c622dc2c8173b862b368423f673e6c64aeaae87e662",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=nqw%2BwVn%2FC626wU8kCG6wB60PeeBDlBrb5K2DZFjYiDd%2FH3TRkugZZyVFWe3HtUvS&expiry=TC5EKsR0LqdLpoGm10YN9Q%3D%3D&mac=f2b396a026740034a7d911dab29f62cc8f11116cc5fd88f2608a157b2b87452c",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=v5oYFovy0H0%2Fyzku1VS%2BKyzyfM5QmFOdvN5kk%2Bx%2Ff1oSdEg8Ndgw%2BBTZMhN0O7Yn&expiry=UigLMgQ5MYXT3dp9aP5GSA%3D%3D&mac=6c87caec477968815c5a066b58ac8b1ca5764edc6e1e9aa0bdf559e0734ceac2",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=Qn3w%2B40TpuwMXMKisOxXeTSDz8WC2lWcFhttVAungbk26E%2F4vjNZ%2BXY8qpyVZRQZ&expiry=FZXxf8XOSic5bADM%2FrrjIg%3D%3D&mac=d2ef75c4683b29b83079cae93b64a80d9eb00cdf8d9c43c91148017d842197e5",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=K4m%2FZTJAMJ00CqNE5fFWQd0BBFrYsqOW6gMBK5y7x8xuMs6YtHaxJNl70AOFgaZU&expiry=6ZtuFexAcUe6NtcFDjjQWA%3D%3D&mac=96b49d020a7319247aa5d676b300dcd33b020b03b86df5a0ea8c67d48e678774",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=BmEF6AiPW%2F1TlBnCUC%2BzgsmJjhRC4QJWkaRTBRkBhOYAm3sK%2BZfiyOKYb5YAM7%2Bt&expiry=AAZLeSQss1kpce6ELh6sJQ%3D%3D&mac=b77210655142b985eb1f6d73fb6f61bd5816df54fcb32eccd1982fc93b57aa6c",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=0SdHxvyxp50BucBQBPDQjfCfxTple%2BFkRVDjma087hQUm65CqEGU9Ja0MjBaJXZ9&expiry=TCFolUpbeis2OiG7g%2FgAjQ%3D%3D&mac=a251c48aa59da7861183aad5ac26795ad501494feb0ffbeb21f2eba96fd7f2bc",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=M6%2BgoRwY2YzIFz%2Bq6p0ULdWM38nfzWIw73qXFy0GkuJ8mpmvIRzV3QdJEnjHTbNE&expiry=FsDJiYVvEieDDrYFn1xeMw%3D%3D&mac=bca08d6b10d77f75bb07430123e66f33ee1f3f9f841a73852414753706848061",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=jtmdKOHSdTSXaavxxeUTqK84L61tJ8GkndiEyTVg88MsF4VV5%2Bi1xku4g%2FGDCdPh&expiry=ouSmeToZZ1%2BprHEyiNE6Fg%3D%3D&mac=ff0c8424bcf7facf8c41bc22dd3821e455041748d6dadf5c9da2e29a7eff270e",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=cw3NTbXEiWRWln5m3DVnQVz1gCAr0QyWMK%2BHe4oeQDU7KRTrvtUhLcrQ4OedXYZU&expiry=tB0903trBeKSjJqj6uRJuQ%3D%3D&mac=bd1584d8b2cc55bd1d9ef257e42f354adad66091c3c171fc626e106a9c9c562f",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=4Uhzr%2FACnea52IUfMGYt%2B251To5t0L%2FoNk8LAGdSdPBUowFvakHujTyE1dWsW%2Fdo&expiry=xct%2Fv47FRPy8U9R6seAKVg%3D%3D&mac=900afcd5479add1f282c47452afc78d9478a30c6ba5b993d12911a2a227e8af9",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=%2BH9lc8UXwwM2f7f8n8SAULTjyPd%2B5hBhibO%2FaICUZ1ZC2a2WjsXG40PgfG6SOn4l&expiry=jjQVEnY9XXDfDrpo0%2BdOEA%3D%3D&mac=edc3d0c446c00f850de8e123f5af6edc3e93b77a1a97a2db484b0711af5b3354",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=afYl8LIc8pGsw%2Fl8Ws25%2FomUx49f9h21OBWSR0%2FIaZSbEeipyInEAzSiLwGly0iA&expiry=PIHatY6YvA9YDPFvSD5lFA%3D%3D&mac=58cc56854459e954fef4c55d00496ba5bcc49b927916477330d1abe9e9c8b745",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=vUGjtpy%2FanyMI%2Fau8rM5M8gkrbqtLsS70PVHsGU8VooTTW2glG%2B6uKD%2Fopwq9OwO&expiry=XfDABAni%2FNJ0RmWMbQEdNA%3D%3D&mac=901cd241cc919e11fd78c82c92f6fd7c649c32e3b86777b19f77f889a8ed9528",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=eCCEZkWLgTGSFSkLkXuhWXqAk82Jpk9bcvlPzWLH3rdYP%2Ff5BLcvnjy6IZhLmFp0&expiry=FMCBTivDMJLmc7tSwkbIBQ%3D%3D&mac=ef9aedd14ae06f7f21e8e7eaa922689d660d477220713c5b85a16facc6b21852",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=DH0VhdqZRWvTdSBCD0urgoJ8L2cf%2BW4089og008NpTKWfOWKknwWIiGRzAgi%2BVvC&expiry=r9XhIvAE%2FOgGz9NUftn0UA%3D%3D&mac=2a42c15e9eae51dd013e1e9c4ca4b6c922e3b43e142f3ffdd11b30368bdcbaf6",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=x9yGFrlzh07ThPgjzTnmbZ7k6OKx9Cl171uIlKqt685jij2x%2FveSxA%2FWInYekM2i&expiry=5VUmRULQVWvd8Ki%2Byx7L3A%3D%3D&mac=275f3d3305a3c6700a3208327c065643ce2d0ce5c453ae7294331406cfbda471",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=AYTdCyvNed9%2BoeUSRJR1GRw7B4Pb3qxGnwnN%2B1fq2IwFNsuP2MNxmHq%2BEjErrKSU&expiry=zvAK6WWqBKc9kpuUJ78V%2BQ%3D%3D&mac=dcd20bec85f54b22db0913a5beed91c9fe241f60b856a71c5ac72c45e3531c91",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=XWhPyYNIcZmn9OF7IhMSmFDf0ziQ9EWHwh6hl58IBXCaFGbeU5Qd6MOdCDY32jzA&expiry=ZB3WNoqToX2GPafS81QVUA%3D%3D&mac=5570b7499e2496605732cb108081341bb4084b9acc1d9bb86e62dce8d8ef4d85",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=O1Bzk5qG9Zp9RJmAMDdosORu9tSVylOGReXfSLm6WjN9lYuzmsjDddBz0OQm%2BSeY&expiry=LhugjPSacYhNVBndESkskw%3D%3D&mac=265a9c299684e1770832fab73463c9f99e59c294c68006ef9b1fe63538e11716",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=x2nCZKkNWxaogD3Dpoe3QAD%2B7tGvOATByFdDkJoxF%2FT9Wcvdt7K9V4udaMw2qUJr&expiry=CEhsj%2FztDsM9Zeaw0wLvNg%3D%3D&mac=0ab53774ab2d038694a973f364b634bdc328457c86667f61521dadfa8c9fd244",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=0%2BXFxi8uAS7qcLcfAPIUo9raS44PiSygCMogAGgk%2B8brqxTxu7FJV8vUXxt5xuC4&expiry=dRoSw%2B9EIjEtdM%2BKclzTnA%3D%3D&mac=deb0f0a5290148fd8ae86f8163a38dec591edac3e4d54ac40a74533a27b352f4",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=2G%2B%2B0PrebT7wwZki6F8SfkwKWS11WiMts025bj4i03DrKPkyD2X9ezlqX2JJA0nV&expiry=qpLD%2FJv7dWKuPNamRJubFg%3D%3D&mac=5e5df09c39874f3219deff3c73d743074b945048a3a9403c33ad7b3cdc1e1bf8",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=j0598H%2FfawkRq76%2F4RD4qp6IO4v5G4%2BDLkW%2Fm6P4%2FwRoox8So0ULOx3xOr6MHc0a&expiry=7tHReZEsxmrXVBRv9DOlew%3D%3D&mac=5914c7563dee90d363b76edec5a8a1fcc4c92facb8190103ccbe18433ae2ae5f",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=q%2Fi6xa4P3jZIKj56IQr%2BDn4o1YhPJmdiyChLcu27PThdYtQLJGxd83C324cunvKg&expiry=uNHuFWkfVK4ERS9oYoKAJw%3D%3D&mac=cc63efb84128966c8bc5baf426bf9e3b407a5164136d5b20a217ee3b9bd059f7",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=p%2Fpjq0C9IshIEmOkxSNkVPy4bRu3cr4UKZZYOvSm7bQQiCwF%2BtNjOpvmgmd2C2B3&expiry=qJXSpXsDMNPxZEW6HFNfhQ%3D%3D&mac=f8742e64e0589e871140ba04f1dc64d79d2dd0d94e05d065a8782e37520b27fc",
    "https://soggydriveindex.niofluff.workers.dev/download.aspx?file=a5cbzIDibLgb%2BWiCBlycGE5uxMNaJAvCrpJL7TbCF9DnLyd%2BnPIyBJHvnI5q3l26&expiry=yDWefKjHyABDc4Lzlu5fxw%3D%3D&mac=949893b2cce806208d412509f1edf02886aeec2815f6b0592245c0c6adfafa9a",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]

@app.route('/')
def lien_aleatoire():
    lien = random.choice(liste_liens)
    return jsonify({"lien": lien})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)
