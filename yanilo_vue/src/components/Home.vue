<template>
  <div>
    <Header/>
    <Banner></Banner>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "./common/Header";
import Footer from "./common/Footer";
import Banner from "./common/Banner";
export default {
  name: "Home",
  components:{
    Header,Footer,Banner,
  }

}
</script>

<style scoped>

</style>
