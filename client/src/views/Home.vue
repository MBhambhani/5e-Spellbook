<template>
  <v-layout row>
    <v-flex xs3 md2>
      <NavBar @change-spells="handleChangeSpells"/>
    </v-flex>
    <v-flex xs9 md10>
      <v-layout column>
        <SpellGroup v-for="(spellList, index) in spellLists" :key="index"
          :level="spellList.level" :spells="spellList.spells"/>
      </v-layout>
    </v-flex>
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
    spellLists: [
      {
        level: '0',
        spells: [],
      },
      {
        level: '1',
        spells: [],
      },
    ],
  }),
  methods: {
    handleChangeSpells(selectedClass) {
      const path = `http://127.0.0.1:5000/spells?filter=${selectedClass}`;
      axios.get(path)
        .then((response) => {
          this.spellLists = response.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
