# End To End Machine Learning Project

## Run from terminal

docker build -t containermn.azurecr.io/app:latest .

docker login containermn.azurecr.io

docker push containermn.azurecr.io/app:latest
