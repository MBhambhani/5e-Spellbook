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
      @view-custom-spells="handleViewCustomSpells"
      @add-custom-spell="handleAddCustomSpell"
      :isDrawerOpen="isDrawerOpen"
      :isLoggedIn="isLoggedIn"
      :spellbooks="spellbooks"
    />
    <v-content>
      <ClassSpellList
        @add-spell-to-book="handleAddSpellToBook"
        @add-custom-spell-to-book="handleAddCustomSpellToBook"
        @edit-custom-spell="handleEditCustomSpell"
        @delete-custom-spell="handleDeleteCustomSpell"
        :spellList="spellList"
        :spellbooks="spellbooks"
        :isCustom="displayedClass === 'custom'"
        v-if="!displayedBook"
      />
      <SpellBook
        @remove-custom-spell-from-book="handleRemoveCustomSpellFromBook"
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
  methods: {
    displayErrorMessage(error) {
      // eslint-disable-next-line
      console.error(error);
      this.isLoading = false;
      this.snackbarText = error.response ? error.response.data.message : 'Error!';
      this.isSnackbarError = true;
      this.isSnackbarActive = true;
    },
    displaySuccessMessage(response) {
      this.isLoading = false;
      this.snackbarText = response.data.message;
      this.isSnackbarError = false;
      this.isSnackbarActive = true;
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
    handleAddCustomSpell(data) {
      Utils.addCustomSpell(data, this.jwt)
        .then(() => {
          if (this.displayedClass === 'custom') {
            this.handleViewCustomSpells();
          }
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleAddCustomSpellToBook(data) {
      Utils.addCustomSpellToBook(data, this.jwt)
        .then((response) => {
          this.displaySuccessMessage(response);
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleAddSpellToBook(data) {
      Utils.addSpellToBook(data, this.jwt)
        .then((response) => {
          this.displaySuccessMessage(response);
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
    handleDeleteCustomSpell(data) {
      Utils.deleteCustomSpell(data, this.jwt)
        .then(() => {
          this.handleViewCustomSpells();
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleEditCustomSpell(data) {
      Utils.editCustomSpell(data, this.jwt)
        .then(() => {
          this.handleViewCustomSpells();
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
    handleRemoveCustomSpellFromBook(spellId) {
      Utils.removeCustomSpellFromBook({
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
    handleRemoveSpellFromBook(spellId) {
      Utils.removeSpellFromBook({
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
    handleViewBook(name) {
      this.isLoading = true;
      Utils.getBook(name, this.jwt)
        .then((response) => {
          this.isLoading = false;
          this.displayedBook = name;
          this.displayedClass = '';
          this.spellList = response.data;
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleViewClassSpells(selectedClass) {
      this.isLoading = true;
      Utils.getSpells(selectedClass)
        .then((response) => {
          this.isLoading = false;
          this.displayedBook = '';
          this.displayedClass = selectedClass;
          this.spellList = response.data;
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
    handleViewCustomSpells() {
      this.isLoading = true;
      Utils.getCustomSpells(this.jwt)
        .then((response) => {
          this.isLoading = false;
          this.displayedBook = '';
          this.displayedClass = 'custom';
          this.spellList = response.data;
        })
        .catch((error) => {
          this.displayErrorMessage(error);
        });
    },
  },
};
</script>
