from flask import Flask, jsonify, render_template
import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client['tran']
transaction = db['transaction']

app = Flask(__name__)


@app.route('/show/<string:period>/<string:unit>')
def show_transaction(period, unit):
    global result
    multiplier = 1
    if unit == 'toman':
        multiplier = 0.1
    if period == 'daily':
        pipeline = [
            {
                "$project": {
                    "year": {"$year": "$createdAt"},
                    "month": {"$month": "$createdAt"},
                    "day": {"$dayOfMonth": "$createdAt"},
                    "amount": 1,
                }
            },
            {"$group": {"_id": {"year": "$year", "month": "$month", "day": "$day"},
                        "total": {"$sum": {'$multiply': ['$amount', multiplier]}}}},
            {"$sort": {"_id": 1}}
        ]
        result = transaction.aggregate(
            pipeline
        )
    elif period == 'monthly':
        pipeline = [
            {
                "$project": {
                    "year": {"$year": "$createdAt"},
                    "month": {"$month": "$createdAt"},
                    "amount": 1,
                }
            },
            {"$group": {"_id": {"year": "$year", "month": "$month"},
                        "total": {"$sum": {'$multiply': ['$amount', multiplier]}}}},
            {"$sort": {"_id": 1}}
        ]
        result = transaction.aggregate(
            pipeline
        )


    elif period == 'yearly':
        pipeline = [
            {
                "$project": {
                    "year": {"$year": "$createdAt"},
                    "amount": 1,
                }
            },
            {"$group": {"_id": {"year": "$year"}, "total": {"$sum": {'$multiply': ['$amount', multiplier]}}}},
            {"$sort": {"_id": 1}}
        ]
        result = transaction.aggregate(
            pipeline
        )
    elif period == 'weekly':
        pipeline = [
            {
                "$project": {
                    "year": {"$year": "$createdAt"},
                    "month": {"$month": "$createdAt"},
                    "week": {"$week": "$createdAt"},
                    "amount": 1,
                }
            },
            {"$group": {"_id": {"year": "$year", "month": "$month", "week": "$week"},
                        "total": {"$sum": {'$multiply': ['$amount', multiplier]}}}},
            {"$sort": {"_id": 1}}
        ]
        result = transaction.aggregate(
            pipeline
        )

    pprint(list(result)[:2])
    return str(list(result))


if __name__ == '__main__':
    app.run()
