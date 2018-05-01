import os

ENV_SECRETS = [
	"RIOT_API_KEY",
	"CHAMPIONGG_KEY",
]

FILE_SECRETS = []

class SecretManager(object):
	class __SecretManager(object):
		def __init__(self):
			self.secrets = SecretManager.get_secrets_dict()

	instance = None

	def __init__(self):
		if not SecretManager.instance:
			SecretManager.instance = SecretManager.__SecretManager()

	def __getattr__(self, name):
		if name not in self.instance.secrets:
			raise KeyError("'%s' is not a valid secret key" % name)
		return self.instance.secrets[name]

	def get_secrets_dict():
		secrets_dict = {}
		def _read_env_secret(env_key):
			return (env_key, os.environ.get(env_key))
		def _read_file_secret(file_key, file_path):
			with open(file_path) as file:
				return (file_key, file.read())
		secrets_dict.update(dict(map(_read_env_secret, ENV_SECRETS)))
		secrets_dict.update(dict(map(_read_file_secret, FILE_SECRETS)))
		return secrets_dict
