<template>
  <v-expansion-panel-content>
    <template v-slot:actions>
      <v-icon>$vuetify.icons.expand</v-icon>
    </template>
    <template v-slot:header>
      <div v-if="level > 0"><b>Level {{ level }}</b></div>
      <div v-else><b>Cantrips</b></div>
    </template>
    <v-divider/>
    <v-data-table
      class="pl-4"
      :headers="headers"
      :items="spells"
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
</template>

<script>
import SpellInfoModal from './SpellInfoModal.vue';

export default {
  name: 'SpellGroup',
  components: {
    SpellInfoModal,
  },
  props: ['level', 'spells'],
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
