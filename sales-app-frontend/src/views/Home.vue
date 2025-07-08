<template>
  <f7-page name="home" class="home-page">
    <f7-navbar title="Sales App" />

    <f7-block class="text-align-center intro-block">
      <h2 class="intro-title">Welcome</h2>
      <p class="intro-subtitle">Select a tool below</p>
    </f7-block>

    <f7-block class="nav-buttons">
      <f7-button fill large class="nav-button" @click="$f7router.navigate('/products/')">
        Product Info
      </f7-button>

      <f7-button fill large class="nav-button" @click="$f7router.navigate('/promotions/')">
        Promotions
      </f7-button>

      <f7-button fill large class="nav-button" @click="$f7router.navigate('/tech/')">
        Technical Info
      </f7-button>

      <f7-button fill large class="nav-button" @click="$f7router.navigate('/choose/')">
        Product Chooser
      </f7-button>

      <f7-button fill large class="nav-button" @click="$f7router.navigate('/locator/')">
        Dealer Locator
      </f7-button>
    </f7-block>
  </f7-page>
</template>

<style scoped>
.home-page {
  background-color: #f2f2f7;
}

.intro-block {
  margin-top: 32px;
  margin-bottom: 16px;
}

.intro-title {
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 4px;
  color: #1c1c1e;
}

.intro-subtitle {
  font-size: 16px;
  color: #6e6e73;
}

.nav-buttons {
  padding: 0 16px;
}

.nav-button {
  margin-bottom: 16px;
  height: 48px;
  font-size: 16px;
  font-weight: 500;
  background-color: #007aff;
  color: white;
  border-radius: 12px;
}
</style>
