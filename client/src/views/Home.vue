<template>
  <v-app>
    <Toolbar
      @toggle-drawer="drawer = !drawer"
      @register="handleRegister"
      @login="handleLogin"
      @logout="handleLogout"
      :loggedIn="isLoggedIn"
    />
    <NavBar
      @view-class-spells="handleViewClassSpells"
      @view-book="handleViewBook"
      @create-book="handleCreateBook"
      @delete-book="handleDeleteBook"
      :drawer="drawer"
      :loggedIn="isLoggedIn"
      :spellbooks="spellbooks"
    />
    <v-content>
      <ClassSpellList
        @add-spell-to-book="handleAddSpellToBook"
        :spellList="spellList"
        :spellbooks="spellbooks"
        v-show="!viewingSpellbooks"
      />
      <SpellBook
        :spellList="spellList"
        v-show="viewingSpellbooks"
      />
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
      <v-icon v-if="!snackbarError" color="#9fd356">check</v-icon>
      <v-icon v-else color="#fa824c">error</v-icon>
      {{ snackbarText }}
      <v-btn
        icon
        @click="snackbar = false"
      >
        <v-icon color="white">
          clear
        </v-icon>
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
    jwt: localStorage.getItem('jwt') || '',
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
          localStorage.setItem('jwt', this.jwt);
          this.displaySuccessMessage(response);
          this.getUserSpellbooks();
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleLogout() {
      this.jwt = '';
      localStorage.removeItem('jwt');
    },
    getUserSpellbooks() {
      Utils.getAllBooksForUser(this.jwt)
        .then((response) => {
          this.spellbooks = response.data;
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleViewBook(name) {
      this.loading = true;
      Utils.getBook(name, this.jwt)
        .then((response) => {
          this.viewingSpellbooks = true;
          this.spellList = this.filterSpellList(response.data);
          this.loading = false;
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleCreateBook(data) {
      Utils.createBook(data, this.jwt)
        .then(() => {
          this.getUserSpellbooks();
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleDeleteBook(data) {
      Utils.deleteBook(data, this.jwt)
        .then(() => {
          this.getUserSpellbooks();
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleAddSpellToBook(data) {
      Utils.addToBook(data, this.jwt)
        .then((response) => {
          this.displaySuccessMessage(response);
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
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
      // eslint-disable-next-line
      console.error(error);
      this.loading = false;
      this.snackbarText = error.response ? error.response.data.message : 'Error!';
      this.snackbarError = true;
      this.snackbar = true;
    },
  },
  computed: {
    isLoggedIn() {
      if (!this.jwt) {
        return false;
      }
      const token = this.jwt.split('.');
      const body = JSON.parse(atob(token[1]));
      return Date.now() < (body.exp * 1000);
    },
  },
  mounted() {
    if (this.jwt) {
      this.getUserSpellbooks();
    }
  },
};
</script>
