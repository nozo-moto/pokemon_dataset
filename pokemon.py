import json
import time
import urllib.request
import urllib.parse
from tqdm import tqdm
from pprint import pprint

zukan_url = "https://www.pokemon.jp/zukan/scripts/data/top_zukan.json"
pokemon_url = "https://www.pokemon.jp/api.php"
pokemon_img_url = "https://www.pokemon.jp/zukan/images/l/"

def get_zukan():
    req = urllib.request.Request(zukan_url)
    with urllib.request.urlopen(req) as res:
        zukan = json.loads(res.read().decode('utf8'))
    return zukan

def get_pokemon(poke_data):
    data = {}
    data['zukan_no']     = poke_data['zukan_no']
    data['sub_id']       = poke_data['sub_id']
    data['pokemon_name'] = poke_data['pokemon_name']
    data['takasa']       = poke_data['takasa']
    data['omosa']        = poke_data['omosa']
    data['sub_name']     = poke_data['sub_name']
    data['type']         = poke_data['type']
    data['tokusei']      = poke_data['tokusei']
    

    req = urllib.request.Request(pokemon_url, data=urllib.parse.urlencode(data).encode("utf-8"))
    with urllib.request.urlopen(req) as res:
        pokemon_detail = json.loads(res.read().decode('utf8'))

    return pokemon_detail

def download_pokemon_img(poke_data):
    with urllib.request.urlopen(pokemon_img_url + poke_data["filename"]) as req:
        img_data = req.read()
        with open(poke_data["zukan_no"] + ".png", mode='wb') as f:
            f.write(img_data)

if __name__ == "__main__":
    zukan = get_zukan()
    for z in tqdm(zukan):
        poke_detail = get_pokemon(z)
        download_pokemon_img(poke_detail)
        time.sleep(1)
