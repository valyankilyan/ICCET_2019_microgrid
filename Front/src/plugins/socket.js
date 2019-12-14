class Socket {
    isConnected = false
    messageHandlers = []
    constructor(url) {
        this._url = url;
        this._init();
    }

    _init() {
        this._socket = new WebSocket(this._url);

        this._socket.onopen = () => {
            console.log("Соединение установлено.");
            this.isConnected = true;
        };

        this._socket.onclose = (event) => {
            if (event.wasClean) {
                console.log('Соединение закрыто чисто');
            } else {
                console.log('Обрыв соединения'); // например, "убит" процесс сервера
            }
            console.log('Код: ' + event.code + ' причина: ' + event.reason);
            this.isConnected = false;
        };

        this._socket.onmessage = (event) => {
            for (let messageHandle of this.messageHandlers) {
                messageHandle(event.data);
            }
            console.log("Получены данные " + event.data);
        };

        this._socket.onerror = function (error) {
            console.log("Ошибка " + error.message);
        };
    }

    send(data, tryCount) {
        if (tryCount === undefined)
            tryCount = 5;

        if (!this.isConnected && tryCount > 0) {
            console.log('соединение не работает пробуем еще разик');
            tryCount--;
            setTimeout(() => {
                this.send(data, tryCount);
            }, 1000);

            return;
        }

        if (!this.isConnected && tryCount <= 0) {
            console.log('соединение не работает больше не будет');
            return;
        }

        this._socket.send(data);
    }

    addMessageHandler(messageHandler) {
        if(typeof messageHandler != 'function')
            return;

        this.messageHandlers.push(messageHandler);
    }

    removeMessageHandler(messageHandler) {
        const index = this.messageHandlers.indexOf(messageHandler);
        if(index == -1)
            return;

        this.messageHandlers.splice(index, 1);
    }
}

function install(Vue, options) {
        var socket = new Socket(options.url);

        Vue.prototype.$socket = socket;
        console.log('update');
        return socket;
    }


export default install;