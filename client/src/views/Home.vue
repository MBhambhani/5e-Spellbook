<template>
  <v-layout column>
    <SpellGroup/>
  </v-layout>
</template>

<script>
import axios from 'axios';
import SpellGroup from '../components/SpellGroup.vue';

export default {
  name: 'home',
  components: {
    SpellGroup,
  },
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5000/ping';
      axios.get(path)
        .then((response) => {
          this.msg = response.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
