<template>
  <v-app>
    <Toolbar
      @toggle-drawer="isDrawerOpen = !isDrawerOpen"
      @register="handleRegister"
      @login="handleLogin"
      @logout="handleLogout"
      :isLoggedIn="isLoggedIn"
      :title="displayedBook || displayedClass && displayedClass + ' Spells'"
    />
    <NavBar
      @view-class-spells="handleViewClassSpells"
      @view-book="handleViewBook"
      @create-book="handleCreateBook"
      @delete-book="handleDeleteBook"
      :isDrawerOpen="isDrawerOpen"
      :isLoggedIn="isLoggedIn"
      :spellbooks="spellbooks"
    />
    <v-content>
      <ClassSpellList
        @add-spell-to-book="handleAddSpellToBook"
        :spellList="spellList"
        :spellbooks="spellbooks"
        v-if="!displayedBook"
      />
      <SpellBook
        @remove-spell-from-book="handleRemoveSpellFromBook"
        :spellList="spellList"
        v-else
      />
    </v-content>
    <v-dialog
      v-model="isLoading"
      persistent
      width="300"
    >
      <v-card
        color="accent"
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
      v-model="isSnackbarActive"
      :timeout="2000"
    >
      <v-icon v-if="!isSnackbarError" color="success">check</v-icon>
      <v-icon v-else color="warning">error</v-icon>
      <v-spacer/>
      {{ snackbarText }}
      <v-spacer/>
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
    displayedBook: '',
    displayedClass: '',
    isDrawerOpen: true,
    isLoading: false,
    isSnackbarActive: false,
    isSnackbarError: false,
    snackbarText: '',
  }),
  methods: {
    handleViewClassSpells(selectedClass) {
      this.isLoading = true;
      Utils.getSpells(selectedClass)
        .then((response) => {
          this.isLoading = false;
          this.displayedBook = '';
          this.displayedClass = selectedClass;
          this.spellList = this.filterSpellList(response.data);
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleRegister(userData) {
      this.isLoading = true;
      Utils.register(userData)
        .then(() => {
          this.handleLogin(userData);
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleLogin(userData) {
      this.isLoading = true;
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
      this.isLoading = true;
      Utils.getBook(name, this.jwt)
        .then((response) => {
          this.isLoading = false;
          this.displayedBook = name;
          this.displayedClass = '';
          this.spellList = this.filterSpellList(response.data);
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
          if (data.book_name === this.displayedBook) {
            this.spellList = [];
            this.displayedBook = '';
          }
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
    handleRemoveSpellFromBook(spellId) {
      Utils.removeFromBook({
        book_name: this.displayedBook,
        spell_id: spellId,
      }, this.jwt)
        .then((response) => {
          // refresh spells shown on page
          this.handleViewBook(this.displayedBook);
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
      this.isLoading = false;
      this.snackbarText = response.data.message;
      this.isSnackbarError = false;
      this.isSnackbarActive = true;
    },
    displayErrorMessage(error) {
      // eslint-disable-next-line
      console.error(error);
      this.isLoading = false;
      this.snackbarText = error.response ? error.response.data.message : 'Error!';
      this.isSnackbarError = true;
      this.isSnackbarActive = true;
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
