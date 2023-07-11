docker run -d -p 9200:9200 -p 9300:9300 --name elasticsearch docker.elastic.co/elasticsearch/elasticsearch:7.14.0
docker run -d --link elasticsearch:elasticsearch --name logstash -v /path/to/logstash/config:/usr/share/logstash/config docker.elastic.co/logstash/logstash:7.14.0
docker run -d -p 5601:5601 --link elasticsearch:elasticsearch --name kibana docker.elastic.co/kibana/kibana:7.14.0