def format_photos(photos):
    """Formata as fotos para mostrar no app Dash."""
    return [
        {"img_src": photo['img_src'], "earth_date": photo['earth_date']}
        for photo in photos
    ]
