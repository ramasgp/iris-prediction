const Path = require('path');
const PredictAPI = require('./api.js');
const Nunjucks = require('nunjucks');

const handler = {
    predict: async (request, h) => {
        try {
            const data = request.payload;

            if (!data) {
                return {
                    status: 'FAILURE',
                    message: 'Payload is empty'
                };
            }

            const predictionResult = await PredictAPI.predict(data);
            if (predictionResult.status === 'SUCCESS') {
                const renderedHtml = Nunjucks.render('index.html', {
                    prediction_result: predictionResult.data.result
                });
                return h.response(renderedHtml).type('text/html');
            } else {
                return h.response({
                    status: 'FAILURE',
                    message: predictionResult.message
                }).code(400);
            }
        } catch (error) {
            return {
                status: 'ERROR',
                message: error.message
            };
        }
    }
};

module.exports = handler;
