from flask_openapi3 import OpenAPI
from routes.projeto_routes import projeto_bp
from routes.template_routes import template_bp
from routes.dashboard_routes import dashboard_bp
from flask_cors import CORS
import traceback


def create_app():
    app = OpenAPI(__name__, info={"title": "Lancer Free API", "version": "1.0.0"})

    app.register_api(projeto_bp)
    app.register_api(template_bp)
    app.register_api(dashboard_bp)

    @app.errorhandler(404)
    def page_not_found(error):
        return {"error": "This page does not exist"}, 404

    @app.errorhandler(Exception)
    def _all_exception_handler(error):
        res = {"error": str(error)}
        print(traceback.format_exc())
        return res, 500

    CORS(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=8000)
