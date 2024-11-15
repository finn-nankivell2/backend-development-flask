from app import create_app

import sqlalchemy as sa
import sqlalchemy.orm as so

init_app = create_app()

@init_app.shell_context_processor
def make_shell_context():
    return {
        "sa": sa,
        "so": so,
    }
