<template>
  <v-flex xs5 md3 mx-3 mb-4>
    <v-card>
      <v-card-text class="text-xs-center">
        <h3>{{ spell.name }}</h3>
        {{ spell.casting_time }} | {{ spell.spell_range }}
      </v-card-text>
      <v-card-actions>
        <v-spacer/>
        <SpellInfoModal :spell="spell"/>
        <v-spacer/>
      </v-card-actions>
    </v-card>
  </v-flex>
</template>

<script>
import SpellInfoModal from './SpellInfoModal.vue';

export default {
  name: 'SpellCard',
  components: {
    SpellInfoModal,
  },
  props: ['spell'],
  data: () => ({
    dialog: false,
  }),
};
</script>

<style>
.v-btn {
  min-width: 0 !important;
}
h3 {
  font-weight: normal;
}
</style>
