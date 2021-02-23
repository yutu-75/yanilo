<template>
  <div id="app">

    <router-view/>
  </div>


</template>

<script>
export default {
  name: 'App',
  created() {
    window.addEventListener('beforeunload', () => {
      console.log('页面要刷新啦！！！,赶紧保存数据！！！！');
      sessionStorage.setItem('cart_length', this.$store.state.cart_length);


    })
  }
}
</script>

<style>

</style>
<!--<style>-->

<!--/*浮动小人的css*/-->
<!--.img{-->
<!--    height: 200px;-->
<!--    width: 200px;-->
<!--    background-image: url("./assets/sleep.png");-->
<!--    background-size: 100%;-->
<!--    background-position-x: initial;-->
<!--    background-position-y: initial;-->
<!--    background-attachment: initial;-->
<!--    background-origin: initial;-->
<!--    background-clip: initial;-->
<!--}-->
<!--#spig{-->
<!--    height: 200px;-->
<!--    width: 200px;-->
<!--    display: block;-->
<!--    position: absolute;-->
<!--    bottom: 300px;-->
<!--    left: 160px;-->
<!--    z-index: 9999;-->
<!--}-->
<!--#message{-->

<!--    text-align:center !important;-->


<!--    font: 15px arial,sans-serif;-->

<!--    background-color: rgba(61, 73, 94, 0.09);-->
<!--    border:1px  #74dff1;  /*同时设置边框大小 样式 颜色*/-->
<!--    border-radius: 10px;-->
<!--    box-shadow: darkgrey 1px 1px;-->


<!--}-->

<!--/*固定位置*/-->
<!--.c1{-->
<!--  background-color: red;-->
<!--  height: 800px;-->

<!--}-->
<!--.c2{-->
<!--  background-color: blue;-->
<!--  height: 800px;-->
<!--}-->
<!--.c3{-->
<!--  /* 相对于浏览器窗口来设置位置 */-->
<!--  position: fixed;-->
<!--  right:40px;-->
<!--  bottom: 200px;-->
<!--  height: 35px;-->
<!--  width: 35px;-->
<!--  /*background: url("icon.jpg");*/-->
<!--  /*background-size: cover;   !*把背景图片变成自适应大小*!*/-->


<!--}-->
<!--.above{-->
<!--  height:35px;-->
<!--  width: 35px;-->
<!--  transition: linear 0.3s;  /*设置旋转的时间*/-->
<!--}-->
<!--.above:hover{-->
<!--    transform: rotate(720deg);-->
<!--  /*transform: scale(1.5) rotate(720deg);!*设置 缩放大小 旋转的度数*!*/-->
<!--}-->
<!--.c3 a{-->

<!--  text-decoration: none;-->
<!--  color:black;-->

<!--}-->

<!--</style>-->
