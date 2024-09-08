from community_app import create_app
from community_app.models.questions import Questions
from community_app.models.responses import Responses

if __name__ == '__main__':
    app = create_app()
    app.run()
