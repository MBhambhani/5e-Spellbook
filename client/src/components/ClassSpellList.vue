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
            <v-layout row>
              <v-btn dark small class="add-btn px-2">Add</v-btn>
              <SpellInfoModal :spell="props.item"/>
            </v-layout>
          </td>
        </template>
      </v-data-table>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import SpellInfoModal from './SpellInfoModal.vue';

export default {
  name: 'ClassSpellList',
  components: {
    SpellInfoModal,
  },
  props: ['spellList'],
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
};
</script>

<style>
.v-btn {
  min-width: 0 !important;
}
.add-btn {
  background-color:#9fd356 !important;
}
</style>
