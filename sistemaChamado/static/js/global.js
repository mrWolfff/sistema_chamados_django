
$(document).ready(function(){

	//modificar o ativo das navs
	$('#nao_realizado').click(function(event){
		$('#todos').removeClass('active');
		$('#em_andamento').removeClass('active');
		$('#concluidos').removeClass('active');
		$(this).addClass('active');
	});
	$('#em_andamento').click(function(event){
		$('#todos').removeClass('active');
		$('#nao_realizado').removeClass('active');
		$('#concluidos').removeClass('active');
		$(this).addClass('active');
	});
	$('#concluidos').click(function(event){
		$('#todos').removeClass('active');
		$('#em_andamento').removeClass('active');
		$('#nao_realizado').removeClass('active');
		$(this).addClass('active');
	});
	$('#todos').click(function(event){
		$('#concluidos').removeClass('active');
		$('#em_andamento').removeClass('active');
		$('#nao_realizado').removeClass('active');
		$(this).addClass('active');
	});

	//modificar a nav lateral
	$('.toggle-nav').click(function(event) {
		event.stopPropagation();
		toggleNav();
	});
	$('#main').click(function (event){
		let target = $(event.target);
		if(!target.closest('#nav').length && $('#wrapper').hasClass('show-nav')) toggleNav();
	});
	function toggleNav(){
		if($('#wrapper').hasClass('show-nav')){
			$('#wrapper').removeClass('show-nav');   
		}
		else {
			$('#wrapper').addClass('show-nav');
		}
	}

	//checkbox do index
	$(".form-check-input").change(function() {
		if ($(this).prop("checked") == true) {
			$("#tr").removeClass('table-light');
			$('#tr').addClass('table-active');
		}else{
			$("#tr").removeClass('table-active');
			$('#tr').addClass('table-light');
		}
	});

	//faixa bem vindo usuario
	$('.card').hover(
		function() {
			$(this).removeClass('bg-light');
			$(this).addClass(' bg-primary');
		},function(){
			$(this).removeClass('bg-primary');
			$(this).addClass(' bg-light');
		});



});