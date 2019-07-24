<template>
  <v-app>
    <Toolbar @toggle-drawer="drawer = !drawer"/>
    <NavBar @change-spells="handleChangeSpells" :drawer="drawer"/>
    <v-content>
      <v-flex shrink>
        <ClassSpellList :spellList="spellList" v-show="!viewingSpellbooks"/>
        <SpellBook :spellList="spellList" v-show="viewingSpellbooks"/>
      </v-flex>
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
    handleChangeSpells(selectedClass) {
      const path = `http://127.0.0.1:5000/spells?filter=${selectedClass}`;
      axios.get(path)
        .then((response) => {
          this.viewingSpellbooks = false;
          this.spellList = this.filterSpellLists(response.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    filterSpellLists(data) {
      return data.filter(sp => sp.spells && sp.spells.length > 0);
    },
  },
};
</script>
