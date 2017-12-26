(function () {
    'use strict';

    angular
        .module('webportal.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    function config($routeProvider) {
        $routeProvider.when('/register', {
            controller: 'RegisterController',
            controllerAs: 'vm',
            templateUrl: '/authentication/templates/register.html'
        }).otherwise('/');
    }
})();