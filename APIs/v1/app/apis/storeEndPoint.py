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
        return None, {
            'status': 'error',
            'message': 'Bad request, no user token'
            }, 400

    provider = Provider.query.filter_by(email=currentUserEmail).first()

    if not provider:
        return None, {
            'status': 'error',
            'message': 'Provider not found'
            }, 404

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

    try:

        store_name = request.form.get('store_name')
        store_location = request.form.get('store_location')
        store_email = request.form.get('store_email')
        store_phone_number = request.form.get('store_phone_number')
        operation_times = request.form.get('operation_times')
        social_media_accounts = request.form.get('social_media_accounts')
        store_bio = request.form.get('store_bio')

        if not store_name or not store_location or not store_email or not store_phone_number:
            return jsonify({
                'status': 'error',
                'message': 'Missing required fields'
                }), 400

        inner_image = request.files.get('inner_image')
        outer_image = request.files.get('outer_image')

        if inner_image:
            inner_image_filename, inner_image_path = saveProfilePicture(inner_image, (600, 600), 'static/store_pics')
        else:
            inner_image_filename = None

        if outer_image:
            outer_image_filename, outer_image_path = saveProfilePicture(outer_image, (600, 600), 'static/store_pics')
        else:
            outer_image_filename = None

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

        db.session.add(new_store)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'message': 'Store successfully created!',
            'data': new_store.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        print(f"Error occurred during store creation: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'An error occurred while creating the store: {}'.format(str(e))
            }), 500


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
        return jsonify({
            'status': 'error',
            'message': 'Store not found or you are not authorized to update this store'
            }), 404

    if request.form.get("store_name"):
        store.store_name = request.form.get("store_name")
    if request.form.get("store_location"):
        store.store_location = request.form.get("store_location")
    if request.form.get("store_email"):
        store.store_email = request.form.get("store_email")
    if request.form.get("store_phone_number"):
        store.store_phone_number = request.form.get("store_phone_number")
    if request.form.get("operation_times"):
        store.operation_times = request.form.get("operation_times")
    if request.form.get("social_media_accounts"):
        store.social_media_accounts = request.form.get("social_media_accounts")
    if request.form.get("store_bio"):
        store.store_bio = request.form.get("store_bio")

    inner_image = request.files.get('inner_image')
    outer_image = request.files.get('outer_image')

    if inner_image:
        inner_image_filename, inner_image_path = saveProfilePicture(inner_image, (600, 600), 'static/store_pics')
        store.inner_image = inner_image_filename
    if outer_image:
        outer_image_filename, outer_image_path = saveProfilePicture(outer_image, (600, 600), 'static/store_pics')
        store.outer_image = outer_image_filename

    try:
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': 'Store updated successfully!',
            'data': store.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': 'An error occurred while updating the store.'
            }), 500


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
        return jsonify({
                'status': 'error',
                'message': 'Store not found or you are not authorized to delete this store'
            }), 404

    try:
        db.session.delete(store)
        db.session.commit()
        return jsonify({
                'status': 'success',
                'message': 'Store deleted successfully'
            }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
                'status': 'error',
                'message': 'An error occurred while deleting the store.'
            }), 500


@store.route('/stores', methods=['GET'])
@limiter.limit("5 per minute")
@swag_from(getAllStoresDoc)
def getAllStores():
    stores = Store.query.all()
    if not stores:
        return jsonify({
                'status': 'error',
                'message': 'No stores found'
            }), 404
    storeList = []
    for store in stores:
        storeData = store.to_dict()
        storeData['products'] = [product.to_dect() for product in store.products]
        storeList.append(storeData)

    return jsonify({
            'status': 'success',
            'message': 'All stores in the database',
            'stores': storeList
        }), 200



@store.route('/stores-with-out-product', methods=['GET'])
@limiter.limit("5 per minute")
@swag_from(getStoresDoc)
def getAllStores2():
    stores = Store.query.all()
    
    if not stores:
        return jsonify({
            'status': 'error',
            'message': 'No stores found'
        }), 404
    
    store_list = []
    for store in stores:
        storeOwner = Provider.query.filter_by(id=store.provider_id).first()
        storeOwnerName = storeOwner.username
        store_data = {
            'id': store.store_id,
            'owner': storeOwnerName,
            'phoneNumber': store.store_phone_number,
            'email': store.store_email,
            'storeName': store.store_name,
            'outer_image': store.outer_image_url,
            'inner_image': store.inner_image_url
        }
        store_list.append(store_data)

    return jsonify({
        'status': 'success',
        'message': 'Stores successfully retrieved',
        'stores': store_list
    }), 200
