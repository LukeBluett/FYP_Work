#!/usr/bin/env python3

import docker
from docker import client

import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

import pymongo
from pymongo import MongoClient

import datetime

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ()

docker_client = docker.Client(base_url='unix://var/run/docker.sock')
server = SimpleXMLRPCServer(('localhost', 8003), requestHandler=RequestHandler, allow_none=True)
mongo_client = MongoClient()

def start_container(container, user):
    mongo_add(user, container, "Started")
    docker_client.start(container)

def stop_container(container, user):
    mongo_add(user, container, "Stopped")
    docker_client.stop(container)

def pull_container(container, user):
    mongo_add(user, container, "Stopped")
    docker_client.pull(container)

def register_all_functions():
    server.register_function(start_container, "start_container")
    server.register_function(stop_container, "stop_container")
    server.register_function(pull_container, "pull_container")

def mongo_add(user, container, action):
    container_info = {"User": user, "Container": container, "Action": action, "Datetime": datetime.datetime.utcnow()}
    container_collection = db.container_collection
    container_id = container_collection.insert_one(container_info).inserted_id

if __name__ == "__main__":
    mongo_client = MongoClient('0.0.0.0', 32770)
    db = mongo_client.container_database
    collection = db.container_collection

    register_all_functions()
    print('Server')
    try:
        print('on')
        server.serve_forever()
    except Exception:
        print('off:', Exception)


