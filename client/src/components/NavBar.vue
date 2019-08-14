<template>
  <v-navigation-drawer app clipped width="250" v-model="isDrawerOpen">
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
      <v-list-group v-show="isLoggedIn">
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
            <DeleteButtonWithDialog
              @confirm="deleteBook(book)"
              :icon="'delete'"
              :message="'Are you sure you want to delete ' + book + '?'"
            />
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
              color="secondary"
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
import DeleteButtonWithDialog from './DeleteButtonWithDialog.vue';

export default {
  name: 'NavBar',
  components: {
    DeleteButtonWithDialog,
  },
  props: ['isDrawerOpen', 'isLoggedIn', 'spellbooks'],
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
