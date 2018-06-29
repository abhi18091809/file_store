var fileStoreApp = angular.controller('fileStoreApp', ['$scope','service', function($scope,service){

    $scope.fileUpload = function() {
        var file = $scope.fileToUpload;
        var uploadUrl = '/upload';
        service.uploadFileToUrl(file, uploadUrl);
    };
}]);