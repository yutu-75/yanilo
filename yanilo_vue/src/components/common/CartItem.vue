<template>
    <div class="cart_item">
      <div class="cart_column column_1">

        <el-checkbox class="my_el_checkbox" v-model="cart.selected"></el-checkbox>
      </div>

      <div class="cart_column column_2">
        <img :src="cart.course_img" alt="">
        <span><router-link to="/course/detail/1">{{cart.name}}</router-link></span>

      </div>
      <div class="cart_column column_3">
        <el-select v-model="cart.expire_id" size="mini" placeholder="请选择购买有效期" class="my_el_select">
          <el-option :label="expire.expire_text" :value="expire.id" :key="expire.id" v-for="(expire,expire_index) in cart.expire_list"></el-option>

        </el-select>
      </div>
      <div class="cart_column column_4">¥{{cart.real_price}}</div>
      <div class="cart_column column_4" id="delete" @click="delete_course">删除</div>
    </div>
</template>

<script>
export default {
    name: "CartItem",
    data(){
      return {
        // checked:false,

      }
    },
    props:['cart', ],
    watch:{

      'cart.selected':function (){
        // 添加选中
        let token = localStorage.token || sessionStorage.token;
        if (this.cart.selected){
          this.$axios.patch(`${this.$settings.Host}/cart/add_cart/`,{
            course_id: this.cart.course_id,

          },{
            headers:{
              'Authorization':'jwt ' + token
            }
          }).then((res)=>{
            this.$message.success(res.data.msg);
            this.$emit('cal_t_p')
          }).catch((error)=>{
            this.$message.error(res.data.msg);
          })
        }
        else {
          // 取消选中
          this.$axios.put(`${this.$settings.Host}/cart/add_cart/`,{
            course_id: this.cart.course_id,

          },{
            headers:{
              'Authorization':'jwt ' + token
            }
          }).then((res)=>{
            this.$message.success(res.data.msg);
            this.$emit('cal_t_p')
          }).catch((error)=>{
            this.$message.error(res.data.msg);
          })
        }
      },

      'cart.expire_id':function (){
        let token = localStorage.token || sessionStorage.token;

          this.$axios.put(`${this.$settings.Host}/cart/expires/`,{
            course_id: this.cart.course_id,
            expire_id:this.cart.expire_id,
          },{
            headers:{
              'Authorization':'jwt ' + token
            }

      }
      ).then((res)=>{
        this.$message.success(res.data.msg);
        // console.log('>>>>', res.data.real_price)
        this.cart.real_price = res.data.real_price;

        this.$emit('change_expire_handler',)

          }).catch((error)=>{
            this.$message.error(error.response.data.msg)
          })
    }
},
  methods:{
      delete_course(){
        let token = localStorage.token || sessionStorage.token;

          this.$axios.delete(`${this.$settings.Host}/cart/add_cart/`,{
            params:{
              course_id: this.cart.course_id,  // request.query_params.get('course_id')
            },
            headers:{
              'Authorization':'jwt ' + token
            }
          })
        .then((res)=>{
          this.$message.success(res.data.msg);
          this.$store.commit('add_cart', res.data.cart_length) ;
          this.$emit('delete_course_handler')

        })
        .catch((error)=>{
          this.$message.error(error.response.data.msg);
        })
      }
  }
}


</script>


<style scoped>

#delete{
  cursor: pointer;
}
  /*.cart_item{*/
  /*  height: 100px;*/
  /*}*/
.cart_item::after{
  content: "";
  display: block;
  clear: both;
}
.cart_column{
  float: left;
  height: 150px;
  display: flex;
  align-items: center;
}
.cart_item .column_1{
  width: 88px;
  position: relative;
}
.my_el_checkbox{
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  margin: auto;
  width: 16px;
  height: 16px;
}
.cart_item .column_2 {
  /*padding: 67px 10px;*/
  width: 520px;
  /*height: 116px;*/
}
.cart_item .column_2 img{
  width: 175px;
  /*height: 115px;*/
  margin-right: 35px;
  /*vertical-align: middle;*/
}
.cart_item .column_3{
  width: 197px;
  position: relative;
  padding-left: 10px;
}
.my_el_select{
  width: 117px;
  height: 28px;
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto;
}
.cart_item .column_4{
  /*padding: 67px 10px;*/
  /*height: 116px;*/
  width: 142px;
  /*line-height: 116px;*/
}

</style>
