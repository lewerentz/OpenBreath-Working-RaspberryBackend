(function () {
    var host = "http://192.168.1.31:5000";
    var configUrl = host + '/config';

    window.RestClient = {
        getConfig: function (cb) {
            var xhr = new XMLHttpRequest();

            xhr.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    cb(JSON.parse(this.responseText))
                }
            };

            xhr.open("GET", configUrl, true);
            xhr.send();
        },
        postConfig: function (data, cb) {
            var xhr = new XMLHttpRequest();

            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    cb(JSON.parse(this.responseText))
                }
            };

            xhr.open("POST", configUrl, true);
            xhr.setRequestHeader("Content-type", "application/json");
            xhr.send(JSON.stringify(data));
        }
    };
})();
