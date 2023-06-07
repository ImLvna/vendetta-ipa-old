import json
from datetime import datetime
import os


entitlements = [
    "com.apple.security.application-groups",
    "com.apple.developer.associated-domains",
    "beta-reports-active",
    "com.apple.developer.storekit.request-data",
    "get-task-allow",
    "aps-environment"
]
permissions = {
    "BluetoothAlways": "Discord uses Bluetooth to connect to other devices.",
    "BluetoothPeripheral": "Discord uses Bluetooth to connect to other devices.",
    "Camera": "You can take photos and videos inside Discord.",
    "Contacts": "Discord can access your contacts to help you find friends.",
    "LocalNetwork": "Discord uses your local network to connect to other devices.",
    "LocationAlwaysAndWhenInUse": "Discord uses your location to help you find friends.",
    "LocationWhenInUse": "Discord uses your location to help you find friends.",
    "LocationAlways": "Discord uses your location to help you find friends.",
    "Microphone": "You can record audio messages inside Discord.",
    "PhotoLibraryAdd": "You can save photos and videos inside Discord.",
    "PhotoLibrary": "You can send photos and videos inside Discord."
}

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
            "version": f"0.0.{os.environ.get('NUMBER')}",
            "versionDate": datetime.now().isoformat(),
            "size": os.path.getsize("pages/Vendetta.ipa"),
            "versionDescription": f"{os.environ.get('DESCRIPTION')} - {os.environ.get('COMMIT')[:7]}",
            "downloadURL": "https://imlvna.github.io/vendetta-ipa/Vendetta.ipa",
            "beta": False,

            "appPermissions": {
                "entitlements": ({"name":entitlement} for entitlement in entitlements),
                "privacy": ({"name":perm, "usageDescription":desc} for perm, desc in permissions.items())
            }
        }
    ]
}

with open("pages/vendetta.json", "w", encoding='utf-8') as source_file:
    json.dump(source, source_file, indent=4)
