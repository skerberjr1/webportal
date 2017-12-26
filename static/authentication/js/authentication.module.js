(function () {
    'use strict';

    angular
        .module('webportal.authentication', [
            'webportal.authentication.controllers',
            'webportal.authentication.services'
        ]);

    angular
        .module('webportal.authentication.controllers', []);

    angular
        .module('webportal.authentication.services', ['ngCookies']);
})();