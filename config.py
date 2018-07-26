import os
# pulling from enviromental variable,
MONGODB_SETTINGS = {
    'host': os.environ['DATABASE_URL']
}
THREADS_PER_PAGE = 2
# secret key for cookies
SECRET_KEY = os.environ['SECRET_KEY']
JWT_SECRET_KEY = os.environ['SECRET_KEY']
