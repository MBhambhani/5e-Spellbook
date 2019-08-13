<template>
  <v-toolbar app clipped-left flat color="primary">
    <v-btn text icon @click="toggleDrawer()">
      <v-icon color="white">menu</v-icon>
    </v-btn>
    <v-toolbar-title style="color:white">Larrel's Tome</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn flat color="white" v-show="isLoggedIn" @click="logout()">
      Log out
    </v-btn>
    <v-dialog v-model="dialog" width="50%">
      <template v-slot:activator="{ on }">
        <v-btn flat color="white" v-on="on" v-show="!isLoggedIn">
          Register / Log in
        </v-btn>
      </template>
      <v-card>
        <v-card-text>
          <v-form ref="form">
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
          <v-btn
            @click="registerOrLogin('register')"
            class="form-button"
            :disabled="!formIsValid"
            color="info"
          >
            Register
          </v-btn>
          <v-btn
            @click="registerOrLogin('login')"
            class="form-button"
            :disabled="!formIsValid"
            color="info"
          >
            Log In
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-toolbar>
</template>

<script>
export default {
  name: 'Toolbar',
  props: ['spellbooks', 'isLoggedIn'],
  data: () => ({
    dialog: false,
    username: '',
    password: '',
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
    clearUsernamePassword() {
      this.$refs.form.reset();
    },
    registerOrLogin(action) {
      this.dialog = false;
      this.$emit(action, {
        username: this.username,
        password: this.password,
      });
      this.clearUsernamePassword();
    },
    logout() {
      this.$emit('logout');
    },
  },
  computed: {
    formIsValid() {
      return this.username && this.password;
    },
  },
};
</script>
