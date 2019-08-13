<template>
  <v-flex xs5 md3 mx-3 mb-3>
    <v-card>
      <v-card-title
        primary-title
      >
        <h3>{{ spell.name }}</h3>
      </v-card-title>
      <v-card-actions>
        <v-dialog
          v-model="dialog"
          width="75%"
        >
          <template v-slot:activator="{ on }">
            <v-btn
              color="#3c91e6"
              dark
              small
              v-on="on"
            >
              Info
            </v-btn>
          </template>

          <v-card>
            <v-card-title
              class="headline"
              style="background:#fa824c;color:white"
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
      </v-card-actions>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  name: 'SpellCard',
  props: ['spell'],
  data: () => ({
    dialog: false,
  }),
};
</script>

<style>
.v-btn {
  min-width: 0 !important;
}
h3 {
  font-weight: normal;
}
</style>
