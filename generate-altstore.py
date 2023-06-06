import json
import os
from subprocess import check_output

with open("version.txt", "r", 'utf-8') as version_file:
    version = version_file.read()

source = {
    "name": "Vendetta",
    "identifier": "dev.beefers.vendetta",
    "description": "A mod for Discord",
    "iconURL": "https://avatars.githubusercontent.com/u/112445065?s=500",
    "website": "https://discord.gg/n9QQ4XhhJP",
    "tintColor": "#3ab8ba",
    "featuredApps": [
        "dev.beefers.vendetta"
    ],
    "apps": [
        {
            "name": "Vendetta",
            "bundleIdentifier": "dev.beefers.vendetta",
            "developerName": "Beef",
            "localizedDescription": "A mod for Discord",
            "iconURL": "https://avatars.githubusercontent.com/u/112445065?s=500",
            "tintColor": "#3ab8ba",
            "versions": [],
        }
    ]
}


for file in os.listdir("ipa"):
    if not file.endswith(".ipa"):
        continue
    numeric_version = int(file.split("-")[0])
    commithash = file.split("-")[1]

    isodate = check_output(["bash" "-c" f"""
    cd Vendetta
    git show -s --format=%ci {commithash}"""]).decode("utf-8").split(" ", maxsplit=1)[0]
    commitdesc = check_output(["bash" "-c" f"""
    cd Vendetta
    git show -s --format=%s {commithash}"""]).decode("utf-8")


    source["apps"][0]["versions"].append(
        {
            "version": f"0.0.{numeric_version}",
            "date": isodate,
            "localizedDescription": commitdesc,
            "downloadURL": "https://imlvna.github.io/vendetta-ipa/ipas/" + file
        }
    )


with open("pages/vendetta.json", "w", encoding='utf-8') as source_file:
    json.dump(source, source_file, indent=4)