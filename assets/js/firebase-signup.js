/*the following app.js will deal with the user details which include the userName, email and password
 from the form, and passing them to the firebase.*/

/*This ap.js initializes Firebase, gets the user details first .
 Since for now we set our database rules as default in the firebase console:

{
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null"
  }
}
 It requires  Authentication.

 So we need to sends two elements: email and password to firebase to get authentication (Sign up) in order 
 to write user details in real-time databse. 
 
 We cannot write the userName and email as soon as we get the authentication, so we cannot write push(data) 
 in the signup eventListener. 
 (if we set public database rules, we can write push() in the signup eventListener, but we'd better not do that)
 
 After the authentication, the userName and email may be stored in the real-time database via 
 method auth().onAuthStateChanged of Firebase SDK
 */

(function(){
	
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
  const txtEmail = document.getElementById("form-email");
  const txtPassword = document.getElementById("form-password");
  const btnSignUp = document.getElementById("btn-signup");
  const txtFirstName= document.getElementById("form-first-name");
  const txtLastName= document.getElementById("form-last-name");
  // const btnLogout = document.getElementById("btnLogout");
  
  //Create a database refernce, so we can add userDetails in to real-time database
  const dbRefUsers = firebase.database().ref().child('User');
  var userDetails=null; //This var is going to hold JOSN (email and fullName from the form)
  
	  
  //Add signup event
  btnSignUp.addEventListener('click', function(e){
	  //Get email and password
	  //TODO: CHECK IF IT IS A REAL EMAIL
	  const email = txtEmail.value;
	  const pass = txtPassword.value;
	  const firstName = txtFirstName.value;
	  const lastName = txtLastName.value;
	  const auth = firebase.auth(); 

	  userDetails = {UserDetails: {
                                   Email: email,
                                   FirstName: firstName,
                                   LastName: lastName
                                   }
	  }
      //Sign up
	  const promiseSignUp = auth.createUserWithEmailAndPassword(email,pass);
	  //Above promiseSignUp can only work for one time, so we should add a realTime listener latter
	   
	   
	  //Print & alert the message if there is an error, 
	  //such as: if the email has already been auth, the firebase will reject adding them automatically
	  promiseSignUp.catch(function(e){
		  console.log(e.message)
		  alert(e.message);
		  userDetails = null;//Clear the userDetails so that it won't be stored in the real-time database
		  });

		});
		

  //Add a realTime listener
   firebase.auth().onAuthStateChanged( function(firebaseUser){
	   if(firebaseUser){//If there is a firebaseUser( which means we've already signed in)
		   console.log(firebaseUser);
		   if(userDetails!=null){ //store the user details into firebase			   
		      dbRefUsers.push(userDetails); 
			  alert("Successfully pushed");	 
		   }
	   }else{
		   console.log("Not logged in");
		   btnLogout.style.visibility = "hidden" //If there is no user signed up, hides the log out button	   	 
	   }
       });
	   
	// //Sign out, in order try to add differnet users
    //btnLogout.addEventListener('click', function(e){
	// 	   firebase.auth().signOut();
	//    });
	   
	}());