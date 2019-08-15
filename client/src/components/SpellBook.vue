<template>
  <v-layout column>
    <div v-if="isBookEmpty" class="title text-xs-center mt-5">
      Your spellbook is currently empty.
    </div>
    <v-flex
      v-else
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
          @remove-custom-spell="removeCustomSpellFromBook"
          @remove-spell="removeSpellFromBook"
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
  methods: {
    removeCustomSpellFromBook(spellId) {
      this.$emit('remove-custom-spell-from-book', spellId);
    },
    removeSpellFromBook(spellId) {
      this.$emit('remove-spell-from-book', spellId);
    },
  },
  computed: {
    isBookEmpty() {
      let isEmpty = true;
      this.spellList.forEach((spellGroup) => {
        if (spellGroup.spells.length > 0) {
          isEmpty = false;
        }
      });
      return isEmpty;
    },
  },
};
</script>
