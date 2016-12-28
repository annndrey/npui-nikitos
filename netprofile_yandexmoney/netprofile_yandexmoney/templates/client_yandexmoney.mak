## -*- coding: utf-8 -*-

<li class="list-group-item">
  <form class="row" id="ymform" role="form" method="post" action="https://money.yandex.ru/eshop.xml" target="_top">
    <label for="" class="col-sm-4">${_('Yandex.Money Payment')}</label>
    <div class="col-sm-8 form-inline">
      <input name="shopId" value="24278" type="hidden"/>
      <input name="scid" value="38471" type="hidden"/>
      <input name="sum" class="form-control" type="text" placeholder="${_('Enter amount')}" title="${_('Enter payment amount')}" required="required" tabindex="-1" autocomplete="off" value=""/>
      <input name="paymentType" value="" type="hidden"/>
      <input name="xopid" id="xopid" value="" type="hidden"/>
      <input name="shopSuccessUrl" value="${req.current_route_url()}" type="hidden"/>
      <input name="shopFailUrl" value="${req.current_route_url()}" type="hidden"/>
      <input name="customerNumber" value="${stash.id}" type="hidden"/>
      <input name="goods_name_N" value="${_('Stash refill')}" type="hidden"/>
      <input name="csrf" value="${req.get_csrf()}" type="hidden" />
      <button class="btn btn-default" type="submit" name="submit" title="${_('Press to make payment')}">${_('Pay')}</button>
    </div>
  </form>
</li>

<script type="text/javascript">
$( "#ymform" ).submit(function( event ) {
   event.preventDefault();
   var $form = $( this ),
   shopid = $form.find( "input[name='shopId']" ).val(),
   sum = $form.find( "input[name='sum']" ).val(),
   stashid = $form.find( "input[name='customerNumber']" ).val();
   var posting = $.post( "${req.route_url("yandexmoney.cl.neworder")}", { shopid: shopid, diff: sum, stash: stashid } );
   posting.done(function( data ) {
     var content = $( data );
     $( "#xopid" ).val(data);
     $("#ymform").unbind('submit').submit();
   });
  });
$( "#ymform" ).submit();
</script>
