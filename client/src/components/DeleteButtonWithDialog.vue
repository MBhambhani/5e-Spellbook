<template>
  <v-dialog v-model="dialog" width="30%">
    <template v-slot:activator="{ on }">
      <v-btn
        @mouseover="deleteButtonColor = 'error'"
        @mouseleave="deleteButtonColor = 'grey'"
        v-on.stop="on"
        icon
        class="ma-0"
      >
        <v-icon :color="deleteButtonColor">{{ icon }}</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-card-text class="text-xs-center">
        {{ message }}
      </v-card-text>
      <v-card-actions>
        <v-spacer/>
        <v-btn flat @click="confirm()">
          Yes
        </v-btn>
        <v-btn flat @click="dialog = false">
          No
        </v-btn>
        <v-spacer/>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'DeleteButtonWithDialog',
  props: ['icon', 'message'],
  data: () => ({
    dialog: false,
    deleteButtonColor: 'grey',
  }),
  methods: {
    confirm() {
      this.dialog = false;
      this.$emit('confirm');
    },
  },
};
</script>

<style>

</style>
