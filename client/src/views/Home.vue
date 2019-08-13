<template>
  <v-app>
    <Toolbar
      @toggle-drawer="drawer = !drawer"
      @register="handleRegister"
      @login="handleLogin"
      :loggedIn="isLoggedIn"
    />
    <NavBar
      @view-class-spells="handleViewClassSpells"
      @view-book="handleViewBook"
      @add-book="handleAddBook"
      :drawer="drawer"
      :loggedIn="isLoggedIn"
      :spellbooks="spellbooks"
    />
    <v-content>
      <ClassSpellList :spellList="spellList" v-show="!viewingSpellbooks"/>
      <SpellBook :spellList="spellList" v-show="viewingSpellbooks"/>
    </v-content>
    <v-dialog
      v-model="loading"
      persistent
      width="300"
    >
      <v-card
        color="#fa824c"
        dark
      >
        <v-card-text>
          Loading...
          <v-progress-linear
            indeterminate
            color="white"
            class="mb-0"
          ></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-snackbar
      v-model="snackbar"
      :timeout="2000"
    >
      <v-icon v-show="!snackbarError" color="#9fd356">check</v-icon>
      <v-icon v-show="snackbarError" color="#fa824c">error</v-icon>
      <span class="ml-3">
        {{ snackbarText }}
      </span>
      <v-btn
        color="#3c91e6"
        flat
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </v-app>
</template>

<script>
import Toolbar from '../components/Toolbar.vue';
import NavBar from '../components/NavBar.vue';
import ClassSpellList from '../components/ClassSpellList.vue';
import SpellBook from '../components/SpellBook.vue';
import Utils from '../utils';

export default {
  name: 'Home',
  components: {
    Toolbar,
    NavBar,
    ClassSpellList,
    SpellBook,
  },
  data: () => ({
    spellList: [],
    spellbooks: [],
    jwt: '',
    userId: '',
    viewingSpellbooks: false,
    drawer: true,
    loading: false,
    snackbar: false,
    snackbarText: '',
    snackbarError: false,
  }),
  methods: {
    handleViewClassSpells(selectedClass) {
      this.loading = true;
      Utils.getSpells(selectedClass)
        .then((response) => {
          this.viewingSpellbooks = false;
          this.spellList = this.filterSpellList(response.data);
          this.loading = false;
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleRegister(userData) {
      this.loading = true;
      Utils.register(userData)
        .then(() => {
          this.handleLogin(userData);
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleLogin(userData) {
      this.loading = true;
      Utils.login(userData)
        .then((response) => {
          this.jwt = response.data.token;
          this.userId = response.data.user_id;
          this.displaySuccessMessage(response);
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    getUserSpellbooks() {
      Utils.getAllBooksForUser({ user_id: this.userId }, this.jwt)
        .then((response) => {
          this.spellbooks = response.data;
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleViewBook(name) {
      this.loading = true;
      Utils.getBook({ book_name: name, user_id: this.userId }, this.jwt)
        .then((response) => {
          this.viewingSpellbooks = true;
          this.spellList = this.filterSpellList(response.data);
          this.loading = false;
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleAddBook(name) {

    },
    handleDeleteBook(name) {

    },
    filterSpellList(data) {
      return data.filter(sp => sp.spells && sp.spells.length > 0);
    },
    displaySuccessMessage(response) {
      this.snackbarText = response.data.message;
      this.snackbarError = false;
      this.snackbar = true;
      this.loading = false;
    },
    displayErrorMessage(error) {
      this.snackbarText = error.response.data.message;
      this.snackbarError = true;
      this.snackbar = true;
      this.loading = false;
      // eslint-disable-next-line
      console.error(error);
    },
  },
  computed: {
    isLoggedIn() {
      if (!this.jwt) {
        return false;
      }
      const token = this.jwt.split('.');
      const body = JSON.parse(atob(token[1]));
      return Date.now() < (body.exp*1000);
    },
  },
};
</script>
