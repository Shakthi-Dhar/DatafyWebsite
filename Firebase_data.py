import pyrebase

config = {
    "apiKey": "AIzaSyD0ssd1sAVJyu59tOLyV03w9X7Le3o-Q4c",
    "authDomain": "datafy-577f9.firebaseapp.com",
    "databaseURL": "https://datafy-577f9-default-rtdb.firebaseio.com",
    "projectId": "datafy-577f9",
    "storageBucket": "datafy-577f9.appspot.com",
    "messagingSenderId": "151080070844",
    "appId": "1:151080070844:web:cb98371ce89bcd1eef2ab9",
    "measurementId": "G-V6T1KJG9LP"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


# # Path to where the data is to be stored
# path_on_cloud = "Technology.csv"
#
# # Path where you want the data to be stored locally
# path_local = "Technology.csv"
#
# # Command to upload the data to firebase
# storage.child(path_on_cloud).put(path_local)
#
# # Command to download the data from firebase
# storage.child(path_on_cloud).download("test.csv")


def download_csv(file, ext):
    return storage.child(file + ".csv").download("Data\Datafy" + file + "." + ext)
