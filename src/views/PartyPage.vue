<template>
  <!-- HomePage -->
  <div class="container">
    <TopMenu />
    <!-- 将 selectedYear 作为 props 传递给 VotesMap -->
    <PartyMap :selectedYear="selectedYear" />
    <div id="timeline" style="width: 100%; height: 100px; margin-top: auto;"></div> <!-- 时间轴容器 -->
  </div>
</template>

<script>
import TopMenu from '@/components/TopMenu.vue';
import PartyMap from '@/components/PartyMap.vue';
import * as echarts from 'echarts';

export default {
  name: 'VotesPage',
  components: {
    TopMenu,
    PartyMap
  },
  data() {
    return {
      selectedYear: '1976', // 默认选择1976年
    };
  },
  mounted() {
    // 初始化时间轴
    this.initTimeline();
  },
  methods: {
    initTimeline() {
      const timeline = echarts.init(document.getElementById('timeline'));

      // 配置时间轴
      timeline.setOption({
        timeline: {
          axisType: 'category',
          autoPlay: true, // 自动播放
          playInterval: 1000, // 播放间隔
          data: ['1976', '1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012', '2016', '2020'],
          label: {
            formatter: '{value}年',
          },
          symbolSize: 10,
          lineStyle: {
            color: '#a6a6a6',
            width: 2
          },
          checkpointStyle: {
            symbol: 'circle',
            symbolSize: 10,
            color: '#ff6600',
            borderColor: '#ffffff',
            borderWidth: 2,
          },
          controlStyle: {
            showNextBtn: false,
            showPrevBtn: false
          },
        },
        options: [
          { title: { text: '1976年选举' } },
          { title: { text: '1980年选举' } },
          { title: { text: '1984年选举' } },
          { title: { text: '1988年选举' } },
          { title: { text: '1992年选举' } },
          { title: { text: '1996年选举' } },
          { title: { text: '2000年选举' } },
          { title: { text: '2004年选举' } },
          { title: { text: '2008年选举' } },
          { title: { text: '2012年选举' } },
          { title: { text: '2016年选举' } },
          { title: { text: '2020年选举' } },
        ]
      });

      // 添加事件监听，监听时间轴的变化
      timeline.on('timelineChanged', (params) => {
        // 获取选中的年份
        const selectedYear = params.currentIndex;
        // 更新选中的年份
        this.selectedYear = ['1976', '1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012', '2016', '2020'][selectedYear];
      });
    }
  }
};
</script>

<style scoped>
/* 使用Flexbox布局容器 */
.container {
  display: flex;
  flex-direction: column; /* 垂直排列 */
  height: 100vh; /* 充满整个视口高度 */
}

#timeline {
  margin-top: auto; 
}
</style>
