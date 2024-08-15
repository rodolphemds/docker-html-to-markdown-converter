# HTML to markdown converter
This is to create a docker container allowing to convert an html text to a markdown readable file. 

## 1. Copy the file to convert into the base folder of the repository and name it "file_to_convert.html"

## 2. Build docker image

```sh
docker build -t html-to-md-converter .
```

## 3. Run docker

```sh
docker run --name html-to-md-converter-container html-to-md-converter
```