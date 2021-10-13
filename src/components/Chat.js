import ChatBot from 'react-simple-chatbot';
const Chat = () => {
    return (  
        <div className="chat">
         <ChatBot
          steps={[
            {
                id:'intro', 
                message:'Hello.Do you have your order id?', 
                trigger:'intro-user',
               },
               {
                id:'intro-user', 
                options:[
                  {value:'y', label:'Yes', trigger:'yes-response'},
                  {value:'n', label:'No', trigger:'no-response'},
                ] ,
               },
               {
                id:'yes-response', 
                message:'Please enter you order id',
                trigger:'order'
               },
               {
                id:'no-response', 
                message:'Sorry to hear that.I can not help you any further ', 
                end:true,
               },
               {
                id:'order', 
                user:true, 
                validator: (value) => {
                   if (value==='0-9')
                     {
                       return true;
                     }
                   else
                     {
                       return'Please input numeric characters only.';
                     }
                },
                end:true,
               },
            ]}/>
        </div>
    );
}
 
export default Chat;