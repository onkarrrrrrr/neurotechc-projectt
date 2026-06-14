import os
import datetime
from pymongo import MongoClient
from pymongo.server_api import ServerApi

def get_mongo_client():
    """
    Retrieves the MongoClient configured with the environment-supplied MONGO_URI.
    Falls back to localhost if the variable is not set.
    """
    uri = os.environ.get('MONGO_URI')
    if not uri:
        uri = "mongodb://localhost:27017/"
    
    return MongoClient(uri, server_api=ServerApi('1'))

def test_mongo_connection():
    """
    Pings the MongoDB server to verify a successful connection.
    Returns (status, message).
    """
    client = get_mongo_client()
    try:
        client.admin.command('ping')
        return True, "Pinged your deployment. You successfully connected to MongoDB!"
    except Exception as e:
        return False, str(e)
    finally:
        client.close()

from bson.objectid import ObjectId

def save_appointment_to_mongodb(data):
    """
    Saves the validated appointment form data as a document in the MongoDB database collection.
    """
    client = get_mongo_client()
    try:
        db = client.get_database('neurotech')
        collection = db.get_collection('appointments')
        
        document = {
            'full_name': data.get('full_name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
            'company': data.get('company', ''),
            'service': data.get('service'),
            'message': data.get('message', ''),
            'status': 'NEW',
            'note': '',
            'created_at': datetime.datetime.utcnow()
        }
        
        result = collection.insert_one(document)
        return result.inserted_id
    finally:
        client.close()

def get_all_appointments():
    """
    Fetches all appointments sorted by created_at descending.
    """
    client = get_mongo_client()
    try:
        db = client.get_database('neurotech')
        collection = db.get_collection('appointments')
        appointments = list(collection.find().sort('created_at', -1))
        # Convert ObjectId to string for easy templating
        for appt in appointments:
            appt['id_str'] = str(appt['_id'])
        return appointments
    finally:
        client.close()

def update_appointment(appt_id, status=None, note=None):
    """
    Updates the status or note for a specific appointment document.
    """
    client = get_mongo_client()
    try:
        db = client.get_database('neurotech')
        collection = db.get_collection('appointments')
        
        update_fields = {}
        if status is not None:
            update_fields['status'] = status
        if note is not None:
            update_fields['note'] = note
            
        if update_fields:
            collection.update_one({'_id': ObjectId(appt_id)}, {'$set': update_fields})
    finally:
        client.close()

def delete_appointment(appt_id):
    """
    Deletes an appointment document from the collection by ID.
    """
    client = get_mongo_client()
    try:
        db = client.get_database('neurotech')
        collection = db.get_collection('appointments')
        collection.delete_one({'_id': ObjectId(appt_id)})
    finally:
        client.close()

def save_job_to_mongodb(data):
    """
    Saves a job document to MongoDB.
    """
    client = get_mongo_client()
    try:
        db = client.get_database('neurotech')
        collection = db.get_collection('jobs')
        
        document = {
            'job_title': data.get('job_title'),
            'description': data.get('description', ''),
            'experience_level': data.get('experience_level'),
            'employment_type': data.get('employment_type', 'FULL_TIME'),
            'location': data.get('location', ''),
            'salary_min': data.get('salary_min'),
            'salary_max': data.get('salary_max'),
            'skills_required': data.get('skills_required', ''),
            'apply_link': data.get('apply_link', 'https://www.linkedin.com/company/neurotech-circuits-private-limited/jobs/'),
            'is_active': data.get('is_active', True),
            'created_at': datetime.datetime.utcnow(),
            'updated_at': datetime.datetime.utcnow()
        }
        
        result = collection.insert_one(document)
        return result.inserted_id
    finally:
        client.close()

def get_all_jobs():
    """
    Fetches all jobs sorted by created_at descending.
    """
    client = get_mongo_client()
    try:
        db = client.get_database('neurotech')
        collection = db.get_collection('jobs')
        jobs = list(collection.find().sort('created_at', -1))
        # Convert ObjectId to string for easy templating
        for job in jobs:
            job['id_str'] = str(job['_id'])
        return jobs
    finally:
        client.close()

def update_job(job_id, **kwargs):
    """
    Updates specific fields for a job document.
    """
    client = get_mongo_client()
    try:
        db = client.get_database('neurotech')
        collection = db.get_collection('jobs')
        
        if kwargs:
            kwargs['updated_at'] = datetime.datetime.utcnow()
            collection.update_one({'_id': ObjectId(job_id)}, {'$set': kwargs})
    finally:
        client.close()

def delete_job(job_id):
    """
    Deletes a job document from the collection by ID.
    """
    client = get_mongo_client()
    try:
        db = client.get_database('neurotech')
        collection = db.get_collection('jobs')
        collection.delete_one({'_id': ObjectId(job_id)})
    finally:
        client.close()
