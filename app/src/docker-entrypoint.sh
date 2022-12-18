while ! nc -z $AUTH_POSTGRES_HOST $AUTH_POSTGRES_PORT;do
      sleep 0.1
done
python pywsgi
