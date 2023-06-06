import json
from datetime import datetime
import os

with open("version.txt", "r", encoding='utf-8') as version_file:
    version = version_file.readline().strip()


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
            "versions": [
                {
                    "version": f"0.0.{version}",
                    "date": datetime.now().isoformat(),
                    "localizedDescription": f"{os.environ.get('DESCRIPTION')} - {os.environ.get('COMMIT')}",
                    "downloadURL": "https://imlvna.github.io/vendetta-ipa/Vendetta.ipa"
                }
            ],
        }
    ]
}

with open("pages/vendetta.json", "w", encoding='utf-8') as source_file:
    json.dump(source, source_file, indent=4)
