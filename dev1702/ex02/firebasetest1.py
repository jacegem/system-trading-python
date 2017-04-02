from firebase import firebase
firebase = firebase.FirebaseApplication('https://myfirstapp-bcfdc.firebaseio.com/', None)
result = firebase.get('/2016', None)
print(result)

# {'1': 'John Doe', '2': 'Jane Doe'}