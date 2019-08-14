<template>
  <v-dialog
    v-model="dialog"
    width="75%"
  >
    <template v-slot:activator="{ on }">
      <v-btn
        class="modal-btn px-2"
        dark
        small
        v-on="on"
        color="info"
      >
        Info
      </v-btn>
    </template>

    <v-card>
      <v-card-title
        class="headline accent white--text"
        primary-title
      >
        {{ spell.name }}
      </v-card-title>
      <v-card-text>
        <v-flex pt-1>
          <i>
            {{ spell.school }}
            <span v-show="spell.ritual"> ritual</span>
          </i>
        </v-flex>
        <v-flex pt-1>Range: {{ spell.spell_range }}</v-flex>
        <v-flex pt-1>Casting time: {{ spell.casting_time }}</v-flex>
        <v-flex pt-1>
          Duration:
          <span v-show="spell.concentration"> Concentration, </span>
          {{ spell.duration }}
        </v-flex>
        <v-flex pt-1>Components: {{ spell.components }}</v-flex>
        <v-flex pt-1 v-show="spell.material">
          Material(s): {{ spell.material }}
        </v-flex>
        <v-flex pt-3>{{ spell.desc }}</v-flex>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          flat
          @click="dialog = false"
        >
          Close
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'SpellInfoModal',
  props: ['spell'],
  data: () => ({
    dialog: false,
  }),
};
</script>
