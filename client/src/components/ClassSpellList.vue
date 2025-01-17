<template>
  <v-expansion-panel>
    <v-expansion-panel-content
      v-for="(spellGroup, index) in spellList"
      :key="index"
    >
      <template v-slot:actions>
        <v-icon>$vuetify.icons.expand</v-icon>
      </template>
      <template v-slot:header>
        <div v-if="spellGroup.level > 0"><b>Level {{ spellGroup.level }}</b></div>
        <div v-else><b>Cantrips</b></div>
      </template>
      <v-divider/>
      <v-data-table
        class="pl-4"
        :headers="headers"
        :items="spellGroup.spells"
        hide-actions
      >
        <template v-slot:items="props">
          <td>{{ props.item.name }}</td>
          <td>{{ props.item.school }}</td>
          <td>{{ props.item.casting_time }}</td>
          <td style="width:20%">
            <v-layout row align-center>
              <v-menu offset-y>
                <template v-slot:activator="{ on }">
                  <v-btn
                    dark
                    small
                    class="px-2"
                    v-on="on"
                    color="secondary"
                  >
                    Add To
                  </v-btn>
                </template>
                <v-list>
                  <v-list-tile
                    v-for="(book, index) in spellbooks"
                    :key="index"
                    @click="addToBook(book, props.item.id)"
                  >
                    <v-list-tile-title>{{ book }}</v-list-tile-title>
                  </v-list-tile>
                </v-list>
              </v-menu>
              <SpellInfoModal :spell="props.item"/>
              <CustomSpellDialog
                v-if="isCustom"
                @save="editCustomSpell"
                :spell="props.item"
                :isCreate="false"
              />
              <DeleteButtonWithDialog
                v-if="isCustom"
                @confirm="deleteCustomSpell(props.item.id)"
                :icon="'delete'"
                :message="'Are you sure you want to delete ' + props.item.name + '?'"
              />
            </v-layout>
          </td>
        </template>
      </v-data-table>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import CustomSpellDialog from './CustomSpellDialog.vue';
import DeleteButtonWithDialog from './DeleteButtonWithDialog.vue';
import SpellInfoModal from './SpellInfoModal.vue';

export default {
  name: 'ClassSpellList',
  components: {
    CustomSpellDialog,
    DeleteButtonWithDialog,
    SpellInfoModal,
  },
  props: ['spellList', 'spellbooks', 'isCustom'],
  data: () => ({
    headers: [
      {
        text: 'Spell Name',
        sortable: true,
        value: 'name',
      },
      {
        text: 'School of Magic',
        sortable: true,
        value: 'school',
      },
      {
        text: 'Casting Time',
        sortable: true,
        value: 'casting_time',
      },
    ],
  }),
  methods: {
    addToBook(book, spellId) {
      if (this.isCustom) {
        this.$emit('add-custom-spell-to-book', { book_name: book, spell_id: spellId });
      } else {
        this.$emit('add-spell-to-book', { book_name: book, spell_id: spellId });
      }
    },
    editCustomSpell(spellData) {
      this.$emit('edit-custom-spell', spellData);
    },
    deleteCustomSpell(spellId) {
      this.$emit('delete-custom-spell', { spell_id: spellId });
    },
  },
};
</script>

<style>
.v-btn {
  min-width: 0 !important;
}
</style>
