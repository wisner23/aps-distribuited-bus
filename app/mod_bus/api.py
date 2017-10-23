from flask import Blueprint

mod_bus = Blueprint("mod_bus", __name__, url_prefix="/bus")


@mod_bus.route("", methods=["GET"])
def get_bus():
    return ["test"]