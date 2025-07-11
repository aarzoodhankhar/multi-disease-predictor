import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyAoWaR-yPFCJeozYA-zp6zKraO3zQ3TIms",
    "authDomain": "multi-disease-predictor-2ea8c.firebaseapp.com",
    "projectId": "multi-disease-predictor-2ea8c",
    "storageBucket": "multi-disease-predictor-2ea8c.appspot.com",
    "messagingSenderId": "813326664822",
    "appId": "1:813326664822:web:396a0b4e2f7cdbb038cb57",
    "measurementId": "G-2XDXMLRJTJ",
    "databaseURL": "https://multi-disease-predictor-2ea8c-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database() 