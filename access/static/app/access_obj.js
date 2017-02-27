'use strict';

var accessApp = angular.module('accessApp', ['ngSanitize']);

angular.module('accessApp')
    .config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});


accessApp.controller("AccessController", function($scope, $location, $http, $sce, $compile) {
    $scope.itemsPage = {
        availableOptions: [
          {id: '10', name: '10'},
          {id: '25', name: '25'},
          {id: '50', name: '50'},
          {id: '100', name: '100'}
        ],
        selectedOption: {id: '10', name: '10'}
    };

    $scope.getAccessObject = function (page, search) {
        if (page){
            $scope.itemsPage.selectedOption.page = page;
        }
        if (search){
            $scope.itemsPage.selectedOption.search = search;
        }else if(search === 0){
            $scope.itemsPage.selectedOption.search = 0;
        }
        $scope.validReg = false;
        $http.post('get-access-objects', angular.toJson($scope.itemsPage.selectedOption))
        .then(function(response) {
            $scope.facilitys = response.data;
            $scope.paginator = $compile(response.data[response.data.length-1].paginator)($scope);
            angular.element(document.getElementById('paginator')).html($scope.paginator);
            $scope.validReg = false;
        })
        .catch(function(response) {
            $scope.facilitys = 0;
            $scope.validReg = true;
        });
    };

    $scope.getAccessObject();

    $http.get('get-access-users')
        .then(function(response) {
            $scope.users = response.data;
        })
        .catch(function(response) {

        });
    $scope.change = function(user_pk, obj_pk, selected){
        $scope.data = {
            user_pk: user_pk,
            obj_pk: obj_pk,
            selected: selected
        };
        $scope.desableCheck = true;
        jQuery('.messageServer').animate({backgroundColor: '#FCCD1B'}, 500);
        jQuery('.messageServer').text('Обработка').fadeIn(300).delay(100);
        $http.post('change_access_facility', angular.toJson($scope.data))
            .then(function(data) {
                var data = data.data;
                jQuery('.messageServer').animate({backgroundColor: '#5bc0de'}, 500);
                jQuery('.messageServer').text('Пользователь: '+data.user+". "+data.message+". Объект: ID "+data.id_facility).fadeIn(1000).delay(3000).fadeOut(500);
            })
            .catch(function(data, status) {
                jQuery('.messageServer').animate({backgroundColor: '#c9302c'}, 500);
                jQuery('.messageServer').text('Ошибка '+data.status+'. '+data.responseText).fadeIn(1000).delay(2000).fadeOut(500);

            })
            .finally(function() {
                $scope.desableCheck = false;
            });

    };
    $scope.changeAll = function (user_pk, selected) {
        $scope.data = {
            user_pk: user_pk,
            selected: selected,
            all: true
        };
        $scope.desableCheck = true;
        jQuery('.messageServer').animate({backgroundColor: '#FCCD1B'}, 500);
        jQuery('.messageServer').text('Обработка').fadeIn(300).delay(100);
        $http.post('change_access_facility', angular.toJson($scope.data))
            .then(function(data) {
                $scope.getAccessObject(1, 0);
                var data = data.data;
                jQuery('.messageServer').animate({backgroundColor: '#5bc0de'}, 500);
                jQuery('.messageServer').text('Пользователь: '+data.user+". "+data.message+". Объект: ID "+data.id_facility).fadeIn(1000).delay(3000).fadeOut(500);
            })
            .catch(function(data, status) {
                jQuery('.messageServer').animate({backgroundColor: '#c9302c'}, 500);
                jQuery('.messageServer').text('Ошибка '+data.status+'. '+data.responseText).fadeIn(1000).delay(2000).fadeOut(500);

            })
            .finally(function() {
                $scope.desableCheck = false;
            });
    };
    $scope.getItems = function () {
        $scope.getAccessObject();
    };
    $scope.paginate = function (page) {
        $scope.getAccessObject(page);
    };
    $scope.validSearch = false;
    $scope.searchObj = function (search) {
        var page = 1;
        $scope.getAccessObject(page, search);
    };
    $scope.cancelSearch = function () {
        $scope.search = '';
        $scope.getAccessObject(1, 0);
    }

});