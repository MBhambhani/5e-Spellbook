<template>
  <v-toolbar app clipped-left flat class="title-background">
    <v-btn text icon @click="handleMenuClick()">
      <v-icon color="white">menu</v-icon>
    </v-btn>
    <v-toolbar-title class="title-text">Larrel's Tome</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn flat><span class="title-text">Register/Log in</span></v-btn>
  </v-toolbar>
</template>

<script>
export default {
  name: 'Toolbar',
  methods: {
    handleMenuClick() {
      this.$emit('toggle-drawer');
    },
  },
};
</script>

<style>
.title-text {
  color:white;
}
.title-background {
  background-color:#342e37 !important;
}
</style>
