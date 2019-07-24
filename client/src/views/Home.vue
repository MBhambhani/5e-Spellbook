<template>
  <v-app>
    <Toolbar
      @toggle-drawer="drawer = !drawer"
      @register-or-log-in="handleRegisterLogIn()"
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
  }),
  methods: {
    handleRegisterLogIn() {

    },
    handleChangeSpells(selectedClass) {
      const path = `http://127.0.0.1:5000/spells?filter=${selectedClass}`;
      axios.get(path)
        .then((response) => {
          this.viewingSpellbooks = false;
          this.spellList = this.filterSpellList(response.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
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
