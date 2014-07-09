var FFClub = angular.module('FFClub', ['ui.bootstrap']);


FFClub.controller('FFClub', function($scope, $http) {

  $http.get('data/FF_Day1.json').success(function(data) {
    $scope.clubs = data;
  });

});