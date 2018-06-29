fileStoreApp.service('fileStoreApp',['$https', function($https){

    this.uploadFileToUrl = function(file, uploadUrl){
        var fd = new FormData();
        fd.append('file',file);

        $https:.post(uploadUrl, fd, {
            transformRequest: angular.identity,
            headers: {'Content-type': content-type}})

            .success(function(res){
                data = res.data;
            })

            .error(function(res){
                data = res.data;
            });
        }

}]);