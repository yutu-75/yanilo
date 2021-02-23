<template>
	<div class="login box">
<div class="container" id="container">
	<div class="form-container sign-up-container">
		<form action="#">
			<h1>Create Account</h1>
			<div class="social-container">
				<a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
				<a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
				<a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
			</div>
			<span>or use your email for registration</span>
			<input type="text" placeholder="Name" />
			<input type="email" placeholder="Email" />
			<input type="password" placeholder="Password" />
			<button>注 册</button>
		</form>
	</div>
	<div class="form-container sign-in-container">
		<form action="#">
			<h1>Sign in</h1>
			<div class="social-container">
				<a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
				<a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
				<a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
			</div>
			<span>or use your account</span>
			<input v-model = "Email" type="email" placeholder="Email" />
			<input v-model="password" type="password" placeholder="Password" />
			<a href="" style="color: rgba(87,114,135,0.79)">忘记密码?</a>
			<button @click="login">登 录</button>
		</form>
	</div>
	<div class="overlay-container">
		<div class="overlay">
			<div class="overlay-panel overlay-left">
				<h1>Welcome Back!</h1>
				<p>To keep connected with us please login with your personal info</p>
				<button class="ghost" id="signIn">登 录</button>
			</div>
			<div class="overlay-panel overlay-right">
				<h1>Hello, Friend!</h1>
				<p> 输入您的个人详细信息并与我们一起开始旅程 ！</p>
				<button class="ghost" @click="register_show" id="signUp">注 册</button>
			</div>
		</div>
	</div>
</div>

<footer>
	<p>
		Created with <i class="fa fa-heart"></i> by
		<a target="_blank" href="https://florin-pop.com">Florin Pop</a>
		- Read how I created this and how you can join the challenge
		<a target="_blank" href="https://www.florin-pop.com/blog/2019/03/double-slider-sign-in-up-form/">here</a>.
	</p>
</footer>

	</div>
</template>

<script>
export default {
  name: 'Login',
  data(){
    return {
        Email:"",
        login_type: 0,
        username:"",
        password:"",
        remember:false
    }
  },
  created(){
  },
  methods:{
    register(){

    },

    login(){

    },
    register_show(){
    const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');
      container.classList.add("right-panel-active");
    signUpButton.addEventListener('click', () => {
      container.classList.add("right-panel-active");
    });

    signInButton.addEventListener('click', () => {
      container.classList.remove("right-panel-active");
    });
    },




    xx(){
      alert('xxxxx')
    },
    LoginHandle(){
      var captcha1 = new TencentCaptcha('2033693254', (res) =>{
                if (res.ret === 0){
          console.log(res.randstr);
          console.log(res.ticket);


          this.$axios.post(`${this.$settings.Host}/users/login/`,{
            username:this.username,
            password:this.password,
            ticket:res.ticket,
            randstr:res.randstr,

          }).then((res)=>{
            console.log(res);
            // console.log(this.remember);
            if (this.remember){
              localStorage.token = res.data.token;
              localStorage.username = res.data.username;
              localStorage.id = res.data.id;
              localStorage.credit = res.data.credit;
              localStorage.credit_to_money = re.data.credit_to_money;
              sessionStorage.removeItem('token');
              sessionStorage.removeItem('username');
              sessionStorage.removeItem('id');
              sessionStorage.removeItem('credit');
              sessionStorage.removeItem('credit_to_money');


            }else {
              console.log('xxxxxxxxxxx')
              console.log(res.data)
              sessionStorage.token = res.data.token;
              sessionStorage.username = res.data.username;
              sessionStorage.id = res.data.id;
              sessionStorage.credit = res.data.credit;
              sessionStorage.credit_to_money = res.data.credit_to_money;
              localStorage.removeItem('token');
              localStorage.removeItem('username');
              localStorage.removeItem('id');
              localStorage.removeItem("credit");
              localStorage.removeItem("credit_to_money");
            }

            this.$confirm('下一步想去哪消费！', '提示', {
                confirmButtonText: '去首页',
                cancelButtonText: '去上一个界面',
                type: 'success'
              }).then(() => {
                this.$router.push('/');
              }).catch(() => {
                this.$router.go(-1);
              });


          }).catch((error)=>{
            this.$alert('用户名或者密码错误', '登录失败', {
              confirmButtonText: '确定',

            });
          })
        }
      });
      captcha1.show(); // 显示验证码
      // this.$axios.post(`${this.$settings.Host}/users/login/`,{
      //   username:this.username,
      //   password:this.password,
      //
      //
      // }).then((res)=>{
      //   console.log(res)
      //   if(this.remember){
      //     localStorage.token = res.data.token;
      //     localStorage.username = res.data.username;
      //     localStorage.id = res.data.id;
      //     sessionStorage.removeItem('token');
      //     sessionStorage.removeItem('username');
      //     sessionStorage.removeItem('id');
      //
      //   }else {
      //     sessionStorage.token = res.data.token;
      //     sessionStorage.username = res.data.username;
      //     sessionStorage.id = res.data.id;
      //     //localStorage.clear()//清除全局
      //     localStorage.removeItem('token');//
      //     localStorage.removeItem('username');//
      //     localStorage.removeItem('id');//
      //   }
      //    this.$router.push('/');
      // }).catch((error)=>{
      //   this.$alert('用户名password error', 'error msg', {
      //     confirmButtonText: '确定',
      //   });
      // })
    }

  },

};
</script>

<style>

@import url('https://fonts.googleapis.com/css?family=Montserrat:400,800');

* {
	box-sizing: border-box;
}

body {
	background: #f6f5f7;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
	font-family: 'Montserrat', sans-serif;
	height: 100vh;
	margin: -20px 0 50px;
}

h1 {
	font-weight: bold;
	margin: 0;
}

h2 {
	text-align: center;
}

p {
	font-size: 14px;
	font-weight: 100;
	line-height: 20px;
	letter-spacing: 0.5px;
	margin: 20px 0 30px;
}

span {
	font-size: 12px;
}

a {
	color: #333;
	font-size: 14px;
	text-decoration: none;
	margin: 15px 0;
}

button {
	border-radius: 20px;
	border: 1px solid #FF4B2B;
	background-color: #FF4B2B;
	color: #FFFFFF;
	font-size: 12px;
	font-weight: bold;
	padding: 12px 45px;
	letter-spacing: 1px;
	text-transform: uppercase;
	transition: transform 80ms ease-in;
}

button:active {
	transform: scale(0.95);
}

button:focus {
	outline: none;
}

button.ghost {
	background-color: transparent;
	border-color: #FFFFFF;
}

form {
	background-color: #FFFFFF;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 0 50px;
	height: 100%;
	text-align: center;
}

input {
	background-color: #eee;
	border: none;
	padding: 12px 15px;
	margin: 8px 0;
	width: 100%;
}

.container {
	background-color: #fff;
	border-radius: 10px;
  	box-shadow: 0 14px 28px rgba(0,0,0,0.25),
			0 10px 10px rgba(0,0,0,0.22);
	position: relative;
	overflow: hidden;
	width: 768px;
	max-width: 100%;
	min-height: 480px;
}

.form-container {
	position: absolute;
	top: 0;
	height: 100%;
	transition: all 0.6s ease-in-out;
}

.sign-in-container {
	left: 0;
	width: 50%;
	z-index: 2;
}

.container.right-panel-active .sign-in-container {
	transform: translateX(100%);
}

.sign-up-container {
	left: 0;
	width: 50%;
	opacity: 0;
	z-index: 1;
}

.container.right-panel-active .sign-up-container {
	transform: translateX(100%);
	opacity: 1;
	z-index: 5;
	animation: show 0.6s;
}

@keyframes show {
	0%, 49.99% {
		opacity: 0;
		z-index: 1;
	}

	50%, 100% {
		opacity: 1;
		z-index: 5;
	}
}

.overlay-container {
	position: absolute;
	top: 0;
	left: 50%;
	width: 50%;
	height: 100%;
	overflow: hidden;
	transition: transform 0.6s ease-in-out;
	z-index: 100;
}

.container.right-panel-active .overlay-container{
	transform: translateX(-100%);
}

.overlay {
	background: #FF416C;
	background: -webkit-linear-gradient(to right, #FF4B2B, #FF416C);
	background: linear-gradient(to right, #FF4B2B, #FF416C);
	background-repeat: no-repeat;
	background-size: cover;
	background-position: 0 0;
	color: #FFFFFF;
	position: relative;
	left: -100%;
	height: 100%;
	width: 200%;
  	transform: translateX(0);
	transition: transform 0.6s ease-in-out;
}

.container.right-panel-active .overlay {
  	transform: translateX(50%);
}

.overlay-panel {
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 0 40px;
	text-align: center;
	top: 0;
	height: 100%;
	width: 50%;
	transform: translateX(0);
	transition: transform 0.6s ease-in-out;
}

.overlay-left {
	transform: translateX(-20%);
}

.container.right-panel-active .overlay-left {
	transform: translateX(0);
}

.overlay-right {
	right: 0;
	transform: translateX(0);
}

.container.right-panel-active .overlay-right {
	transform: translateX(20%);
}

.social-container {
	margin: 20px 0;
}

.social-container a {
	border: 1px solid #DDDDDD;
	border-radius: 50%;
	display: inline-flex;
	justify-content: center;
	align-items: center;
	margin: 0 5px;
	height: 40px;
	width: 40px;
}

footer {
    background-color: #222;
    color: #fff;
    font-size: 14px;
    bottom: 0;
    position: fixed;
    left: 0;
    right: 0;
    text-align: center;
    z-index: 999;
}

footer p {
    margin: 10px 0;
}

footer i {
    color: red;
}

footer a {
    color: #3c97bf;
    text-decoration: none;
}
</style>

