<template>
  <v-expansion-panel>
    <v-expansion-panel-content>
      <template v-slot:header>
        <div>{{ level }}</div>
      </template>
      <v-layout row>
        <SpellCard v-for="(spell, index) in spells" :key="index"
          :spellInfo="spell"/>
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
  props: ['level', 'spells'],
};
</script>
