from __future__ import print_function
import time
import re
import json
import argparse
import sys
from kafka import KafkaProducer



def send_message(producer, topic, input):
     
     with open(input, 'r') as ins:
             for line in ins:
                     value1 = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))
                     producer.send(topic, json.dumps({'remote_host': value1[0], 'user-identifier': value1[1], 'frank': value1[2], 'time_received': value1[3],'request_first_line': value1[4],'status': value1[5],'size_bytes': value1[6],'request_header_referer': value1[7],'request_header_user_agent': value1[8]}))


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-rh', '--host', default="127.0.0.1:9092")
	parser.add_argument('-t', '--topic', default='messages')
	parser.add_argument('-i', '--input', required=True)
	args = parser.parse_args()
	
	producer = KafkaProducer(bootstrap_servers=args.host)
	send_message(producer, args.topic, args.input)