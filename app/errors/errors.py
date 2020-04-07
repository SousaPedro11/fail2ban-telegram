import json

from app.errors import errors_bp


@errors_bp.app_errorhandler(401)
@errors_bp.app_errorhandler(500)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

# app.register_error_handler(InternalServerError, handle_exception)
