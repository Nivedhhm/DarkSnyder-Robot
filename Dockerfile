RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /DarkSnyder-Robot
WORKDIR /DarkSnyder-Robot
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]




