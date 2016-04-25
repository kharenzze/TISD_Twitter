import tweepy

consumer_key = raw_input("Introduzca el consumer_key >>> ")
consumer_secret = raw_input("Introduzca el consumer_secret >>> ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Ahora necesitamos el access token para los permmisos
redirect_url = auth.get_authorization_url()
print "Puede obtener el access token en este link >>> ", redirect_url
verifier = raw_input("Introduzca el codigo verificador: ")

# Obtenemos y pasamos al objeto 'auth' el token con el codigo antes provisto
auth.get_access_token(verifier)

# Obtenemos un objeto api que necesitaremos para hacer los requests a Twitter
api = tweepy.API(auth)   # Pasando el objeto 'auth' como parametro