function restart() {
    const statusText = document.getElementById('status');
    const car = document.getElementById('car');

    statusText.innerText = "Going to begin the program";
    statusText.style.color = "black";

    car.className = ''; // Resets car position
    fetch('/change_light/off'); // Turn all LEDs off
}

function begin() {
    const statusText = document.getElementById('status');
    const car = document.getElementById('car');

    statusText.innerText = "Car is stopped at redlight";
    statusText.style.color = "red";

    car.className = 'at-stop-line'; // Move car to the line
    fetch('/change_light/red'); // Shine Red LED
}

function go() {
    const statusText = document.getElementById('status');
    const car = document.getElementById('car');

    // Immediate feedback for Yellow light
    statusText.innerText = "Preparing to move...";
    statusText.style.color = "orange";
    fetch('/change_light/yellow');

    // Wait 2 seconds for the Green light and driving action
    setTimeout(() => {
        statusText.innerText = "Car is moving";
        statusText.style.color = "green";

        fetch('/change_light/green');
        car.className = 'drive-away';
    }, 2000); // 2000ms = 2 seconds
}
