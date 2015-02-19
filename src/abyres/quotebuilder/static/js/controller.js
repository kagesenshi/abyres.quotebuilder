(function () {
    var App = angular.module('quotebuilderControllers', ['ngResource', 'quotebuilderServices']);

    App.controller('ProductListCtrl', ['$scope', 'Product', function ($scope, Product) {
        $scope.products = Product.query();
    }]);

    App.controller('ProductDetailCtrl', ['$scope', '$routeParams', 'Product', 
            function ($scope, $routeParams, Product) {
                $scope.product = Product.get({productId: $routeParams.productId});
            }
    ]);
})();
