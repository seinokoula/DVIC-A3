const getBtn = document.getElementById('get');

const player_score = document.getElementById('player_score');
const best_score = document.getElementById('best_score');

const url = 'http://localhost:3000';

getBtn.addEventListener('click', postData)
async function postData(e) {
    e.preventDefault();
    axios.get(url)
        .then(function (response) {
            console.log(response.data.score[2]);

            // Get the last player's score (biggest id)
            const ids = response.data.score.map(object => {
                return object.id;
            });
            const max_id = Math.max(...ids);
            const obj_id = response.data.score.find(element => element.id === max_id);
            player_score.innerHTML = obj_id.value;


            // Get the bast player's score (biggest value)
            const values = response.data.score.map(object => {
                return object.value;
            });
            const max_value = Math.max(...values);
            const obj_value = response.data.score.find(element => element.value === max_value);
            best_score.innerHTML = obj_value.value;

            console.log(response);
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
    /*
    const res = await fetch(url, { method: 'GET' })
    console.log(res)
    const data = await res.json()

    // Get the last player's score (biggest id)
    const ids = data.scores.map(object => {
        return object.id;
    });
    const max_id = Math.max(...ids);
    const obj_id = data.scores.find(element => element.id === max_id);
    player_score.innerHTML = obj_id.value;

    // Get the bast player's score (biggest value)
    const values = data.scores.map(object => {
        return object.value;
    });
    const max_value = Math.max(...values);
    const obj_value = data.scores.find(element => element.value === max_value);
    best_score.innerHTML = obj_value.value;
    */
}