(function () {
    var App = angular.module('quotebuilderApp', [
            'ngRoute',
            'quotebuilderServices',
            'quotebuilderControllers',
    ]);

    App.config(['$routeProvider',
            function ($routeProvider) {

                var templatedir = $('meta[name=ngPartials]').attr('content');

                $routeProvider.when('/products', {
                    templateUrl: templatedir + 'product-list.html',
                    controller: 'ProductListCtrl'
                }).
                when('/products/:productId', {
                    templateUrl: templatedir + 'product-details.html',
                    controller: 'ProductDetailCtrl'
                }).
                otherwise({
                    redirectTo: '/products'
                })
            }
    ]);

})();
