<template>
  <v-navigation-drawer permanent>
    <v-toolbar flat>
      <v-list>
        <v-list-tile>
          <v-list-tile-title class="title">
            Larrel's Tome
          </v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-toolbar>

    <v-divider></v-divider>

    <v-list dense class="pt-0">
      <v-list-tile
        v-for="(item, index) in classNames"
        :key="index"
        @click="changeSpells(item)"
      >
        <v-list-tile-content>
          <v-list-tile-title>{{ item }} Spells</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'NavBar',
  methods: {
    changeSpells(selectedClass) {
      this.$emit('change-spells', selectedClass);
    },
  },
  data: () => ({
    classNames: [
      'Bard',
      'Cleric',
      'Druid',
      'Paladin',
      'Ranger',
      'Sorcerer',
      'Warlock',
      'Wizard',
    ],
  }),
};
</script>
