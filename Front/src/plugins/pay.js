export default class Pay {
    constructor(akbSeconds, hydrogenSeconds) {
        this.hydrogenTariff = 5;
        this.akbTariff = 7;
        this.akbSeconds = akbSeconds;
        this.hydrogenSeconds = hydrogenSeconds;
        this.seconds = akbSeconds + hydrogenSeconds;
    }

    get workTime() {
        let hours = parseInt(this.seconds / 3600);
        let minutes = parseInt(this.seconds / 60);
        let seconds = this.seconds % 60;

        if (hours < 10) hours = "0" + hours;

        if (minutes < 10) minutes = "0" + minutes;

        if (seconds < 10) seconds = "0" + seconds;

        return `${hours}:${minutes}:${seconds}`;
    }

    get sum() {
        return (
            this.akbSeconds * this.akbTariff +
            this.hydrogenSeconds * this.hydrogenTariff
        );
    }
}