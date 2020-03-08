angular.module('zapyle')
    .controller('UploadCtrl', function($scope,$http,$localStorage) {
        $scope.user_type = $localStorage.user_type;
        $scope.img_id = 1;
        $scope.new_img=1;
        $scope.images_selected=[]
        $scope.cropper = {};
        //$scope.custom_cropper = [1, 0, 0]
        $scope.cropper.sourceImage = null;
        $scope.cropper.croppedImage   = null;
        $scope.bounds = {};
        $scope.bounds.left = 50;
        $scope.bounds.right = 50;
        $scope.bounds.top = 50;
        $scope.bounds.bottom = 50;
        $scope.age = [{'id':0, 'name':'0-3 months'},
                        {'id':1,'name':'3-6 months'},
                        {'id':2,'name':'6-12 months'},
                        {'id':3,'name':'1-2 years'}];
        $scope.conditions=[{'id':0,'name':'New with tags'},
                        {'id':1,'name':'Mint Condition'},
                        {'id':2,'name':'Gently loved'},
                        {'id':3,'name':'Worn out'}];
        $scope.free_size=1   
        $scope.addresses = []    
        $scope.size_selected = [{}]  
    $scope.addChoice = function(){
        $scope.size_selected.push({})
    }    
    $scope.removeChoice = function(item){
        $scope.size_selected.shift(item)
    }
    $scope.add_visible_crop=function (id) {
        $('.crop-image').addClass('is_visible');
    
    }
    $scope.get_brands = function(search_word){
            $http({
                method: 'GET',
                url: "/getbrand/?q="+search_word,
            }).then(function successCallback(response) {
                $scope.brands = response.data
                // $scope.brands.unshift({'brand':'--Select Brand--','id':'00000'})
                $scope.brand_selected = $scope.brands[0]
            }, function errorCallback(response) {
                console.log(response);
            });        
    }
    $scope.get_addresses = function(){
            $http({
                method: 'GET',
                url: "/address/crud/",
            }).then(function successCallback(response) {
                console.log(response)
                $scope.addresses=response.data.data
            }, function errorCallback(response) {
                console.log(response);
            });        
    }
    $scope.get_styles = function(search_word){
            $http({
                method: 'GET',
                url: "/getfashion/",
            }).then(function successCallback(response) {
                $scope.styles = response.data
                // $scope.styles.unshift({'brand':'--Select Brand--','id':'00000'})
                $scope.style_selected = $scope.styles[0]
            }, function errorCallback(response) {
                console.log(response);
            });        
    }
    var UploadStart = Date.now()
    $scope.get_upload_details = function(search_word){
            $http({
                method: 'GET',
                url: "/catalogue/crud/",
            }).then(function successCallback(response) {
                $scope.cat=response.data.data['category']
                $scope.sub_cat = response.data.data['sub_category']
                $scope.sub_categories_temp=response.data.data['sub_category']
                $scope.colors = response.data.data['color']
                $scope.occasions = response.data.data['occasion']
                $scope.styles = response.data.data['fashion_types']
                $scope.states = response.data.data['states']
                console.log($scope.sub_categories+'=====')
                console.log(response.data.data);
                $scope.brands = response.data.data['brands']
                //$scope.brand_selected = $scope.brands[0]
                $scope.categories = response.data.data['category']
                $scope.sub_categories = response.data.data['sub_category']
                $scope.size_list = response.data.data.global_product_list
            }, function errorCallback(response) {
                console.log(response.data.category);
            });        
    }
    $scope.account_num_edit = 1
    $scope.get_account_number = function(search_word){
            $http({
                method: 'GET',
                url: "/user/accountnumber/",
            }).then(function successCallback(response) {
                $scope.account_num = response.data.user_acc
                $scope.confirm_account_num = response.data.user_acc
                $scope.ifsc_code = response.data.ifsc_code
                $scope.account_holder = response.data.account_holder
                if($scope.account_num && $scope.ifsc_code){
                    $scope.account_num_edit = 0
                }
            }, function errorCallback(response) {
                console.log(response.data.category);
            });        
    }
    $scope.get_account_number()
    // $scope.get_brands("")
    // $scope.get_styles()
    $scope.get_upload_details()
    $scope.get_addresses()
    $scope.set_brand = function(){
        console.log($scope.brand_selected)
        $scope.search_word=($scope.brand_selected && $scope.brand_selected) || ""
    }
    $scope.hide_crop=function() {
        $('.crop-image').removeClass('is_visible');
            $scope.images_selected.push({'id':$scope.img_id,'img_url':$scope.cropper.croppedImage})
            $scope.img_id=$scope.img_id+1;
            if ($scope.images_selected.length==6){
                $scope.new_img=0;
            }
            $scope.img1=$scope.cropper.croppedImage;
            $scope.cropper.croppedImage=null
    }
    $scope.cancel_crop = function(){
        $('.crop-image').removeClass('is_visible');
    }
    $scope.remove_img=function(id){
        for(var i=0;i<$scope.images_selected.length;i++){
            if($scope.images_selected[i].id==id){
                $scope.images_selected.splice(i,1)
            }
        }
        $scope.new_img=1;
    }
    $scope.post_account_num = function(){
        if($scope.account_num && $scope.ifsc_code  && $scope.account_num == $scope.confirm_account_num)
        {
            $http({
                method: 'POST',
                url: "user/accountnumber/",
                data: {
                    'account_number': $scope.account_num,
                    'ifsc_code': $scope.ifsc_code,
                    'account_holder': $scope.account_holder
                }
            }).then(function successCallback(response) {
                if(response.data.status == 'success'){
                    $scope.account_num_edit = 0
                }else{
                    alert(JSON.stringify(response.data.detail))                    
                }
            }, function errorCallback(response) {
                console.log(response.data.category);
            }); 
        }
    }
    $scope.product_type = '2'
    $scope.size_selected = [{}]
    $scope.submit=function(){
        if($scope.images_selected.length==0){
            alert("Select atleast one image")
            return false;
        }
        if($scope.product_type == 2){
            if($('.address-card.is_selected').length==0){
                alert("Select Pickup address")
                return false;
            }
            if (!($scope.account_num == $scope.confirm_account_num)){
                alert("Account number and confirm accout number does not match")
            }
            if ($scope.account_num_edit){
                alert('create a bank account')
                return false;
            }
            var server_data={
                    'pickup_address': $('.address-card.is_selected').attr('select-card'),
                    'images': $scope.images_selected,
                    'title': $scope.product_title,
                    'description': $scope.product_description,
                    'style': $scope.style_selected,
                    'brand': $scope.brand_selected.id,
                    'original_price':Math.round($scope.original_price),
                    'listing_price': Math.round($scope.listing_price),
                    'occasion': $scope.occasion_selected,
                    'sale': $scope.product_type,
                    'product_category': $scope.sub_cat_selected,
                    'color': $scope.color_selected,
                    'age': $scope.age_selected['id'],
                    'condition': $scope.condition['id'],
                    'discount': $scope.discount,
                    'free_quantity':$scope.free_quantity,
                    'size_type':$scope.size_selected[0].size_type

                }
        }else{
            var server_data={
                    'pickup_address': $('.address-card.is_selected').attr('select-card'),
                    'images': $scope.images_selected,
                    'title': $scope.product_title,
                    'description': $scope.product_description,
                    'style': $scope.style_selected,
                    'brand': $scope.brand_selected.id,
                    'occasion': $scope.occasion_selected,
                    'sale': $scope.product_type,
                    'product_category': $scope.sub_cat_selected,
                    'color': $scope.color_selected,
                    'free_quantity':$scope.free_quantity,
                    'size_type':$scope.size_selected[0].size_type

                }
        }
        // alert('go')
        // return false;
        $("#addProduct").val("Please Wait...").attr('disabled', 'disabled');
        
        if($scope.free_size==false){
            // for (var i=0;i<$scope.size_selected.length;i++){

            // }
            server_data['global_size'] = $scope.size_selected
        }else{
            server_data['global_size'] = 'Free Size'
        }
        console.log(server_data)
        $http({
                method: 'POST',
                url: "/catalogue/crud/",
                data:server_data
            }).error(function(error){console.log(error)
                $("#addProduct").val("Upload").prop('disabled', false);
            }).then(function successCallback(response) {
                console.log(response)  
                if(response.data.status == 'success'){      
                    swal("Success!", "Product Uploaded Successfully!", "success")
                    $("#addProduct").val("Upload").prop('disabled', false);
                    $scope.images_selected = []
                    $scope.product_title = ''
                    $scope.product_description = ''
                    $scope.search_word.brand = ''
                    mixpanel.track("User Event", {'Event Name': 'Upload Start','Start Time': UploadStart});
                    var delta = Math.abs(Date.now() - UploadStart) / 1000;
                    var minutes = Math.floor(delta / 60) % 60;
                    delta -= minutes * 60;
                    var seconds = delta % 60; 
                    mixpanel.track("User Event", {'Event Name': 'Upload Complete','Complete Time': Date.now(), 'Time taken to Upload':minutes+' minutes '+seconds+' seconds'});
                    UploadStart = Date.now()
                }else{
                    alert("Something went wrong")
                    $("#addProduct").val("Upload").prop('disabled', false);
                }
                },
                function errorCallback(response) {
                 });
    
    }
    $scope.cat_change=function(){
        $scope.free_size=false
        if($scope.sub_cat_selected==undefined){
            $scope.free_size=true
            return true
        }
        // else if($scope.category.category_type == "FS"){
        //     $scope.free_size=true
        // }else{
        //     $scope.free_size=false
        // }

        var sub_new=[]
        for(var i=0;i<$scope.sub_categories.length;i++){

            if($scope.sub_categories[i].parent['name']==$scope.category){
                sub_new.push($scope.sub_categories[i])
            }
        }

        for(i in $scope.sub_cat){
            if($scope.sub_cat[i].id == $scope.sub_cat_selected){
                if($scope.sub_cat[i].parent.category_type == "FS"){
                    $scope.free_size=true
                }
            }
        }
        $scope.sub_categories_temp=sub_new
        $scope.sizes = []
        $scope.size_type_list=[]
        // $scope.free_size=true
        // for(var j=0;j<$scope.size_list.length;j++){
        //     if(($scope.size_list[j]['category_type']==$scope.category['category_type']) && !($scope.size_list[j]['size_type'] == "FS")){
        //         $scope.free_size=false
        //     }
        // }
        
    }
    $scope.size_type_change = function(size_type){
        $scope.sizes = $scope.size_list.filter(function(i){if((i.size_type==size_type) && (i.category==$scope.category)){return true}})
        alert($scope.sizes)
    }
    $scope.deleteAddress=function(id){
        $http({
                method: 'DELETE',
                url: "/address/crud/?address_id="+id,
                data:
                {'address_id':id}
            }).error(function(response) {
                console.log(response)
            }).then(function successCallback(response) {
                if(response.data.data){
                    for(var i=0;i<$scope.addresses.length;i++){
                    if($scope.addresses[i]['id']==id){
                        $scope.addresses.splice(i,1)
                    }
                }
            }
         });
    }
    
    $scope.save_address=function(){
        $http({
                method: 'POST',
                url: "/address/crud/",
                data:{
                    'name': $scope.new_name,
                    'address': $scope.new_address,
                    'city': $scope.new_city,
                    'state': $scope.new_state,
                    'phone': $scope.new_phone,
                    'pincode': $scope.new_pincode,
                    'address2': $scope.new_address2
                }
            }, console.log($scope.new_pincode)).error(function(response) {
                console.log(response)
            }).then(function successCallback(response) {
                console.log(response)
                if(response.data.data){
                    response.data.data.state=$scope.new_state
                    $scope.addresses.push(response.data.data)
                    $scope.modal_pop=0
                    $scope.new_name = ''
                    $scope.new_address = ''
                    $scope.new_city = ''
                    $scope.new_state = ''
                    $scope.new_phone = ''
                    $scope.new_pincode = ''
                }else{
                    alert(JSON.stringify(response.data.detail))
                }
         });
    }






$(function () {

  'use strict';

  var console = window.console || { log: function () {} };
  var $image = $('#image');
  // var $download = $('#download');
  var $dataX = $('#dataX');
  var $dataY = $('#dataY');
  var $dataHeight = $('#dataHeight');
  var $dataWidth = $('#dataWidth');
  var $dataRotate = $('#dataRotate');
  var $dataScaleX = $('#dataScaleX');
  var $dataScaleY = $('#dataScaleY');
  var options = {
        aspectRatio: 1 / 1,
        preview: '.img-preview',
        crop: function (e) {
          $dataX.val(Math.round(e.x));
          $dataY.val(Math.round(e.y));
          $dataHeight.val(Math.round(e.height));
          $dataWidth.val(Math.round(e.width));
          $dataRotate.val(e.rotate);
          $dataScaleX.val(e.scaleX);
          $dataScaleY.val(e.scaleY);
        }
      };


  // Tooltip
  $('[data-toggle="tooltip"]').tooltip();


  // Cropper
  $image.on({
    'build.cropper': function (e) {
      console.log(e.type);
    },
    'built.cropper': function (e) {
      console.log(e.type);
    },
    'cropstart.cropper': function (e) {
      console.log(e.type, e.action);
    },
    'cropmove.cropper': function (e) {
      console.log(e.type, e.action);
    },
    'cropend.cropper': function (e) {
      console.log(e.type, e.action);
    },
    'crop.cropper': function (e) {
      console.log(e.type, e.x, e.y, e.width, e.height, e.rotate, e.scaleX, e.scaleY);
    },
    'zoom.cropper': function (e) {
      console.log(e.type, e.ratio);
    }
  }).cropper(options);


  // Buttons
  if (!$.isFunction(document.createElement('canvas').getContext)) {
    $('button[data-method="getCroppedCanvas"]').prop('disabled', true);
  }

  if (typeof document.createElement('cropper').style.transition === 'undefined') {
    $('button[data-method="rotate"]').prop('disabled', true);
    $('button[data-method="scale"]').prop('disabled', true);
  }


  // Download
  // if (typeof $download[0].download === 'undefined') {
  //   $download.addClass('disabled');
  // }


  // Options
  $('.docs-toggles').on('change', 'input', function () {
    var $this = $(this);
    var name = $this.attr('name');
    var type = $this.prop('type');
    var cropBoxData;
    var canvasData;

    if (!$image.data('cropper')) {
      return;
    }

    if (type === 'checkbox') {
      options[name] = $this.prop('checked');
      cropBoxData = $image.cropper('getCropBoxData');
      canvasData = $image.cropper('getCanvasData');

      options.built = function () {
        $image.cropper('setCropBoxData', cropBoxData);
        $image.cropper('setCanvasData', canvasData);
      };
    } else if (type === 'radio') {
      options[name] = $this.val();
    }

    $image.cropper('destroy').cropper(options);
  });


  // Methods
  $('.docs-buttons').on('click', '[data-method]', function () {
    var $this = $(this);
    var data = $this.data();
    var $target;
    var result;

    if ($this.prop('disabled') || $this.hasClass('disabled')) {
      return;
    }

    if ($image.data('cropper') && data.method) {
      data = $.extend({}, data); // Clone a new one

      if (typeof data.target !== 'undefined') {
        $target = $(data.target);

        if (typeof data.option === 'undefined') {
          try {
            data.option = JSON.parse($target.val());
          } catch (e) {
            console.log(e.message);
          }
        }
      }

      result = $image.cropper(data.method, data.option, data.secondOption);

      switch (data.method) {
        case 'scaleX':
        case 'scaleY':
          $(this).data('option', -data.option);
          break;

        case 'getCroppedCanvas':
          if (result) {

            // Bootstrap's Modal
            // console.log(result.toDataURL())
            setTimeout(function(){

            $('.crop-image').removeClass('is_visible');
            $scope.images_selected.push({'id':$scope.img_id,'img_url': result.toDataURL('image/jpeg')})
            $scope.img_id=$scope.img_id+1;
            $scope.$apply()
            $scope.show_crop = false
            })
            // $('#getCroppedCanvasModal').modal().find('.modal-body').html(result);

            // if (!$download.hasClass('disabled')) {
            //   $download.attr('href', result.toDataURL('image/jpeg'));
            // }
          }

          break;
      }

      if ($.isPlainObject(result) && $target) {
        try {
          $target.val(JSON.stringify(result));
        } catch (e) {
          console.log(e.message);
        }
      }

    }
  });


  // Keyboard
  $(document.body).on('keydown', function (e) {

    if (!$image.data('cropper') || this.scrollTop > 300) {
      return;
    }

    switch (e.which) {
      case 37:
        e.preventDefault();
        $image.cropper('move', -1, 0);
        break;

      case 38:
        e.preventDefault();
        $image.cropper('move', 0, -1);
        break;

      case 39:
        e.preventDefault();
        $image.cropper('move', 1, 0);
        break;

      case 40:
        e.preventDefault();
        $image.cropper('move', 0, 1);
        break;
    }

  });


  // Import image
  var $inputImage = $('#inputImage');
  var URL = window.URL || window.webkitURL;
  var blobURL;

  if (URL) {
    $inputImage.change(function () {
      $scope.show_crop = false
      $('.crop-image').removeClass('is_visible')
      var files = this.files;
      var file;

      if (!$image.data('cropper')) {
        return;
      }

      if (files && files.length) {
          $scope.show_crop = true
          $('.crop-image').addClass('is_visible')
          $('.img-container').removeClass('ng-hide')
          $('.clearfix').removeClass('ng-hide')
        file = files[0];

        if (/^image\/\w+$/.test(file.type)) {
          blobURL = URL.createObjectURL(file);
          $image.one('built.cropper', function () {

            // Revoke when load complete
            URL.revokeObjectURL(blobURL);
          }).cropper('reset').cropper('replace', blobURL);
          $inputImage.val('');
        } else {
          window.alert('Please choose an image file.');
        }
      }
    });
  } else {
    $inputImage.prop('disabled', true).parent().addClass('disabled');
  }

});






    $scope.fasioncalculator = function(){
        if(!$scope.original_price){
            $scope.listing_price = 0
            return false            
        }
        if(parseInt($scope.original_price) == 0){
            $scope.listing_price = 0
            return false
        }
        if($scope.age_selected && $scope.condition && $scope.original_price){
            $http({
                    method: 'POST',

                    url: "/catalogue/zapfashioncalculator/",
                    data:{
                        'age':$scope.age_selected['id'],
                        'condition':$scope.condition['id'],
                        'original_price':$scope.original_price,
                    }
                }).error(function(response) {
                    console.log(response)
                }).then(function successCallback(response) {
                    $scope.listing_price = response.data.max_listing_price
                    $("#slider").attr('max', response.data.max_listing_price);
                    $("#slider").val(response.data.max_listing_price);  
                    //$("#slider").slider('refresh');
            });
        }
    }

    var typingTimer;
    var $input = $('#org_price');
    $input.on('keyup', function () {
      clearTimeout(typingTimer);
      typingTimer = setTimeout($scope.fasioncalculator(), 2000);
    });
    $input.on('keydown', function () {
      clearTimeout(typingTimer);
    });

    var output = document.getElementById('range');
    output.innerHTML = $('#slider').val();

function showValue(newValue) {
    output.innerHTML = newValue;
}

$('#slider').change(function(e) {
    showValue($(this).val());

});
});

angular.module('zapyle')
    .controller('PaymentCheckCtrl', function($scope,$http,$localStorage) {

    
})