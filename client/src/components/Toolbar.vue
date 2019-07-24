<template>
  <v-toolbar app clipped-left flat color="#342e37">
    <v-btn text icon @click="toggleDrawer()">
      <v-icon color="white">menu</v-icon>
    </v-btn>
    <v-toolbar-title style="color:white">Larrel's Tome</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn flat color="white" @click="registerOrLogIn()">Register/Log in</v-btn>
  </v-toolbar>
</template>

<script>
export default {
  name: 'Toolbar',
  methods: {
    toggleDrawer() {
      this.$emit('toggle-drawer');
    },
    registerOrLogIn() {
      this.$emit('register-or-log-in');
    },
  },
};
</script>
