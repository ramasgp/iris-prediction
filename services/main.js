document.getElementById('prediction-form').addEventListener('submit', function (event) {
    event.preventDefault();

    let sl = document.getElementById('sl').value;
    let sw = document.getElementById('sw').value;
    let pl = document.getElementById('pl').value;
    let pw = document.getElementById('pw').value;

    const data = {
        sl: sl,
        sw: sw,
        pl: pl,
        pw: pw
    };

    PredictAPI.predict(data)
        .then(response => {
            if (response.status === 'SUCCESS') {
                document.getElementById('prediction-result').textContent = response.data.result;
            } else {
                document.getElementById('prediction-result').textContent = response.message;
            }
        })
        .catch(error => {
            document.getElementById('prediction-result').textContent = 'Error: ' + error;
        });
});
