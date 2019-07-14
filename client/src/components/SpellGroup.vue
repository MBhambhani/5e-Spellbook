<template>
  <v-expansion-panel>
    <v-expansion-panel-content>
      <template v-slot:header>
        <div v-if="level > 0">Level {{ level }}</div>
        <div v-else>Cantrips</div>
      </template>
      <v-container grid-list-medium fluid>
        <v-layout row wrap>
          <SpellCard v-for="(spell, index) in spells" :key="index"
            :spellInfo="spell"/>
        </v-layout>
      </v-container>
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
  props: ['level', 'spells'],
};
</script>
