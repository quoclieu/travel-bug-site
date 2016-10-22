
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
      var buttonFacebook = document.getElementById('btn-continue-with-facebook');
      var userDetails=null;
      var firstName = null;
      var lastName = null;
      var email = null;
      var password = null;
      var rePwd = null;
      var userDetailsFacebook=null;
    
      window.onload = function() {
           initApp();
         };   

      /**
       * initApp handles registering Firebase auth listeners:
       *  - firebase.auth().onAuthStateChanged: This listener is called when the user is signed in 
       *    and that is where we push userDetails in firebase realtime-database.
       *    The user will log out automatically once after their userDetails be stored.
       */
      function initApp(){
        //Listening for auth state changes.
        //[START authstatelistener]
        firebase.auth().onAuthStateChanged(function(user){
          if(user){
            //User is signed in.
            if(userDetails!=null){
				//If the user registered via email & pwd
				emailPwdStore(user);
                           
            }else{
				//If the user continued with Facebook
			    fbStore(user);
			}
            setTimeout('signOut()',3000);//This function will be deleted once after-login website is created

          }else{
           console.log("Not logged in");
      }

        });
        // [END authstatelistener]     
    
      }
    
    //Add signup event
    buttonSignUp.addEventListener('click', handleSignUp, false); 
    //Add fb sign in
    buttonFacebook.addEventListener('click', FacebookSignIn, false);

    /**
    *sign out
    */
   function signOut(){
        firebase.auth().signOut().then(function() {
        // Sign-out successful.
           }, function(error) {
        // An error happened.
        });
   }

      /**
       * Handles the sign up button press
       * Tries to create a new user account with the given email address and password. 
       * If successful, it also signs the user in into the app.
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

    /**
     * Function called when clicking the Continue with Facebook button.
     */
    // [START buttoncallback]
    function FacebookSignIn() {
      if (!firebase.auth().currentUser) {

        // [START createprovider]
        var provider = new firebase.auth.FacebookAuthProvider();
        // [END createprovider]
        // [START addscopes]
        provider.addScope('email');
        // [END addscopes]
        // [START signin]
        firebase.auth().signInWithPopup(provider).then(function(result) {
          // This gives you a Facebook Access Token. You can use it to access the Facebook API.
          var token = result.credential.accessToken;
          // The signed-in user info.
          var user = result.user;
          // [START_EXCLUDE]
         // document.getElementById('quickstart-oauthtoken').textContent = token;
          // [END_EXCLUDE]
        }).catch(function(error) {
          // Handle Errors here.
          var errorCode = error.code;
          var errorMessage = error.message;
          // The email of the user's account used.
          var email = error.email;
          // The firebase.auth.AuthCredential type that was used.
          var credential = error.credential;
          // [START_EXCLUDE]
          if (errorCode === 'auth/account-exists-with-different-credential') {
            alert('You have already signed up with a different auth provider for that email.');
            // If you are using multiple auth providers on your app you should handle linking
            // the user's accounts here.
          } else {
            console.error(error);
          }
          // [END_EXCLUDE]
        });
        // [END signin]
      } else {
        alert("You have signed in with Facebook!");
      }

    }
    // [END buttoncallback]

    /**
	*Strore the user details in database
	*/
    function fbStore(user){
      if(user!=null){
        dbRefUsers.once('value', function(snapshot) {
          if (!snapshot.hasChild(user.uid)) {
            //alert("fill userFacebookInfo");
            fillUserDetailsFacebook(user);
            //alert("fill userFacebookInfo successfully");
              var fbFirstName = getFirstName(user.displayName);
              //alert("updateDisplayName");
              updateDisplayName(user,fbFirstName);
              //alert("updateDisplayName successfully");
              dbRefUsers.child(user.uid).set(userDetailsFacebook);
              alert("You have signed in with Facebook!");
                       
            }
        });
      }
    }
	
	function emailPwdStore(user){
		if(user!=null){
			 //If the user choose the email method and is the first time to sign in 
               updateDisplayName(user,firstName);
               //store the user details into firebase        
               dbRefUsers.child(user.uid).set(userDetails); 
               //alert("push successfully !");  
               setTimeout('sendEmailVerification()',1000); 
		}
	}



    /**
    *get the first name
    */
    function getFirstName(fullName){
      return fullName.split(' ').slice(0, -1).join(' ');
    }

    /**
    *get the last name
    */
    function getLastName(fullName){
      return  fullName.split(' ').slice(-1).join(' ');
    }
	
    /**
    *Fill user infomations from facebook
    */
    function fillUserDetailsFacebook(user){
      userDetailsFacebook={
        UserDetails:{
          email: user.email,
          firstName:getFirstName(user.displayName),
          lastName: getLastName(user.displayName),
          phone: "No Phone Added",
          puserrofileImage: user.photoURL
        }
      }

    }

    /**
	*Fill user infomations from email & pwd
	*/
    function fillUserDetails(){
        //Get userDetails
        firstName = document.getElementById("form-first-name").value;
        lastName = document.getElementById("form-last-name").value;
        email=document.getElementById("form-email").value;
      userDetails = {UserDetails: {
                                email: email,
                                firstName: firstName,
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
 
    /**
     * Sends an email verification to the user.
     */
    function sendEmailVerification() {
      var firebaseuser = firebase.auth().currentUser;
      // [START sendemailverification]
      firebaseuser.sendEmailVerification().then(function() {
        // Email Verification sent!
        // [START_EXCLUDE]
        if(email !=null){
          alert('Please check your email at '+email+' to verify the address.');
        }else{
          alert('Please check your email at '+firebaseuser.email+' to verify the address.');
        }
       
      });
      // [END sendemailverification]
    }

    function updateDisplayName(user,firstName){
      


        // User is signed in.
        user.updateProfile({
            displayName: firstName
        }).then(function() {
            // Update successful.
            //alert("updateProfile");
        }, function(error) {
            // An error happened.
            var errorMessage = error.message;
            alert(errorMessage);
        });

    }
