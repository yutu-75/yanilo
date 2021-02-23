<template>
  <div class="cart">
    <Header></Header>
    <div class="cart-info">
        <h3 class="cart-top">购物车结算 <span>共1门课程</span></h3>
        <div class="cart-title">
           <el-row>
             <el-col :span="2">&nbsp;</el-col>
             <el-col :span="10">课程</el-col>
             <el-col :span="8">有效期</el-col>
             <el-col :span="4">价格</el-col>
           </el-row>
        </div>

        <div class="cart-item" v-for="(course,index) in course_list">
          <el-row>
             <el-col :span="2" class="checkbox">&nbsp;&nbsp;</el-col>
             <el-col :span="10" class="course-info">
               <img :src="course.course_img" alt="">
                <span>{{course.name}}</span>
             </el-col>
             <el-col :span="8"><span>{{course.expire_text}}</span></el-col>
             <el-col :span="4" class="course-price">¥{{course.real_price}}</el-col>
           </el-row>
        </div>

            <div class="discount">
          <div id="accordion">
            <div class="coupon-box">
              <div class="icon-box">
                <span class="select-coupon">使用优惠劵：</span>
                <a class="select-icon unselect" :class="use_coupon?'is_selected':''" @click="use_coupon=!use_coupon"><img class="sign is_show_select" src="../../static/img/12.png" alt=""></a>
                <span class="coupon-num">有{{coupon_list.length}}张可用</span>
              </div>
              <p class="sum-price-wrap">商品总金额：<span class="sum-price">{{total_real_price}}元</span></p>
            </div>
            <div id="collapseOne" v-if="use_coupon">
              <ul class="coupon-list"  v-if="coupon_list.length>0">
                <li class="coupon-item" :class="select_coupon(index,coupon.id)" v-for="(coupon,index) in coupon_list" @click="change_coupon(index,coupon.id)">
                  <p class="coupon-name">{{coupon.coupon.name}}</p>
                  <p class="coupon-condition">满{{coupon.coupon.condition}}元可以使用</p>
                  <p class="coupon-time start_time">开始时间：{{coupon.start_time.replace('T',' ')}}</p>
                  <p class="coupon-time end_time">过期时间：{{coupon.end_time.replace('T',' ')}}</p>
                </li>

              </ul>
              <div class="no-coupon" v-if="coupon_list.length<1">
                <span class="no-coupon-tips">暂无可用优惠券</span>
              </div>
            </div>
          </div>

          <div class="credit-box">
            <label class="my_el_check_box"><el-checkbox class="my_el_checkbox" v-model="use_credit"></el-checkbox></label>
            <p class="discount-num1" v-if="!use_credit">使用我的贝里</p>
            <p class="discount-num2" v-else><span>总积分：{{parseInt(credit)}}，
              <el-input-number v-model="num" @change="handleChange" :min="0" :max="max_credit()" label="描述文字"></el-input-number>，已抵扣 ￥{{ (num / credit_to_money).toFixed(2)}}，本次花费{{num.toFixed(2)}}积分</span></p>
          </div>



          <p class="sun-coupon-num">优惠券抵扣：<span>￥{{total_real_price-total_price}}</span></p>
        </div>








        <div class="calc">
            <el-row class="pay-row">
              <el-col :span="4" class="pay-col"><span class="pay-text">支付方式：</span></el-col>
              <el-col :span="8">
                <span class="alipay"  v-if="pay_type===1"><img src="../../static/img/alipay2.png"  alt=""></span>
                <span class="alipay" @click="pay_type=1"  v-else><img src="../../static/img/alipay.png" alt=""></span>

                <span class="alipay wechat" v-if="pay_type===2"><img src="../../static/img/wechat2.png" alt="" ></span>
                <span class="alipay wechat"  @click="pay_type=2" v-else><img src="../../static/img/wechat.png" alt=""></span>

              </el-col>
              <el-col :span="8" class="count">实付款： <span>¥{{(total_price - num/credit_to_money).toFixed(2)}}</span></el-col>
              <el-col :span="4" class="cart-pay" ><span @click="payhander">支付</span></el-col>
            </el-row>
        </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Footer from "./common/Footer"
  export default {
    name:"Order",
    data(){
      return {
        id: localStorage.id || sessionStorage.id,
        order_id:sessionStorage.order_id || null,
        course_list: [],
        coupon_list: [],
        total_price: 0,  //加上优惠券和积分计算之后的真实总价
        total_real_price: 0,
        pay_type:1,
        current_coupon:0, // 当前选中的优惠券id
        use_coupon:false,
        use_credit:false,
        coupon_obj:{},  // 当前coupon对象  {}
        num:0,
        aa:0,
        credit:0,  // 用户剩余积分
        credit_to_money:0,  //积分兑换比例
        coupon_dk:0,


      }
    },
    components:{
      Header,
      Footer,
    },
    watch:{
      use_coupon(){
        if (this.use_coupon === false){
          this.current_coupon = 0;

        }
      },

      //当选中的优惠券发生变化时，重新计算总价
      current_coupon(){
        this.cal_total_price();
      }
    }
    ,
    created(){
      this.get_order_data();
      this.get_user_coupon();
      this.get_credit();
    },
    methods: {
      max_credit(){
        let a = parseFloat(this.total_price) * parseFloat(this.credit_to_money);
        if (this.credit >= a){
          return a
        }else {
          return parseFloat(this.credit)
        }


      },
      handleChange(value){
        if (!value){
          this.num = 0
        }
        console.log(value);

      },
      get_credit(){
        this.credit = localStorage.getItem('credit') || sessionStorage.getItem('credit')
        this.credit_to_money = localStorage.getItem('credit_to_money') || sessionStorage.getItem('credit_to_money')
      },

      cal_total_price(){
        if (this.current_coupon !== 0){

          let tt = this.total_real_price;
          let sales = this.coupon_obj.coupon.sale;
          let d = parseFloat(this.coupon_obj.coupon.sale.substr(1));
          if (sales[0] === '-'){
            tt = this.total_real_price - d
            // this.total_real_price -= d
          }else if (sales[0] === '*'){
            // this.total_real_price *= d
            tt = this.total_real_price * d
          }
          this.total_price = tt;

        }

      },




      // 记录切换的couponid
      change_coupon(index,coupon_id){
        this.num=0


        let current_c = this.coupon_list[index]
        if (this.total_real_price < current_c.coupon.condition){
          return false
        }
        let current_time = new Date() / 1000;
        let s_time = new Date(current_c.start_time) / 1000
        let e_time = new Date(current_c.end_time) / 1000

        if (current_time < s_time || current_time > e_time){
          return false
        }

        this.current_coupon = coupon_id;
        this.coupon_obj = current_c;

      },

      select_coupon(index,coupon_id){
    //      {
    //     "id": 2,
    //     "start_time": "2020-11-10T09:03:00",
    //     "coupon": {
    //         "name": "五十元优惠券",
    //         "coupon_type": 1,
    //         "timer": 30,
    //         "condition": 50,
    //         "sale": "-50"
    //     },
    //     "end_time": "2020-12-10T09:03:00"
    // },
        let current_c = this.coupon_list[index]
        if (this.total_real_price < current_c.coupon.condition){
          return 'disable'
        }
        let current_time = new Date() / 1000;
        let s_time = new Date(current_c.start_time) / 1000
        let e_time = new Date(current_c.end_time) / 1000

        if (current_time < s_time || current_time > e_time){
          return 'disable'
        }

        if (this.current_coupon === coupon_id){
          return 'active'
        }

        return ''
      },

      get_order_data(){
        let token = localStorage.token || sessionStorage.token;
        this.$axios.get(`${this.$settings.Host}/cart/expires/`,{
          headers:{
              'Authorization':'jwt ' + token
            }
        }).then((res)=>{
          this.course_list = res.data.data;
          this.total_real_price = res.data.total_real_price;
          this.total_price = res.data.total_real_price;
        })
      },

      get_user_coupon(){
        let token = localStorage.token || sessionStorage.token;
        this.$axios.get(`${this.$settings.Host}/coupon/list/`,{
          headers:{
              'Authorization':'jwt ' + token
            }
        }).then((res)=>{
          this.coupon_list = res.data;
        }).catch((error)=>{
          this.$message.error('优惠券获取错误')
        })


      },
      // 支付
      payhander(){

        let token = localStorage.token || sessionStorage.token;
        this.$axios.post(`${this.$settings.Host}/order/add_money/`,{
              "pay_type":this.pay_type,
              "coupon":this.current_coupon,
              "credit":this.num,

        },{
          headers:{
              'Authorization':'jwt ' + token
            }
        }).then((res)=>{
          this.$message.success('订单已经生成，马上跳转支付页面')
          let order_number = res.data.order_number

          this.$axios.get(`${this.$settings.Host}/payment/alipay/?order_number=${order_number}`)
            .then((res)=>{
              // res.data :  alipay.trade...?a=1&b=2....
              location.href = res.data.url;

            })

        }).catch((error)=>{
          this.$message.error(error.response.data.msg);
        })



      }


    }
  }
</script>

<style scoped>

.coupon-box{
  text-align: left;
  padding-bottom: 22px;
  padding-left:30px;
  border-bottom: 1px solid #e8e8e8;
}
.coupon-box::after{
  content: "";
  display: block;
  clear: both;
}
.icon-box{
  float: left;
}
.icon-box .select-coupon{
  float: left;
  color: #666;
  font-size: 16px;
}
.icon-box::after{
  content:"";
  clear:both;
  display: block;
}
.select-icon{
  width: 20px;
  height: 20px;
  float: left;
}
.select-icon img{
  max-height:100%;
  max-width: 100%;
  margin-top: 2px;
  transform: rotate(-90deg);
  transition: transform .5s;
}
.is_show_select{
  transform: rotate(0deg)!important;
}
.coupon-num{
    height: 22px;
    line-height: 22px;
    padding: 0 5px;
    text-align: center;
    font-size: 12px;
    float: left;
    color: #fff;
    letter-spacing: .27px;
    background: #fa6240;
    border-radius: 2px;
    margin-left: 20px;
}
.sum-price-wrap{
    float: right;
    font-size: 16px;
    color: #4a4a4a;
    margin-right: 45px;
}
.sum-price-wrap .sum-price{
  font-size: 18px;
  color: #fa6240;
}

.no-coupon{
  text-align: center;
  width: 100%;
  padding: 50px 0px;
  align-items: center;
  justify-content: center; /* 文本两端对其 */
  border-bottom: 1px solid rgb(232, 232, 232);
}
.no-coupon-tips{
  font-size: 16px;
  color: #9b9b9b;
}
.credit-box{
  height: 30px;
  margin-top: 40px;
  display: flex;
  align-items: center;
  justify-content: flex-end
}
.my_el_check_box{
  position: relative;
}
.my_el_checkbox{
  margin-right: 10px;
  width: 16px;
  height: 16px;
}
.discount{
    overflow: hidden;
}
.discount-num1{
  color: #9b9b9b;
  font-size: 16px;
  margin-right: 45px;
}
.discount-num2{
  margin-right: 45px;
  font-size: 16px;
  color: #4a4a4a;
}
.sun-coupon-num{
  margin-right: 45px;
  margin-bottom:43px;
  margin-top: 40px;
  font-size: 16px;
  color: #4a4a4a;
  display: inline-block;
  float: right;
}
.sun-coupon-num span{
  font-size: 18px;
  color: #fa6240;
}
.coupon-list{
  margin: 20px 0;
}
.coupon-list::after{
  display: block;
  content:"";
  clear: both;
}
.coupon-item{
  float: left;
  margin: 15px 8px;
  width: 180px;
  height: 100px;
  padding: 5px;
  background-color: #fa3030;
  cursor: pointer;
}
.coupon-list .active{
  background-color: #fa9000;
}
.coupon-list .disable{
  cursor: not-allowed;
  background-color: #fa6060;
}
.coupon-condition{
  font-size: 12px;
  text-align: center;
  color: #fff;
}
.coupon-name{
  color: #fff;
  font-size: 24px;
  text-align: center;
}
.coupon-time{
  text-align: left;
  color: #fff;
  font-size: 12px;
}
.unselect{
  margin-left: 0px;
  transform: rotate(-90deg);
}
.is_selected{
  transform: rotate(-1turn)!important;
}
  .coupon-item p{
    margin: 0;
    padding: 0;
  }

.cart{
  margin-top: 80px;
}
.cart-info{
  overflow: hidden;
  width: 1200px;
  margin: auto;
}
.cart-top{
  font-size: 18px;
  color: #666;
  margin: 25px 0;
  font-weight: normal;
}
.cart-top span{
    font-size: 12px;
    color: #d0d0d0;
    display: inline-block;
}
.cart-title{
    background: #F7F7F7;
    height: 70px;
}
.calc{
  margin-top: 25px;
  margin-bottom: 40px;
}

.calc .count{
  text-align: right;
  margin-right: 10px;
  vertical-align: middle;
}
.calc .count span{
    font-size: 36px;
    color: #333;
}
.calc .cart-pay{
    margin-top: 5px;
    width: 110px;
    height: 38px;
    outline: none;
    border: none;
    color: #fff;
    line-height: 38px;
    background: #ffc210;
    border-radius: 4px;
    font-size: 16px;
    text-align: center;
    cursor: pointer;
}
.cart-item{
  height: 120px;
  line-height: 120px;
  margin-bottom: 30px;
}
.course-info img{
    width: 175px;
    height: 115px;
    margin-right: 35px;
    vertical-align: middle;
}
.alipay{
  display: inline-block;
  height: 48px;
}
.alipay img{
  height: 100%;
  width:auto;
}

.pay-text{
  display: block;
  text-align: right;
  height: 100%;
  line-height: 100%;
  vertical-align: middle;
  margin-top: 20px;
}
</style>
