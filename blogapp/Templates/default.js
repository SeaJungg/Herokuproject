var doc = document;
var button = doc.getElementById("btn").addEventListener('click', function(){
    Login();
});

function Login(){
            var form = doc.form1;
            var IDRule = /^[A-za-z]{8,20}/g;
            var PWRule = /^[A-za-z0-9]{8,20}/g;
            if(form.txtID.value == ""){
                alert("아이디를 입력하세요.");
                name.focus();
                return;
            }

            if(form.txtPwd.value == ""){
                alert("패스워드를 입력하세요.");
                name.focus();
                return;
            }
            
            if(form.txtPwd2.value == ""){
                alert("확인패스워드을 입력하세요.");
                name.focus();
                return;
            }
            
        
            if(!IDRule.test(form.txtID.value)){
                alert("입력한 아이디가 조건에 맞지 않아요. 아이디는 영문으로 시작하는 8~20자의 영문 혹은 숫자여야 해요.");
                return;
            }

            if(!PWRule.test(form.txtPwd.value)){
                alert(form.txtPwd.value+"입력한 비밀번호가 조건에 맞지 않아요. 비밀번호는 영문으로 시작하는 8~20자의 영문 혹은 숫자여야 해요.");
                return;
            }

            if(form.txtPwd.value != form.txtPwd2.value){
                alert("확인용 비밀번호가 서로 일치하지 않아요.")
                return;
            }

            alert("회원가입이 완료되었어요 :) ")
            form.submit();
}