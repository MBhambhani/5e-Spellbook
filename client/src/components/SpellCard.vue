<template>
  <v-flex xs5 md3 mx-3 mb-4>
    <v-card>
      <div class="text-xs-right">
        <v-spacer/>
        <DeleteButtonWithDialog
          @confirm="removeSpell()"
          :icon="'clear'"
          :message="'Are you sure you want to remove ' + spell.name + '?'"
        />
      </div>
      <v-card-text class="text-xs-center pt-0 pb-2">
        <p class="title">{{ spell.name }}</p>
        <div>Range: {{ spell.spell_range }}</div>
        {{ spell.casting_time }}
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
import DeleteButtonWithDialog from './DeleteButtonWithDialog.vue';

export default {
  name: 'SpellCard',
  components: {
    SpellInfoModal,
    DeleteButtonWithDialog,
  },
  props: ['spell'],
  methods: {
    removeSpell() {
      this.dialog = false;

      if (this.spell.creator_id) {
        // only custom spells have a creator_id field
        this.$emit('remove-custom-spell', this.spell.id);
      } else {
        this.$emit('remove-spell', this.spell.id);
      }
    },
  },
};
</script>

<style>
.v-btn {
  min-width: 0 !important;
}
</style>
