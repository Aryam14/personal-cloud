# personal-cloud
Project to store data on the personal server set up by the user.
flask --app src init-db
flask --app src run

unix:cloud.sock -m 007 "src:create_app()"

nginx conf user is current user (to give persmission)
