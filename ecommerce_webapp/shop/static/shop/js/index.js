debugger;
      console.log("Working")
      var count=0;
      if(localStorage.getItem('cart')==null)
      {
        var cart={};
      }
      else
      {
        cart=JSON.parse(localStorage.getItem('cart'));
        var count=0;
        for(var item in cart) {
        
              var value = cart[item][0];
              count=count+value;
          
      }
        document.getElementById('cart').innerHTML=count;
       
      }
      
      $('.divproduct').on('click','button.cart',function(){

        console.log("clicked")
        idstr=this.id.toString();
        console.log(idstr);
        
        if(cart[idstr]!=undefined)
        {
          quantity=cart[idstr][0]+1;
          
        }
        else{
          quantity=1;
          product_name=document.getElementById("name"+idstr).innerHTML;
          product_price=document.getElementById("price"+idstr).innerHTML;
          cart[idstr]=[quantity,product_name,parseInt(product_price)];

          
        }
        console.log(cart);
        localStorage.setItem('cart',JSON.stringify(cart));
        updateCart();
        //document.getElementById('cart').innerHTML=Object.keys(cart).length;
      });

      //$('#popcart').popover();    
      updatePopover(cart);
      function updatePopover(cart){
        debugger;
        var popStr="";
        popStr=popStr+"<h6>Items in your shopping cart</h6><div class='my-2'>";
        var i=1;
        var totalPrice=0;
        for(var item in cart){
          popStr=popStr+i+") ";
              var price=0;
              price=cart[item][2]*cart[item][0];
              //price=document.getElementById('price'+item).innerHTML*cart[item][0];
              totalPrice=totalPrice+price;
              popStr=popStr+cart[item][1].slice(0,12)+"...Rs "+cart[item][2]+" * "+cart[item][0]+" = <b>Rs "+ price+"</b><br>";
              i=i+1;
        }
        popStr=popStr+"</div>";
        popStr=popStr+"<div class='btn btn-sm btn btn-black col-md-12'>Total Bill is Rs. "+totalPrice+"</div><br>";
        popStr=popStr+"<div><a href='/shop/checkout' class='btn btn-sm btn-blue col-md-12 my-2' >Checkout</a></div>";
        console.log(popStr);
        document.getElementById("popcart").setAttribute('data-content', popStr);
       // $('.cartpopup').on('click','button.popcart',function(){
       //   $('#popcart').popover('toggleEnabled');
      //  });
        $('#popcart').click(function(){
          $('#popcart').popover('show');
        })
        //$('#popcart').popover('hide');
        //$('#popcart').popover('show');
        
          

      }
      function clearCart()
      {
        debugger;
            cart=JSON.parse(localStorage.getItem('cart'));
            if(cart==null)
            {
              swal("Cart is already empty");
              
            }
            else{
              localStorage.clear();
              cart={};
            }
            for(var item in cart){
              if(document.getElementById('div'+item)!=null)
              document.getElementById('div'+item).innerHTML=`<button id="${item}" class="btn btn-blue cart">Add To Cart</button>`;
            }
            updateCart();
      }
      //document.getElementById("popcart").setAttribute('data-content', '<h6>Cart for your items in my shopping cart</h6>');

      function updateCart()
      {
        debugger;
        var sum=0;
        for(var item in cart){
          sum=sum+cart[item][0];
          document.getElementById("div"+item).innerHTML="<button id='minus"+item+"' class='btn btn-blue minus' ><b>-</b></button><span id='val"+item+"' ><b style='padding:5px;'>"+cart[item][0]+"</b></span><button id='plus"+item+"' class='btn btn-blue plus' ><b>+</b></button>";
        }
        document.getElementById('cart').innerHTML=sum;
        updatePopover(cart);
      }
      $('.divproduct').on('click','button.minus',function(){
        console.log("minus")
        item_number=this.id.slice(12,)
        cart['product'+item_number][0]=cart['product'+item_number][0]-1;
        cart['product'+item_number][0]=Math.max(0,cart['product'+item_number][0]);
        document.getElementById('valproduct'+item_number).innerHTML=cart['product'+item_number][0];
        if(cart['product'+item_number][0]==0)
        {document.getElementById('divproduct'+item_number).innerHTML=`<button id="product${item_number}" class="btn btn-blue cart">Add To Cart</button>`
        delete cart['product'+item_number];
        }
        else{
          document.getElementById('valproduct'+item_number).innerHTML=cart['product'+item_number][0];
        }
        localStorage.setItem('cart',JSON.stringify(cart));
        updateCart();
        console.log(item_number);
      });
      $('.divproduct').on('click','button.plus',function(){
        debugger;
        console.log("plus")
        item_number=this.id.slice(11,);
        cart['product'+item_number][0]=cart['product'+item_number][0]+1;
  
        //Math.max(0,item_number);
        document.getElementById('valproduct'+item_number).innerHTML=cart['product'+item_number][0];
        localStorage.setItem('cart',JSON.stringify(cart));
        updateCart();
        console.log(item_number);
      });