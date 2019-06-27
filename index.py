from firebase import firebase
firebase = firebase.FirebaseApplication("https://skripsiph.firebaseio.com/")
data = {
	'nama': 'Lilis',
	'test': 'test'
}

result = firebase.post('/python-sample', data)
print(result)
