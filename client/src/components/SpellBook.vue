<template>
  <v-layout column>
    <v-flex
      v-for="(spellGroup, index) in spellList"
      :key="index"
    >
      <div class="title ma-3">
        <span v-if="spellGroup.level > 0">
          Level {{ spellGroup.level }}
        </span>
        <span v-else>
          Cantrips
        </span>
      </div>
      <v-layout row wrap>
        <SpellCard
          v-for="(spell, index) in spellGroup.spells"
          :spell="spell"
          :key="index"
        />
      </v-layout>
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
