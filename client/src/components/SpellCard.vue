<template>
  <v-flex xs5 md3 mx-3 mb-3>
    <v-card style="border: 3px solid deep-purple">
      <!-- HEADING -->
      <v-layout row px-3 pt-3 justify-space-between>
        <v-flex subheading xs8 md8>
          {{ spellInfo.name }}
        </v-flex>
        <v-flex xs4 md4 text-xs-right font-weight-bold>
          <span v-show="spellInfo.ritual">[R]</span>
          <span v-show="spellInfo.concentration">[C]</span>
        </v-flex>
      </v-layout>
      <!-- SUBHEADINGS -->
      <v-layout row px-3 pt-2>
        <span class="grey--text"><i>{{ spellInfo.school }}</i></span>
      </v-layout>
      <v-layout row px-3 pt-1>
        {{ spellInfo.casting_time }}
        <v-spacer/>
        {{ spellInfo.components }}
      </v-layout>
      <!-- DETAILS -->
      <v-slide-y-transition>
        <v-layout column px-3 v-show="expand">
          <v-flex pt-1>Range: {{ spellInfo.range }}</v-flex>
          <v-flex pt-1>Duration: {{ spellInfo.duration }}</v-flex>
          <v-flex pt-1 v-show="spellInfo.material">
            Material(s): {{ spellInfo.material }}
          </v-flex>
          <v-flex pt-3>{{ spellInfo.desc }}</v-flex>
        </v-layout>
      </v-slide-y-transition>
      <v-card-actions>
        <v-spacer/>
        <v-btn icon @click="expand = !expand" text-xs-right>
          <v-icon>{{ expand ? 'keyboard_arrow_up' :
            'keyboard_arrow_down' }}</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  name: 'SpellCard',
  props: ['spellInfo'],
  data: () => ({
    expand: false,
  }),
};
</script>
