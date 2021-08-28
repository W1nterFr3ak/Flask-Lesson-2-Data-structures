from sqlite3 import Connection as SQLite3Connection
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import Engine
from datetime import datetime
from sqlalchemy import event
import linked_list
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(app.root_path, 'datas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
now = datetime.now()

# configure sqlite3 to enforce foreign key constrain
@event.listens_for(Engine, 'connect')
def __set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()



class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost")

    def __repr__(self) -> str:
        return f"{self.name}"


class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(500))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f"{self.title}"


#routes

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        name = data['name'],
        email = data['email'],
        address = data['address'],
        phone = data['phone'],
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message':'user created'}), 200


@app.route('/user/ascending_id', methods=['GET'])
def get_all_users_ascending():
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()

    for user in users:
        all_users_ll.insert_end(
            {
                "id":user.id,
                "name":user.name,
                "email":user.email,
                "address":user.address,
                "phone":user.phone, 
            }
        )

    return jsonify(all_users_ll.to_list()), 200

@app.route('/user/descending_id', methods=['GET'])
def get_all_users_descending():
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()

    for user in users:
        all_users_ll.insert_begining(
            {
                "id":user.id,
                "name":user.name,
                "email":user.email,
                "address":user.address,
                "phone":user.phone,
            }
    )

    return jsonify(all_users_ll.to_list()), 200


@app.route('/user/<user_id>', methods=['POST'])
def get_user_id(user_id):
    pass

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    pass


@app.route('/blog_post/<user_id>', methods=['POST'])
def create_blog_post(user_id):
    pass

@app.route('/user/<user_id>', methods=['GET'])
def get_all_blog_post(user_id):
    pass

@app.route('/blog_post/<blog_post_id>', methods=['GET'])
def get_one_blog_post(user_id):
    pass 

@app.route('/blog_post/<blog_post_id>', methods=['DELETE'])
def delete_blog_post(user_id):
    pass



if __name__ == "__main__":
    app.run(debug=True)