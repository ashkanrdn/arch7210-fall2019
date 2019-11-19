let idGenerator = (function* () {
    const prefix = Math.random().toString(36).substring(2, 7) + '_';
    let n = 0;
    while (true) {
        yield prefix + (n++);
    }
})();

window.addEventListener('load', () => {
    let form = document.forms[0];
    let log = document.querySelector('ol');

    function appendLog(message) {
        console.log(message);
        if (typeof message === 'string') {
            try {
                message = JSON.parse(message);
            } catch (e) {
                message = {result: message, error: null};
            }
        }

        let element = document.createElement('li');

        if (message.hasOwnProperty('method')) {
            element.className = 'request';
            if (message.params) {
                let paramList = JSON.stringify(message.params);
                element.textContent = message.method + '(' + paramList.substr(1, paramList.length-2) + ')';
            } else {
                element.textContent = message.method + '()';
            }
        } else {
            element.className = 'response';
            if (message.result) {
                let resultElement = document.createElement('span');
                resultElement.className = 'result';
                resultElement.textContent = message.result;
                element.appendChild(resultElement);
            }
            if (message.error) {
                let errorElement = document.createElement('span');
                errorElement.className = 'error';
                errorElement.textContent = `(${message.error.code}) ${message.error.message}`;
                element.appendChild(errorElement);
            }
        }
        
        if (message.id) {
            element.dataset.requestId = message.id;

            element.addEventListener('mouseenter', () => {
                for (let entry of document.querySelectorAll(`li[data-request-id='${message.id}']`)) {
                    entry.classList.add('highlight');
                }
            });

            element.addEventListener('mouseleave', () => {
                for (let entry of document.querySelectorAll(`li[data-request-id='${message.id}']`)) {
                    entry.classList.remove('highlight');
                }
            });
        }

        log.appendChild(element);
        element.scrollIntoView(false);
    }
    
    let ws = new ReconnectingWebSocket(location.href.replace(/^http/, 'ws'));
    ws.addEventListener('open', () => {
        form.elements['submit'].disabled = false;
    });

    ws.addEventListener('close', () => {
        form.elements['submit'].disabled = true;
    });
    
    ws.addEventListener('message', (msg) => {
        appendLog(msg.data);
    });

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        let request = {
            method: form.elements['method'].value,
            params: JSON.parse('[' + form.elements['params'].value + ']'),
            id: idGenerator.next().value,
        };
        appendLog(request);
        ws.send(JSON.stringify(request));
        form.reset();
        form.elements[0].focus();
    });

    channelLog.forEach(appendLog);
});
