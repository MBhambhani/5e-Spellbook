<template>
  <v-app>
    <Toolbar
      @toggle-drawer="drawer = !drawer"
      @register="handleRegister"
      @log-in="handleLogIn"
    />
    <NavBar
      @change-spells="handleChangeSpells"
      @view-book="handleViewBook"
      @add-book="handleAddBook"
      :drawer="drawer"
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
  </v-app>
</template>

<script>
import axios from 'axios';
import Toolbar from '../components/Toolbar.vue';
import NavBar from '../components/NavBar.vue';
import ClassSpellList from '../components/ClassSpellList.vue';
import SpellBook from '../components/SpellBook.vue';

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
    viewingSpellbooks: false,
    drawer: true,
    loading: false,
  }),
  methods: {
    handleRegister() {

    },
    handleLogIn() {

    },
    handleChangeSpells(selectedClass) {
      const path = `http://127.0.0.1:5000/spells?filter=${selectedClass}`;
      this.loading = true;
      axios.get(path)
        .then((response) => {
          this.viewingSpellbooks = false;
          this.spellList = this.filterSpellList(response.data);
          this.loading = false;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.loading = false;
        });
    },
    filterSpellList(data) {
      return data.filter(sp => sp.spells && sp.spells.length > 0);
    },
    handleViewBook() {
      this.viewingSpellbooks = true;
    },
    handleAddBook() {

    },
  },
};
</script>
