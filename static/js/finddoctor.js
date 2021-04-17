console.log("Find Doctor Connecting!");
$('#aTab1').on('click',function(){
    $('#aTab1').attr("aria-selected","true");
    $('#aTab2').attr("aria-selected","false");
    $('#aTab1').addClass('active');
    $('#tab-1').addClass('active show');
    $('#tab-2').removeClass('active show');
    $('#aTab2').removeClass('active');
})
$('#aTab2').on('click',function(){
    $('#aTab2').attr("aria-selected","true");
    $('#aTab1').attr("aria-selected","false");
    $('#aTab2').addClass('active');
    $('#aTab1').removeClass('active');
    $('#tab-2').addClass('active show');
    $('#tab-1').removeClass('active show');
})

$('.doctor__action__btn--appointment').on('click',function () {
    $('#divDoctorName').css('display', ' ');

})