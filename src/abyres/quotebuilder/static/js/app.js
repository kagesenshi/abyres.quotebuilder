(function () {
    var App = angular.module('quotebuilderApp', [
            'ngRoute',
            'quotebuilderServices',
            'quotebuilderControllers',
    ]);

    App.config(['$routeProvider',
            function ($routeProvider) {

                var templatedir = $('meta[name=ngPartials]').attr('content');

                $routeProvider.when('/:collectionId', {
                    templateUrl: templatedir + 'crud-list.html',
                    controller: 'CRUDListCtrl'
                }).
                when('/:collectionId/:objectId', {
                    templateUrl: templatedir + 'crud-details.html',
                    controller: 'CRUDDetailCtrl'
                }).
                otherwise({
                    redirectTo: '/products'
                })
            }
    ]);

})();
