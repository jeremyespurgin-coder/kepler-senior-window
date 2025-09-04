import logging
import azure.functions as func
import os
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Serving photo list.')

    try:
        photo_dir = os.path.join(os.getcwd(), 'uploaded_photos')
        if not os.path.exists(photo_dir):
            return func.HttpResponse(json.dumps([]), mimetype="application/json")

        photos = []
        for filename in os.listdir(photo_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                photos.append(f"/uploaded_photos/{filename}")

        return func.HttpResponse(json.dumps(photos), mimetype="application/json")

    except Exception as e:
        logging.error(f"Error retrieving photos: {e}")
        return func.HttpResponse("Error retrieving photos.", status_code=500)