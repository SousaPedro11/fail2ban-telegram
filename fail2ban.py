from app import create_app, event_db
from app.event.models import Log, IPAddress, infos
# load_dotenv(os.path.join(basedir, '.env'))

app = create_app()


@app.shell_context_processor
def shell_context():
    return dict(
        app=app,
        db=event_db,
        Log=Log,
        IP=IPAddress,
        Info=infos,
    )


if __name__ == '__main__':
    app.run()
