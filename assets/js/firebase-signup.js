
// Initialize Firebase
  var config = {
    apiKey: "AIzaSyA9-kemWmPvaN-ZmmUZXoJejsoaxHB3fxY",
    authDomain: "travel-bug-potential-user.firebaseapp.com",
    databaseURL: "https://travel-bug-potential-user.firebaseio.com",
    storageBucket: "",
    messagingSenderId: "374111239552"
  };
  firebase.initializeApp(config);


	  
	 //Get elements
      var buttonSignUp = document.getElementById('btn-signup');
      var userDetails=null;
      var firstName = null;
      var lastName = null;
      var email = null;
      var receiveEmail = null;
	  var encodedEmail = null;
	  	  
	  //Add signup event
	  buttonSignUp.addEventListener('click', handleSignUp, false); 
	 

      /**
       * Handles the sign up button press
       * Tries to create a new user account with the given email address and password. 
       * If successful, it also signs the user in into the app.
       */
      function handleSignUp(){      		
        if(checkSignUp){
        	fillUserDetails();     	
        	var promise = firebase.database().ref('PotentialUser/'+encodedEmail).set(userDetails);
            promise.then(
                    // Log the fulfillment value
                    function(val) {
						alert("Sign Up Successfully");
                    })
                .catch(
                    // Log the rejection reason
                    function(reason) {
                        console.log('Handle rejected promise ('+reason+') here.');
                        alert(reason);
                    });
		}
	  }

      function fillUserDetails(){
      	//Get userDetails     
		email=document.getElementById("form-email").value;
		firstName = document.getElementById("form-first-name").value;
		lastName = document.getElementById("form-last-name").value;
      	receiveEmail = getReceiveValue();
      	encodedEmail = email.replace(/\./g, ",");
      	if(receiveEmail!=null){
      		userDetails = {
                                email: email,
                                firstName: firstName,
                                isReceive:receiveEmail,
                                lastName: lastName                                
	                  }
        }
      }

	    

      function getReceiveValue(){
      	var reveiveEmails = document.getElementsByName('form-receiveEmail');
        for(var i = 0; i < reveiveEmails.length; i++){
            if(reveiveEmails[i].checked){
                receiveEmail = reveiveEmails[i].value;
            }
        }
        return receiveEmail;
      }
 

      function checkSignUp(){
		   if(firstNameBlur()&&lastNameBlur()&&emailBlur()){
		    return true;
		}else {
		    return false;
		}
		   
	   }
	   
	   function firstNameBlur(){
	   	 firstName = document.getElementById("form-first-name").value;
	     if(firstName.length==0){
		       alert("Please input your first name.");
		       return false;
	       }else{
			   return true;
		   }
	   }
	   
	   
	   function lastNameBlur(){
	     lastName = document.getElementById("form-last-name").value;	        
	     if(lastName.length==0){
		       alert("Please input your last name.");
		       return false;
	       }else{
			   return true;
		   }
	   }
	   
	   function emailBlur(){
	       email=document.getElementById("form-email").value;	       
	       var reg=/^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$/;
	       if(reg.test(email)){
		       return true;   
	       }else{
		       alert("Please input a correct email format.");
		       return false;
		   }
	   }

		
 
	   
