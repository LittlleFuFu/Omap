<template>
  <!-- VotesMap -->
  <div id="main" style="width: 100%; height: 100vh;"></div> <!-- 地图容器 -->
</template>

<script>
// 引入 ECharts
import * as echarts from 'echarts';
import usaData from './USA.geojson'; // 导入GeoJSON文件

export default {
  name: 'RouteMap',
  mounted() {
    // 注册 GeoJSON 数据
    echarts.registerMap('USA', usaData); // 注册地图数据

    // 提取 GeoJSON 数据中的属性 candidatevotes_1976，并计算最大最小值
    const maxVotes = Math.max(...usaData.features.map(feature => feature.properties.candidatevotes_1976));
    const minVotes = Math.min(...usaData.features.map(feature => feature.properties.candidatevotes_1976));

    // 初始化 ECharts 图表
    const chart = echarts.init(document.getElementById('main'));

    // 设置地图的配置项
    chart.setOption({
      tooltip: {
        trigger: 'item',
        formatter: '{b}<br />Votes: {c}' // 显示区域名称和候选人投票数
      },
      geo: {
        type: 'map',
        map: 'USA', // 选择地图
        roam: false, // 启用缩放和平移
        itemStyle: {
          normal: {
            areaColor: '#eeeeee', // 区域填充颜色
            borderColor: '#111' // 区域边框颜色
          },
          emphasis: {
            areaColor: '#ffcc33' // 高亮区域颜色
          }
        }
      },
      visualMap: {
        min: minVotes,
        max: maxVotes,
        calculable: true, // 允许拖动调节范围
        inRange: {
          color: ['#ffffff', '#ff0000'] // 颜色渐变（从白到红）
        },
        text: ['High', 'Low'], // 可视化图例
        show: true
      },
      series: [
        {
          name: 'USA Map',
          type: 'map',
          geoIndex: 0, // 使用第一个 geo 配置
          data: usaData.features.map(feature => ({
            name: feature.properties.name, // 区域名称
            value: feature.properties.candidatevotes_1976 // 区域的投票数
          }))
        }
      ]
    });
  }
};
</script>

<style scoped>
/* 简单设置地图容器的样式 */
#main {
  width: 100%;
  height: 100%;
  margin-top: 5%;
}
</style>
