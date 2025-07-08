<template>
  <f7-page name="home" class="home-page">
    <f7-navbar title="DataLog" />

    <f7-block class="welcome-block text-align-center">
      <h2 class="welcome-title">Welcome</h2>
      <p class="welcome-subtitle">Select a logging system to begin</p>
    </f7-block>

    <f7-block class="button-grid">
      <f7-row>
        <f7-col width="50">
          <f7-button fill large class="home-button larvae" @click="$emit('navigate', 'larvae')">
            <f7-icon f7="leaf_arrow_circlepath" size="32px" />
            <span>Larvae Logs</span>
          </f7-button>
        </f7-col>
        <f7-col width="50">
          <f7-button fill large class="home-button microwave" @click="$emit('navigate', 'microwave')">
            <f7-icon f7="flame" size="32px" />
            <span>Microwave Logs</span>
          </f7-button>
        </f7-col>
      </f7-row>

      <f7-row>
        <f7-col width="50">
          <f7-button fill large class="home-button prepupae" @click="$emit('navigate', 'prepupae')">
            <f7-icon f7="ant" size="32px" />
            <span>Prepupae Logs</span>
          </f7-button>
        </f7-col>
        <f7-col width="50">
          <f7-button fill large class="home-button updates" @click="$emit('navigate', 'updates')">
            <f7-icon f7="chart_bar" size="32px" />
            <span>Update Results</span>
          </f7-button>
        </f7-col>
      </f7-row>
    </f7-block>
  </f7-page>
</template>

<style scoped>
.home-page {
  background-color: #f8f8f8;
}

.welcome-block {
  margin-top: 32px;
  margin-bottom: 16px;
}

.welcome-title {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 4px;
  color: #111;
}

.welcome-subtitle {
  font-size: 16px;
  color: #666;
}

.button-grid {
  padding: 0 16px;
}

.home-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100px;
  font-size: 14px;
}

.home-button f7-icon {
  margin-bottom: 8px;
}
</style>
