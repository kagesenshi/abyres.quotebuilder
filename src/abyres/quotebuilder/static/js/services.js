(function () {
    var Service = angular.module('quotebuilderServices', ['ngResource']);

    Service.factory('Product', ['$resource',
            function ($resource) {
                return $resource('products/:productId', {}, {
                    query: {
                        method: 'GET',
                        params: {productId: ''},
                        isArray: true
                    }
                })
            }
    ])

})();
