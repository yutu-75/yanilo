<template>

<div class="footer">
  <div>
<hr align="center" width='1000px'  />
  </div>


      <div class="footer-item">
        <div class="foot-left">
        <div class="foot-content">
          <p>
            <span>关于我们</span>
            &nbsp;&nbsp;|&nbsp;&nbsp;
            <span>yanilo杂货铺</span>
          </p>
          <p>
            地址：xx市xx地区xx号  邮箱：xiao3952@foxmail.com
          </p>
          <p>
             © 2017-2020 yanilo
            <a class="copyright" href="http://beian.miit.gov.cn" target="_blank" >渝ICP备19017372号-2</a>
          </p>
          <p>
            <a class="report-link" target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102002019&amp;token=1ee3034d-ba3a-4cc3-89d4-89875e2dd0b1">
              <img class="report-img" src="//img.alicdn.com/tfs/TB1..50QpXXXXX7XpXXXXXXXXXX-40-40.png" style="float:left" >
              渝公网安备 11010102002020号
            </a>
          </p>
        </div>

      </div>
        <img src="@/assets/code.png" alt="" class="code">
      </div>
    </div>
</template>

<script>
export default {
name: "Footer"
}
</script>

<style scoped>

  .footer{
    display: flex;
    align-items: center;
    width: 100%;
    height: 150px;
    flex-direction: column;
    overflow: hidden;
    /*background: #191c25;*/
  }
  .footer .foot-left{
    display: flex;
    align-items: center;
  }
  .footer .foot-left .foot-content p{
    margin-bottom: 10px;
    font-size: 13px;
    font-family: PingFangSC-Regular;
    font-weight: 400;
    color: rgba(90,104,139,0.64);
  }
  .footer-item{
    width: 960px;
    height: 100%;
    justify-content: space-between;
  }
  .foot-left{
    display: flex;
    align-items: center;
    float: left;
  }
  .foot-content a{
    color: rgba(93,202,205,0.67);
    text-decoration: none;
  }
  .footer .foot-left .foot-content p:first-child span{
    font-size: 16px;
    font-weight: 400;
    display: inline-block;
    font-family: PingFangSC-Regular;
    cursor: pointer;
  }
  .foot-content .report-img{
    display: inline-block;
    height: 20px;
    margin-right: 12px;
  }
  .footer-item .code{
    width: 74px;
    height: auto;
    margin-right: 100px;
    float: right;
    padding-top: 30px;
  }

</style>
