#!/usr/bin/env python3
import csv
import os
import random
from dataclasses import dataclass
from enum import Enum

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from numpy.core.defchararray import upper
from sqlalchemy import create_engine, Column, Integer, Text, DateTime, func
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

Base = declarative_base()
metadata = Base.metadata

engine = create_engine('sqlite:///C:/Users/drama/PycharmProjects/2022-SWP-PYTHON/rpsslDB.sqllite3')
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
Base.query = db_session.query_property()
app = Flask(__name__)
api = Api(app)


@dataclass
class Results(Base):
    __tablename__ = 'Results'
    ResultId: int
    PlayerWins: str
    CompWins: str
    Tie: str
    SPOCKChosenP: int
    STONEChosenP: int
    SCISSORSChosenP: int
    PAPERChosenP: int
    LIZARDChosenP: int
    SPOCKChosenC: int
    STONEChosenC: int
    SCISSORSChosenC: int
    PAPERChosenC: int
    LIZARDChosenC: int

    ResultId = Column(Integer, primary_key=True)
    PlayerWins = Column(Integer)
    CompWins = Column(Text)
    Tie = Column(Text)
    SPOCKChosenP = Column(Integer)
    STONEChosenP = Column(Integer)
    SCISSORSChosenP = Column(Integer)
    PAPERChosenP = Column(Integer)
    LIZARDChosenP = Column(Integer)
    SPOCKChosenC = Column(Integer)
    STONEChosenC = Column(Integer)
    SCISSORSChosenC = Column(Integer)
    PAPERChosenC = Column(Integer)
    LIZARDChosenC = Column(Integer)


class ResultsREST(Resource):
    def get(self, id):
        info = Results.query.get(id)
        return jsonify(info)

    def put(self, id):
        d = request.get_json(force=True)
        print(d)
        info = Results(ResultId=d['ResultId'], PlayerWins=d['PlayerWins'], CompWins=d['CompWins'], Tie=d['Tie'],
                       SPOCKChosenP=d['SpockChosenP'], STONEChosenP=d['StoneChosenP'],
                       SCISSORSChosenP=d['ScissorsChosenP'], PAPERChosenP=d['PaperChosenP'],
                       LIZARDChosenP=d['LizardChosenP'], SPOCKChosenC=d['SpockChosenC'], STONEChosenC=d['StoneChosenC'],
                       SCISSORSChosenC=d['ScissorsChosenC'], PAPERChosenC=d['PaperChosenC'],
                       LIZARDChosenC=d['LizardChosenC'])
        db_session.add(info)
        db_session.flush()
        return jsonify(info)

    def delete(self, id):
        info = Results.query.get(id)
        if info is None:
            return jsonify({'Message': 'Could not find your request.'})
        db_session.delete(info)
        db_session.flush()
        return jsonify({'Message:' 'Deleted %s' % id})


api.add_resource(ResultsREST, '/result/<int:id>')


@app.teardown_appcontext
def shutdown_session(exception=None):
    print("Shutdown Session")
    db_session.remove()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host="localhost", port=5000)
