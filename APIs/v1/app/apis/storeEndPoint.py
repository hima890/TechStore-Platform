#!/usr/bin/python3
""" Store API """

from flask import request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import store
from ..models import Store, Provider
from .. import limiter, db
from ..utils import saveProfilePicture
from .swaggerFile import (createStoreDoc, updateStoreDoc,
                          deleteStoreDoc, getAllStoresDoc,
                          getStoresDoc)

def getAccount():
    """Get the authenticated provider"""
    currentUserEmail = get_jwt_identity()

    if not currentUserEmail:
        return None, {'status': 'error', 'message': 'Bad request, no user token'}, 400

    # Fetch the provider by email
    provider = Provider.query.filter_by(email=currentUserEmail).first()

    if not provider:
        return None, {'status': 'error', 'message': 'Provider not found'}, 404

    return provider, None, 200


@store.route('/create-store', methods=['POST'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(createStoreDoc)
def create_store():
    """Create a new store"""
    provider, error, status_code = getAccount()
    if error:
        return jsonify(error), status_code

    # Get store details from the JSON body instead of form
    data = request.get_json()
    store_name = data.get('store_name')
    store_location = data.get('store_location')
    store_email = data.get('store_email')
    store_phone_number = data.get('store_phone_number')
    operation_times = data.get('operation_times')
    social_media_accounts = data.get('social_media_accounts')
    store_bio = data.get('store_bio')

    # Validate required fields
    if not store_name or not store_location or not store_email or not store_phone_number:
        return jsonify({'error': 'Missing required fields'}), 400

    # If handling images, they would still come from request.files (not from JSON)
    inner_image = request.files.get('inner_image')
    outer_image = request.files.get('outer_image')

    inner_image_filename = None
    outer_image_filename = None

    if inner_image:
        inner_image_filename, inner_image_path = saveProfilePicture(inner_image, 'inner')
    if outer_image:
        outer_image_filename, outer_image_path = saveProfilePicture(outer_image, 'outer')

    new_store = Store(
        provider_id=provider.id,
        store_name=store_name,
        store_location=store_location,
        store_email=store_email,
        store_phone_number=store_phone_number,
        operation_times=operation_times,
        social_media_accounts=social_media_accounts,
        store_bio=store_bio,
        inner_image=inner_image_filename,
        outer_image=outer_image_filename
    )

    try:
        db.session.add(new_store)
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': 'Store successfully created!',
            'data': new_store.to_dect()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while creating the store.'}), 500


@store.route('/update-store/<int:store_id>', methods=['PUT'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(updateStoreDoc)
def update_store(store_id):
    """Update store information"""
    provider, error, status_code = getAccount()
    if error:
        return jsonify(error), status_code

    store = Store.query.filter_by(store_id=store_id, provider_id=provider.id).first()
    if not store:
        return jsonify({'error': 'Store not found or you are not authorized to update this store'}), 404

    # Get data from JSON
    data = request.get_json()
    if data.get("store_name"):
        store.store_name = data.get("store_name")
    if data.get("store_location"):
        store.store_location = data.get("store_location")
    if data.get("store_email"):
        store.store_email = data.get("store_email")
    if data.get("store_phone_number"):
        store.store_phone_number = data.get("store_phone_number")
    if data.get("operation_times"):
        store.operation_times = data.get("operation_times")
    if data.get("social_media_accounts"):
        store.social_media_accounts = data.get("social_media_accounts")
    if data.get("store_bio"):
        store.store_bio = data.get("store_bio")

    # Image handling can still be done using request.files
    inner_image = request.files.get('inner_image')
    outer_image = request.files.get('outer_image')

    if inner_image:
        inner_image_filename, inner_image_path = saveProfilePicture(inner_image, 'inner')
        store.inner_image = inner_image_filename
    if outer_image:
        outer_image_filename, outer_image_path = saveProfilePicture(outer_image, 'outer')
        store.outer_image = outer_image_filename

    try:
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': 'Store updated successfully!',
            'data': store.to_dect()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while updating the store.'}), 500


@store.route('/delete-store/<int:store_id>', methods=['DELETE'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(deleteStoreDoc)
def delete_store(store_id):
    """Delete a store by its ID"""
    provider, error, status_code = getAccount()
    if error:
        return jsonify(error), status_code

    store = Store.query.filter_by(store_id=store_id, provider_id=provider.id).first()

    if not store:
        return jsonify( 
            {
                'status': 'error',
                'message': 'Store not found or you are not authorized to delete this store'
            }
            ), 404

    try:
        db.session.delete(store)
        db.session.commit()
        return jsonify(
            {
                'status': 'success',
                'message': 'Store deleted successfully'
            }
            ), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                'status': 'error',
                'message': 'An error occurred while deleting the store.'}
            ), 500


@store.route('/stores', methods=['GET'])
@limiter.limit("5 per minute")
@swag_from(getAllStoresDoc)
def getAllStores():
    # Query to get all stores from the database
    stores = Store.query.all()
    # Check of the there is stores
    if not stores:
        return jsonify( 
            {
                'status': 'error',
                'message': 'No stores found'
            }
            ), 404
    # Prepare the list of stores with their products
    storeList = []
    for store in stores:
        storeData = store.to_dect()
        # Add the products of the store to the response
        storeData['products'] = [product.to_dect() for product in store.products]
        storeList.append(storeData)

    # Return the list of stores and their products as a JSON response
    return jsonify(
        {
            'status': 'success',
            'message': 'All stores in the database',
            'stores': storeList
        }
        ), 200



@store.route('/stores-with-out-product', methods=['GET'])
@limiter.limit("5 per minute")
@swag_from(getStoresDoc)
def getAllStores2():
    # Query to get all stores from the database
    stores = Store.query.all()
    
    # Check if there are stores
    if not stores:
        return jsonify({
            'status': 'error',
            'message': 'No stores found'
        }), 404
    
    # Prepare the list of stores
    store_list = []
    for store in stores:
        store_data = {
            'id': store.id,
            'owner': store.owner,
            'phoneNumber': store.phoneNumber,
            'email': store.email,
            'storeName': store.storeName,
            'outer_image': store.outer_image,
            'inner_image': store.inner_image
        }
        store_list.append(store_data)
    
    # Return the list of stores as a JSON response
    return jsonify({
        'status': 'success',
        'message': 'Stores successfully retrieved',
        'stores': store_list
    }), 200
