from .application import celery, mail
from .config import Config
from flask import render_template
from flask_mail import Message
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess


@celery.task
def producePoster(email, data):
    with TemporaryDirectory() as tmp:
        poster = render_template('poster/uoe.svg', **data)
        outsvg = Path(tmp, 'poster.svg')
        outpdf = outsvg.with_suffix('.pdf')
        with open(outsvg, "w") as f:
            f.write(poster)
        subprocess.run(f"inkscape -A {outpdf} {outsvg}", shell=True)

        msg = Message('poster generated', sender=Config.ADMIN,
                      recipients=[email])
        msg.body = render_template('email/poster_complete.txt')
        msg.html = render_template('email/poster_complete.html')
        with open(outpdf, 'rb') as pdf:
            msg.attach("poster.pdf", "application/pdf", pdf.read())
        mail.send(msg)
