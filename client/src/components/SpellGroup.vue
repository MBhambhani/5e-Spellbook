<template>
  <v-expansion-panel>
    <v-expansion-panel-content>
      <template v-slot:header>
        <div>{{ groupName }}</div>
      </template>
      <v-layout row>
        <SpellCard v-for="(spell, index) in spells" :key="index" :spellInfo="spell"/>
      </v-layout>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import SpellCard from './SpellCard.vue';

export default {
  name: 'SpellGroup',
  components: {
    SpellCard,
  },
  data: () => ({
    groupName: 'Cantrips',
    spells: [{
      name: 'hoi',
      school: 'Necromancy',
      desc: 'hellaooow',
      range: '60 feet',
      casting_time: '1 action',
      components: 'V',
    }],
  }),
};
</script>
