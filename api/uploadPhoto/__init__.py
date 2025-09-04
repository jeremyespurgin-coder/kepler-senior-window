import logging
import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing photo upload.')

    try:
        photo = req.files.get('photo')
        if not photo:
            return func.HttpResponse("No photo uploaded.", status_code=400)

        save_path = os.path.join(os.getcwd(), 'uploaded_photos')
        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, photo.filename)
        with open(file_path, 'wb') as f:
            f.write(photo.stream.read())

        return func.HttpResponse(f"Photo uploaded successfully: {photo.filename}", status_code=200)

    except Exception as e:
        logging.error(f"Error uploading photo: {e}")
        return func.HttpResponse("Error uploading photo.", status_code=500)