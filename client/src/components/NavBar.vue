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
          @click="viewClassSpells(item)"
          class="pl-3"
        >
          <v-list-tile-content>
            <v-list-tile-title>{{ item }} Spells</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list-group>
      <!-- MY SPELLBOOKS -->
      <v-list-group v-show="loggedIn">
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
          class="pl-3"
          @click="viewBook(book)"
        >
          <v-list-tile-content>
            <v-list-tile-title>{{ book }}</v-list-tile-title>
          </v-list-tile-content>
          <v-list-tile-action>
            <v-btn icon @click.stop="deleteBook(book)">
              <v-icon color="grey">delete</v-icon>
            </v-btn>
          </v-list-tile-action>
        </v-list-tile>
        <v-list-tile
          class="pl-3"
        >
          <v-list-tile-content>
            <v-text-field
              v-model="newBookName"
              :append-icon="newBookName == '' ? '' : 'add'"
              @click:append="createBook()"
              type="text"
              placeholder="Add new spellbook"
              class="body-1"
            />
          </v-list-tile-content>
        </v-list-tile>
      </v-list-group>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'NavBar',
  props: ['drawer', 'loggedIn', 'spellbooks'],
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
    newBookName: '',
  }),
  methods: {
    viewClassSpells(cls) {
      this.$emit('view-class-spells', cls);
    },
    viewBook(book) {
      this.$emit('view-book', book);
    },
    createBook() {
      this.$emit('create-book', { book_name: this.newBookName });
      this.newBookName = '';
    },
    deleteBook(book) {
      this.$emit('delete-book', { book_name: book });
    },
  },
};
</script>
