let addedMessage = {}

  async function getResponse(response) {
    addedMessage = await response.json()
    addedMessage = JSON.parse(addedMessage)
  }


  function createMessage(){
    let formData = new FormData();
    formData.append('textmessage', message_content.value);
    formData.append('csrfmiddlewaretoken', token);
    return formData
  }

  async function sendMessage(event) {
    try {
      message_container.innerHTML +=
      HTMLbeforeAdd(message_content)
      let response = await fetch('/chat/', {
        method: 'POST',
        body: createMessage()
      });
      await getResponse(response)
      timeout(addedMessage)
      message_content.value=''
    } catch (error) {
      console.error('Error sending message:', error);
    }
}


  function timeout(addedMessage){
    setTimeout(() => {
      document.getElementById('toDelete').remove()
      message_container.innerHTML +=
      HTMLonAdd(addedMessage)
  }, 500)
  }

  function HTMLonAdd(addedMessage){
  
    return ` <div>
    <div class="messageContainer">
     <div class="nameContent">
       <b>${username}:</b> <div>${addedMessage.fields.text}</div>
     </div>
    </div>
  </div>`
  }


  function HTMLbeforeAdd(message_content){

  return `<div class="messageContainer" id="toDelete">
      <span style="color:grey">${username}</span> 
        <span style="color:grey">${message_content.value}</span> 
     </div>`
  }