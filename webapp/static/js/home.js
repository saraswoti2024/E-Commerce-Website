const input = document.querySelector("#phone");
const error_msg = document.getElementById("error_msg")
const va = window.intlTelInput(input, {
  initialCountry: "us",
  strictMode: true,
  loadUtils: () => import("https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/25.2.1/build/js/utils.js") // for formatting/placeholders etc

});

document.getElementById('ContactForm').addEventListener('submit',function(e){
    if(va.isValidNumber()){
        input.value = va.getNumber();
        error_msg.style.display='none';
    }
    else{
        e.preventDefault();
        error_msg.style.display="inline";
    }
})