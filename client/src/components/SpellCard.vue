<template>
  <v-flex xs12 sm3 offset-xs1>
    <v-card>
      <v-card-title primary-title>{{ spellInfo.name }}</v-card-title>
      <v-card-title>
        <div>
          <span class="grey--text">{{ spellInfo.casting_time }}</span>
        </div>
      </v-card-title>
      <v-card-actions>
        <v-btn icon @click="show = !show">
          <v-icon>{{ show ? 'keyboard_arrow_up' :
            'keyboard_arrow_down' }}</v-icon>
        </v-btn>
      </v-card-actions>
      <v-slide-y-transition>
        <v-card-text v-show="show">
          <span>{{ spellInfo.school }}</span><br/>
          <span>{{ spellInfo.desc }}</span>
        </v-card-text>
      </v-slide-y-transition>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  name: 'SpellCard',
  props: ['spellInfo'],
  data: () => ({
    show: false,
  }),
};
</script>
