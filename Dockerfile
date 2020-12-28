FROM alpine:3.7
RUN apk add --update python3 py-pip
COPY . /exam_Buravchenko
WORKDIR /exam_Buravchenko
ENTRYPOINT ["python3"]
CMD ["programm.py"]