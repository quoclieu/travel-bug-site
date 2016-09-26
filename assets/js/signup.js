// JavaScript Document

      function checkSignUp(){
		   if(firstNameBlur()&&lastNameBlur()&&emailBlur()&&pwdBlur()&&confirmPwdBlur()){
		    alert("Successful !");
		    return true;
		}else {
		    return false;
		}
		   
	   }

      function pwdBlur(){
		   var passw = document.getElementById("form-pwd").value;
		    if(passw.length<6){
		       alert("Please input a password whose length is over 6.");
		       return false;
	       }else{
			   return true;
		   }  
	   }       
	   
	    function confirmPwdBlur(){
		   var passwo = document.getElementById("form-pwd").value;
		   var rePwd = document.getElementById("form-rePwd").value;
           if(passwo==rePwd){
		       return true;   
	       }else{
		       alert("Please ensure you input the same password.");
		       return false;
	       }	   
	   }
	   
	   function firstNameBlur(){
	     var firstName = document.getElementById("form-first-name").value;   
	     if(firstName.length==0){
		       alert("Please input your first name.");
		       return false;
	       }else{
			   return true;
		   }
	   }
	   
	   
	   function lastNameBlur(){
	     var firstName = document.getElementById("form-last-name").value;   
	     if(firstName.length==0){
		       alert("Please input your last name.");
		       return false;
	       }else{
			   return true;
		   }
	   }
	   
	   function emailBlur(){
	       var email=document.getElementById("form-email").value;
	       var reg=/^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$/;
	       if(reg.test(email)){
		       return true;   
	       }else{
		       alert("Please input a correct email format.");
		       return false;
	   }
	  
	   
   }