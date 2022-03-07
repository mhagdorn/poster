#!/bin/bash

export FLASK_APP=poster
export POSTER_ADMIN=poster@poster.org

flask run --cert=adhoc
