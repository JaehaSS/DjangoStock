<template>
  <div>
    <GChart
      type="CandlestickChart"
      :data="chartData"
      :options="chartOptions"
      @ready="onChartReady"
    />
  </div>
</template>

<script>
import { GChart } from "vue-google-charts";
export default {
  components: {
    GChart
  },
  data() {
    return {
      chartData: [
        ["이건", "월", "화", "수", "목"],
        ['Mon', 20, 28, 38, 45],
        ['Tue', 31, 38, 55, 66],
        ['Wed', 50, 55, 77, 80],
        ['Thu', 77, 77, 66, 50],
        ['Fri', 68, 66, 22, 15],
        ["102", 22, 25, 22, 25],
      ],


      // the chartData will be created once Chart is ready (needs google charts lib for this)
      chartOptions: {
        title: 'Candlestick, default',
        curveType: 'function',
        lineWidth: 4,
        intervals: { 'style': 'line' },
        legend: 'none',
        backgroundColor: 'white',
        backgroundColorstroke : '#477',

      }
    };
  },

  methods: {
    onChartReady (chart, google) {
      // now we have google lib loaded. Let's create data table based using it.
      this.createDataTable(google)
    },
    createDataTable(google) {
      const data = new google.visualization.DataTable([
        ['Mon', 20, 28, 38, 45],
        ['Tue', 31, 38, 55, 66],
        ['Wed', 50, 55, 77, 80],
        ['Thu', 77, 77, 66, 50],
        ['Fri', 68, 66, 22, 15]
      ],true);


      // Since the :data is reactive, we just need to update it's value
      this.chartData = data;

    }
  }
};
</script>
