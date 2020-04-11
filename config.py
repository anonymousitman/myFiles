PORT = 8585

# name -> secret (32 hex chars)
USERS = {
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Compatible only with the recent clients
    "tls": True
}
# Makes the proxy harder to detect
# Can be incompatible with very old clients
# SECURE_ONLY = True

# Makes the proxy even more hard to detect
# Compatible only with the recent clients

# The domain for TLS, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "google.com"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"
