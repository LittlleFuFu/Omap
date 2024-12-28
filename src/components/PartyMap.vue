<template>
  <!-- VotesMap -->
  <div id="main" style="width: 100%; height: 100vh;"></div> <!-- 地图容器 -->
</template>

<script>
// 引入 ECharts
import * as echarts from 'echarts';
import usaData from './USA.geojson'; // 导入GeoJSON文件

export default {
  name: 'VotesMap',
  props: {
    selectedYear: {
      type: String,
      required: true
    }
  },
  watch: {
    // 监听年份的变化
    selectedYear(newYear) {
      this.updateMapData(newYear);
    }
  },
  mounted() {
    // 注册 GeoJSON 数据
    echarts.registerMap('USA', usaData, {
    Alaska: {
      left: -131,
      top: 25,
      width: 15
    },
    Hawaii: {
      left: -110,
      top: 25,
      width: 5
    },
    'Puerto Rico': {
      left: -76,
      top: 26,
      width: 2
    }
  }); // 注册地图数据
    this.chart = echarts.init(document.getElementById('main'));

    // 提取所有年份的投票数据
    this.voteData = this.getVoteData();

    // 默认使用1976年的数据
    this.updateMapData(this.selectedYear);
  },
  methods: {
    getVoteData() {
      // 提取每个年份的投票数据
      const data = {};
      const years = ['1976', '1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012', '2016', '2020'];
      years.forEach(year => {
        data[year] = usaData.features.map(feature => ({
          name: feature.properties.name, // 区域名称
          value: feature.properties[`party_simplified_${year}`], // 每年对应的投票数
          
          candidate: feature.properties[`candidate_${year}`], // 候选人
          party: feature.properties[`party_simplified_${year}`] // 政党
        }));
      });
      return data;
    },
    updateMapData(year) {
      const yearData = this.voteData[year];
      const maxVotes = Math.max(...yearData.map(item => item.value));
      const minVotes = Math.min(...yearData.map(item => item.value));

      // 设置地图的配置项
      this.chart.setOption({
        tooltip: {
          trigger: 'item',
          formatter: (params) => {
            const { name, candidate, party } = params.data;
            
            // 根据party的值显示对应政党
            let partyName = '';
            if (party === '1') {
              partyName = 'Democrat';  // 显示民主党
            } else if (party === '-1') {
              partyName = 'Republican'; // 显示共和党
            } else {
              partyName = 'Other';      // 其他情况显示其他
            }

            return `${name}<br />Candidate: ${candidate}<br />Party: ${partyName}`;
          } // 显示区域名称、候选人、党派
        },
        geo: {
          type: 'map',
          map: 'USA', // 选择地图
          roam: false, // 启用缩放和平移
          itemStyle: {
            normal: {
              areaColor: '#eeeeee', // 区域填充颜色
              borderColor: '#111', // 区域边框颜色
              borderWidth: 2,
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
            color: ['#d13438', '#0078d4'] // 颜色渐变（从白到红）
          },
          text: ['High', 'Low'], // 可视化图例
          show: false
        },
        series: [
          {
            name: `${year}年选举`,
            type: 'map',
            geoIndex: 0, // 使用第一个 geo 配置
            data: yearData
          }
        ]
      });
    }
  }
};
</script>

<style scoped>
#main {
  width: 100%;
  height: 100%;
  margin-top: 8%;
}
</style>
