# main app that runs the flask instance imported from the init file

from web_dynamic import create_app
app = create_app()


if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=5000, debug=True)
