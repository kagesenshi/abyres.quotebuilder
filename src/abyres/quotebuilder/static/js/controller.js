(function () {
    var App = angular.module('quotebuilderControllers', ['ngResource', 'quotebuilderServices']);

    App.controller('CRUDListCtrl', ['$scope', '$routeParams', 'CRUDClient', 
            function ($scope, $routeParams, CRUDClient) {
                $scope.objects = CRUDClient($routeParams.collectionId).query();
            }
    ]);

    App.controller('CRUDDetailCtrl', ['$scope', '$routeParams', 'Product', 
            function ($scope, $routeParams, CRUDClient) {
                $scope.object = CRUDClient($routeParams.collectionId).get({objectId: $routeParams.objectId});
            }
    ]);
})();
