export default {
  Host:"http://api.yanilo.top:8000",// server address
    check_login(ths){
      let token = localStorage.token || sessionStorage.token;
      //console.log(this.token);
      console.log('>>>>>',token);
      //console.log('>>>>>',ths.$axios);
      ths.$axios.post(`${this.Host}/users/verify/`,{
        token:token,
      }).then((res)=>{
        //console.log('xxxxxxxxxxxxxxxxxxxxxxx')

        ths.token = token;
        // return 值拿不到。。。

      }).catch((error)=>{
        //console.log(error)
        //.log('ssssssssssssssssssssss')
        ths.token = false;
      })

    }



}

