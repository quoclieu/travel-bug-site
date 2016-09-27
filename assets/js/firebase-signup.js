
     // Initialize Firebase
      var config = {
         apiKey: "AIzaSyBNT4gDmMljV3Oko-E5WLMnNvW9mBfQ5FE",
         authDomain: "travel-bugg.firebaseapp.com",
         databaseURL: "https://travel-bugg.firebaseio.com",
         storageBucket: "travel-bugg.appspot.com",
         messagingSenderId: "262014884649"
      };
      firebase.initializeApp(config);
	  
	 //Get elements
      var dbRefUsers = firebase.database().ref().child('User');
      var buttonSignUp = document.getElementById('btn-signup');
      var userDetails=null;
      var firstName = null;
      var lastName = null;
      var email = null;
      var password = null;
      var rePwd = null;
	  
      window.onload = function() {
           initSignUp();
         };	  

      /**
       * initApp handles registering Firebase auth listeners:
       *  - firebase.auth().onAuthStateChanged: This listener is called when the user is signed in 
       *    and that is where we push userDetails in firebase realtime-database.
       *    The user will log out automatically once after their userDetails be stored.
       */
      function initSignUp(){
      	//Listening for auth state changes.
      	//[START authstatelistener]
      	firebase.auth().onAuthStateChanged(function(user){
      		if(user){
      			//User is signed in.
      			if(userDetails!=null){ 
      			   //store the user details into firebase			   
		           dbRefUsers.push(userDetails); 
		           alert("Sign up successfully !");	 
		           firebase.auth().signOut();
		        }
      		}else{
		       console.log("Not logged in");
			}

      	});
      	// [END authstatelistener]     
		
      }
	  
	  //Add signup event
	  buttonSignUp.addEventListener('click', handleSignUp, false); 
	 

      /**
       * Handles the sign up button press
       */
      function handleSignUp(){      		
        if(checkSignUp){
        	fillUserDetails();
      		//Sign in with email and pass
      		// [START createwith email]
      		email=document.getElementById("form-email").value;
      		password = document.getElementById("form-pwd").value;
            firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
              // Handle Errors here.
              var errorMessage = error.message;
              // [START_EXCLUDE]
              alert(errorMessage);
              console.log(error);
              // [END_EXCLUDE]
              //Clear the userDetails
              userDetails = null;
           });
          // [END createwithemail]     		
        }
      }

      function fillUserDetails(){
      	//Get userDetails
      	firstName = document.getElementById("form-first-name").value;
      	lastName = document.getElementById("form-last-name").value;
      	email=document.getElementById("form-email").value;
	    userDetails = {UserDetails: {
                                Email: email,
                                FirstName: firstName,
                                lastName: lastName
                                    }
	                  }
        }
 

      function checkSignUp(){
		   if(firstNameBlur()&&lastNameBlur()&&emailBlur()&&pwdBlur()&&confirmPwdBlur()){
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

	   function pwdBlur(){
	        password = document.getElementById("form-pwd").value;		   
		    if(password.length<6){
		       alert("Please input a password whose length is over 6.");
		       return false;
	       }else{
			   return true;
		   }  
	   }       
	   
	    function confirmPwdBlur(){
	       password = document.getElementById("form-pwd").value;
	       rePwd = document.getElementById("form-rePwd").value;		   		  
           if(password==rePwd){
		       return true;   
	       }else{
		       alert("Please ensure you input the same password.");
		       return false;
	       }	   
	   }
 
	   
   