from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Movie import Movie
# Models
from models.MovieModel import MovieModel

main = Blueprint('movie_blueprint', __name__)


@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<ci>')
def get_movie(ci):
    try:
        movie = MovieModel.get_movie(ci)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_movie():
    try:
        nombre = request.json['nombre']
        apellido = int(request.json['apellido'])
        procedencia = request.json['procedencia']
        fechaNac = request.json['fechaNac']
        ci = uuid.uuid4()
        movie = Movie(str(ci), nombre, apellido, procedencia, fechaNac)

        affected_rows = MovieModel.add_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<ci>', methods=['PUT'])
def update_movie(ci):
    try:
        nombre = request.json['nombre']
        apellido = int(request.json['apellido'])
        procedencia = request.json['procedencia']
        fechaNac = request.json['fechaNac']
        ci = uuid.uuid4()
        movie = Movie(str(ci), nombre, apellido, procedencia, fechaNac)
        affected_rows = MovieModel.update_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "No movie updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(ci):
    try:
        movie = Movie(ci)

        affected_rows = MovieModel.delete_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "No movie deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500