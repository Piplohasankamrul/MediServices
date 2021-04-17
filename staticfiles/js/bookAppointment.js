console.log("book Appointment");
$(document).ready(function(){
    $('#doctor-button').click(function(){
        $('#pick-doctor').css('display', '');
        $('#pick-doctor').load('td.html');
    });
});
$('#recommedaSpecialistForMe').on('click',function () {
    $('#divSpecialty').css('display','');
    $('#divDoctorName').css('display','none');

});
$('#iWillChooseMyDoctor').on('click',function () {
    $('#divSpecialty').css('display','');
    $('#divDoctorName').css('display','');

});
$('#earliestDate').on('click',function () {
    $('#divPreferredDate').css('display','none');
});
$('#preferredDate').on('click',function () {
    $('#divPreferredDate').css('display','');
});
$('#btnNextStep').on('click',function () {
    $('#divStep1Section').css('display','none');
    $('#divStep2Section').css('display','');
    $('#btnBackStep').css('display','');
    $('#btnBackStep').on('click',function () {
        $('#divStep1Section').css('display','');
        $('#divStep2Section').css('display','none');
        $('#divStep3Section').css('display','none');
        $('#btnBackStep').css('display','none');
    });
    $('#btnNextStep').on('click',function () {
        $('#divStep1Section').css('display','none');
        $('#divStep2Section').css('display','none');
        $('#divStep3Section').css('display','');
        $('#btnBackStep').css('display','');
        $('#btnBackStep').on('click',function () {
            $('#divStep1Section').css('display','none');
            $('#divStep2Section').css('display','');
            $('#divStep3Section').css('display','none');
            $('#btnBackStep').on('click',function () {
                $('#divStep1Section').css('display','');
                $('#divStep2Section').css('display','none');
                $('#divStep3Section').css('display','none');
                $('#btnBackStep').css('display','none');
            });
        });
    });


});