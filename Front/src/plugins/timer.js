export default class Timer {
    constructor() {
        this.seconds = 0;
        this.interval = null;
    }

    start() {
        this.interval = setInterval(() => this.seconds++, 1000);
    }

    stop() {
        clearInterval(this.interval);
    }

    clear() {
        this.seconds = 0;
    }

    toString() {
        let hours = parseInt(this.seconds / 3600);
        let minutes = parseInt(this.seconds / 60);
        let seconds = this.seconds % 60;

        if (hours < 10) hours = "0" + hours;

        if (minutes < 10) minutes = "0" + minutes;

        if (seconds < 10) seconds = "0" + seconds;

        return `${hours}:${minutes}:${seconds}`;
    }
}