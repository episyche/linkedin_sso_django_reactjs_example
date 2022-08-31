import './App.css';
import linkedin from "./linkedin.png";
import {LinkedIn} from 'react-linkedin-login-oauth2';


function App() {
  function handleFailure(e){
    alert(e)
  }
  function handleSuccess(e){
    fetch("http://127.0.0.1:8000/linkedin/",{
      method:"POST",
      body:JSON.stringify({'auth_token':e}),
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      }
    })
    .then((res)=>res.json())
    .then((res)=>{
      document.getElementById("email_id").innerText=res['email']
      document.getElementById("Auth_token").innerText=res['tokens']
    })
  }
  return (
    <div>
      <LinkedIn
        clientId="LinkedIn Client Id"                                     //LinkedIn Client Id
        redirectUri={`${window.location.origin}/linkedin`}
        onSuccess={handleSuccess}
        onFailure={handleFailure}
        className='linkedin'>
        {({ linkedInLogin }) => (
          <img
            className='linkedin'
            onClick={linkedInLogin}
            src={linkedin}
            alt="Sign in with Linked In"

          />
        )}
      </LinkedIn>
      <div className='show_info'>
        <div>
          <label>Email Id: </label>
          <label id='email_id'></label>
        </div>
        <div>
          <label>Auth Token : </label>
          <label id='Auth_token'></label>
        </div>
      </div>
    </div>
  );
}

export default App;
