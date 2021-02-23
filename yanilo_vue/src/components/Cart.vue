<template>
    <div class="cart">
      <Header></Header>
     <div class="cart_info">
        <div class="cart_title">
          <span class="text">我的购物车</span>
          <span class="total">共4门课程</span>
        </div>
        <div class="cart_table">
          <div class="cart_head_row">
            <span class="doing_row"></span>
            <span class="course_row">课程</span>
            <span class="expire_row">有效期</span>
            <span class="price_row">单价</span>
            <span class="do_more">操作</span>
          </div>
          <div class="cart_course_list">
            <CartItem v-for="(value,index) in cart_data_list" :key="index" :cart="value" @cal_t_p="cal_total_price" @change_expire_handler="cal_total_price" @delete_course_handler="delete_c(index)"></CartItem>

          </div>
          <div class="cart_footer_row">
            <span class="cart_select"><label> <el-checkbox v-model="checked"></el-checkbox><span>全选</span></label></span>
            <span class="cart_delete"><i class="el-icon-delete"></i> <span>删除</span></span>
            <router-link to="/order/"><span class="goto_pay">去结算</span></router-link>
            <span class="cart_total">总计：¥{{total_price}}</span>
          </div>
        </div>
      </div>
      <Footer></Footer>
    </div>
</template>

<script>
import Header from "./common/Header"
import Footer from "./common/Footer"
import CartItem from "./common/CartItem"
export default {
    name: "Cart",
    data(){
      return {
        checked: false,
        total_price:0,
        cart_data_list:[],
      }
    },
    methods:{
      cal_total_price(){
        // {
        //     "name": "flask框架",
        //     "course_img": "http://www.lyapi.com:8001/media/course/course-cover.jpeg",
        //     "price": 1110.0,
        //     "real_price": 0,
        //     "expire_id": "0",
        //     'selected':true,
        // }
        // {
        //     "name": "flask框架",
        //     "course_img": "http://www.lyapi.com:8001/media/course/course-cover.jpeg",
        //     "price": 1110.0,
        //     "real_price": 0,
        //     "expire_id": "0",
        //     'selected':false,
        // }
        let t_price = 0
        this.cart_data_list.forEach((v,k)=>{
          if (v.selected){
            t_price += v.real_price
          }
        })
        console.log('total_price>>>>',t_price)
        this.total_price = t_price

      },
      delete_c(index){
        this.cart_data_list.splice(index,1)
        this.cal_total_price()
      }
    },
  created() {
    let token = sessionStorage.token || localStorage.token;
    if (token){

      this.$axios.get(`${this.$settings.Host}/cart/add_cart/`,{
         headers:{
                'Authorization':'jwt ' + token
              }
      })
      .then((res)=>{
        this.cart_data_list = res.data.cart_data_list
      })
      .catch((error)=>{
        this.$message.error(error.response.data.msg);
      })




    }else {
      this.$router.push('/user/login');
    }


  },
  components:{
      Header,
      Footer,
      CartItem,
    }
}
</script>

<style scoped>
.cart_info{
  width: 1200px;
  margin: 0 auto 50px;
}
.cart_title{
  margin: 25px 0;
}
.cart_title .text{
  font-size: 18px;
  color: #666;
}
.cart_title .total{
  font-size: 12px;
  color: #d0d0d0;
}
.cart_table{
  width: 1170px;
}
.cart_table .cart_head_row{
  background: #F7F7F7;
  width: 100%;
  height: 80px;
  line-height: 80px;
  padding-right: 30px;
}
.cart_table .cart_head_row::after{
  content: "";
  display: block;
  clear: both;
}
.cart_table .cart_head_row .doing_row,
.cart_table .cart_head_row .course_row,
.cart_table .cart_head_row .expire_row,
.cart_table .cart_head_row .price_row,
.cart_table .cart_head_row .do_more{
  padding-left: 10px;
  height: 80px;
  float: left;
}
.cart_table .cart_head_row .doing_row{
  width: 78px;
}
.cart_table .cart_head_row .course_row{
  width: 530px;
}
.cart_table .cart_head_row .expire_row{
  width: 188px;
}
.cart_table .cart_head_row .price_row{
  width: 162px;
}
.cart_table .cart_head_row .do_more{
  width: 162px;
}

.cart_footer_row{
  padding-left: 36px;
  background: #F7F7F7;
  width: 100%;
  height: 80px;
  line-height: 80px;
}
.cart_footer_row .cart_select span{
  margin-left: 14px;
  font-size: 18px;
  color: #666;
}
.cart_footer_row .cart_delete{
  margin-left: 58px;
}
.cart_delete .el-icon-delete{
  font-size: 18px;
}

.cart_delete span{
  margin-left: 15px;
  cursor: pointer;
  font-size: 18px;
  color: #666;
}
.cart_total{
  float: right;
  margin-right: 62px;
  font-size: 18px;
  color: #666;
}
.goto_pay{
  float: right;
  width: 159px;
  height: 80px;
  outline: none;
  border: none;
  background: #ffc210;
  font-size: 18px;
  color: #fff;
  text-align: center;
  cursor: pointer;
}
</style>

