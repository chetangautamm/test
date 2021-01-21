FROM ubuntu:16.04
MAINTAINER chetan chetangautamm99@gmail.com

RUN apt-get update
RUN apt-get install -y net-tools
RUN apt-get install -y nano
RUN apt-get install -y sip-tester
RUN apt-get install -y dh-autoreconf
RUN apt-get install -y ncurses-dev
RUN apt-get install -y build-essential
RUN apt-get install -y libssl-dev libpcap-dev
RUN apt-get install -y libncurses5-dev
RUN apt-get install -y libsctp-dev lksctp-tools
RUN apt-get install -y wget
RUN apt-get install -y make
RUN apt-get install -y git
WORKDIR /home/
RUN mkdir sipp
WORKDIR sipp
RUN wget https://github.com/SIPp/sipp/archive/v3.4.1.tar.gz
RUN tar -xvzf v3.4.1.tar.gz
WORKDIR sipp-3.4.1
RUN ./configure
RUN make
