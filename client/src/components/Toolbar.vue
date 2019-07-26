<template>
  <v-toolbar app clipped-left flat color="#342e37">
    <v-btn text icon @click="toggleDrawer()">
      <v-icon color="white">menu</v-icon>
    </v-btn>
    <v-toolbar-title style="color:white">Larrel's Tome</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-dialog v-model="dialog" width="50%">
      <template v-slot:activator="{ on }">
        <v-btn flat color="white" v-on="on">Register/Log in</v-btn>
      </template>
      <v-card>
        <v-card-text>
          <v-form v-model="valid">
            <v-text-field
              v-model="username"
              label="Username"
              :rules="usernameRules"
              prepend-icon="person"
              type="text"
              required
            ></v-text-field>

            <v-text-field
              v-model="password"
              label="Password"
              :rules="passwordRules"
              prepend-icon="lock"
              type="password"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="register()" class="form-button">Register</v-btn>
          <v-btn @click="logIn()" class="form-button">Log In</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-toolbar>
</template>

<script>
export default {
  name: 'Toolbar',
  data: () => ({
    usernameRules: [
      v => !!v || 'Username is required',
    ],
    passwordRules: [
      v => !!v || 'Password is required',
    ],
  }),
  methods: {
    toggleDrawer() {
      this.$emit('toggle-drawer');
    },
    registerOrLogIn() {
      this.$emit('register-or-log-in');
    },
    register() {
    },
  },
};
</script>

<style>
.form-button {
  background-color:#3c91e6 !important;
  color: white !important;
}
</style>
