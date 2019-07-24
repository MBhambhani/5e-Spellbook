<template>
  <v-navigation-drawer app clipped width="200" v-model="drawer">
    <v-list dense expand class="pt-0">
      <!-- BROWSE SPELLS -->
      <v-list-group>
        <template v-slot:activator>
          <v-list-tile>
            <v-list-tile-content>
              <v-list-tile-title>Browse Spells</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
        <v-list-tile
          v-for="(item, index) in classNames"
          :key="index"
          @click="changeSpells(item)"
          class="pl-3"
        >
          <v-list-tile-content>
            <v-list-tile-title>{{ item }} Spells</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list-group>
      <!-- MY SPELLBOOKS -->
      <v-list-group>
        <template v-slot:activator>
          <v-list-tile>
            <v-list-tile-content>
              <v-list-tile-title>My Spellbooks</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
        <v-list-tile
          v-for="(book, index) in spellbooks"
          :key="index"
          @click="viewBook(book)"
          class="pl-3"
        >
          <v-list-tile-content>
            <v-list-tile-title>{{ book }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile
          @click="addBook()"
          class="pl-3"
        >
          <v-list-tile-content>
            <v-list-tile-title>Add new spellbook</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list-group>
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
    viewBook(selectedBook) {
      this.$emit('view-book', selectedBook);
    },
    addBook(name) {
      this.$emit('add-book', name);
    },
  },
  props: ['drawer'],
  data: () => ({
    classNames: [
      'All',
      'Bard',
      'Cleric',
      'Druid',
      'Paladin',
      'Ranger',
      'Sorcerer',
      'Warlock',
      'Wizard',
    ],
    spellbooks: [],
  }),
};
</script>
