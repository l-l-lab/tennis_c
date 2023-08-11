
let score = { "player1": 0, "player2": 0 };

function updateScore(player) {
    // For simplicity in this example, we'll just update the score locally
    // In a real-world scenario, you would send a request to the backend server to update and fetch the score

    score[player] += 1;
    document.getElementById("score").innerText = `${score["player1"]} - ${score["player2"]}`;
}
