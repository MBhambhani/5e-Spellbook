<template>
  <v-layout column>
    <v-toolbar class="title-background elevation-0">
      <v-toolbar-title class="title-text">Larrel's Tome</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat><span class="title-text">Log out</span></v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-layout row>
      <v-flex xs3 md2>
        <NavBar @change-spells="handleChangeSpells"/>
      </v-flex>
      <v-flex xs9 md10>
        <v-expansion-panel class="elevation-0">
          <SpellGroup v-for="(spellList, index) in spellLists" :key="index"
            :level="spellList.level" :spells="spellList.spells"/>
        </v-expansion-panel>
      </v-flex>
    </v-layout>
  </v-layout>
</template>

<script>
import axios from 'axios';
import SpellGroup from '../components/SpellGroup.vue';
import NavBar from '../components/NavBar.vue';

export default {
  name: 'home',
  components: {
    SpellGroup,
    NavBar,
  },
  data: () => ({
    spellLists: [],
  }),
  methods: {
    handleChangeSpells(selectedClass) {
      const path = `http://127.0.0.1:5000/spells?filter=${selectedClass}`;
      axios.get(path)
        .then((response) => {
          this.spellLists = this.filterSpellLists(response.data);
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

<style>
.title-text {
  color:white;
}
.title-background {
  background-color:#342e37 !important;
}
</style>
