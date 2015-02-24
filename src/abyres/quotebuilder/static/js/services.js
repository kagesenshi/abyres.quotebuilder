(function () {
    var Service = angular.module('quotebuilderServices', ['ngResource']);

    Service.factory('CRUDClient', ['$resource',
            function ($resource) {
                return function (collectionId) {
                        var base_url = '/' + collectionId + '/';
                        return $resource(base_url + ':objectId', {}, {
                            query: {
                                method: 'GET',
                                params: {objectId: ''},
                                isArray: true
                            }
                        })
                }
            }
    ])
})();
