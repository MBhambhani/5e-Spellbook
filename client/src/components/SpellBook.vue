<template>
  <v-layout column>
    <v-flex
      v-for="(spellGroup, index) in spellList"
      :key="index"
    >
      <div class="title" v-if="spellGroup.level > 0">
        Level {{ spellGroup.level }}
      </div>
      <div class="title" v-else>Cantrips</div>
      <SpellCard
        v-for="(spell, index) in spellGroup.spells"
        :spell="spell"
        :key="index"
      />
      <v-divider/>
    </v-flex>
  </v-layout>
</template>

<script>
import SpellCard from './SpellCard.vue';

export default {
  name: 'SpellBook',
  components: {
    SpellCard,
  },
  props: ['spellList'],
};
</script>
