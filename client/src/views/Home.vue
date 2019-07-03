<template>
  <v-layout column>
    <SpellGroup v-for="(spellList, index) in spellLists" :key="index"
      :level="spellList.level" :spells="spellList.spells"/>
  </v-layout>
</template>

<script>
import axios from 'axios';
import SpellGroup from '../components/SpellGroup.vue';

export default {
  name: 'home',
  components: {
    SpellGroup,
  },
  data: () => ({
    spellLists: [{
      level: 'Cantrips',
      spells: [{
        name: 'Chill Touch',
        school: 'Necromancy',
        desc: 'hellaooow',
        range: '60 feet',
        casting_time: '1 action',
        components: 'VS',
      }],
    },
    {
      level: 'Level 1',
      spells: [{
        name: 'Magic Missile',
        school: 'Evocation',
        desc: 'hellaooow',
        range: '60 feet',
        casting_time: '1 action',
        components: 'VSM',
      }],
    }],
  }),
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5000/ping';
      axios.get(path)
        .then((response) => {
          this.msg = response.data;
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
