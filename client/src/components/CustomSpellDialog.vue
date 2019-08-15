<template>
  <v-dialog v-model="dialog" width="50%">
    <template v-slot:activator="{ on: { click } }">
      <v-list-tile v-if="isCreate" @click="click">
        <v-list-tile-content>
          <v-list-tile-title>
            Add Custom Spell
          </v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-btn
        v-else
        @click="click"
        @mouseover="iconColor = 'accent'"
        @mouseleave="iconColor = 'grey'"
        icon
      >
        <v-icon :color="iconColor">edit</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-card-text>
        <v-form>
          <v-text-field
            v-model="name"
            label="Name"
          />
          <v-select
            :items="spellLevels"
            v-model="level"
            label="Level"
          />
          <v-text-field
            v-model="school"
            label="School of Magic"
          />
          <v-text-field
            v-model="range"
            label="Range"
          />
          <v-text-field
            v-model="castingTime"
            label="Casting Time"
          />
          <v-text-field
            v-model="duration"
            label="Duration"
          />
          <v-layout row>
            <v-switch
              v-model="ritual"
              label="Ritual"
            />
            <v-switch
              v-model="concentration"
              label="Concentration"
            />
          </v-layout>
          <v-layout row>
            <v-checkbox
              v-model="componentV"
              label="V"
            />
            <v-checkbox
              v-model="componentS"
              label="S"
            />
            <v-checkbox
              v-model="componentM"
              label="M"
            />
          </v-layout>
          <v-text-field
            v-if="componentM"
            v-model="material"
            label="Material"
          />
          <v-textarea
            v-model="desc"
            auto-grow
            rows="1"
            label="Description"
          />
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer/>
        <v-btn flat @click="save()">Save</v-btn>
        <v-spacer/>
        <v-btn flat @click="dialog = false">Cancel</v-btn>
        <v-spacer/>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'CustomSpellDialog',
  props: ['spell', 'isCreate'],
  mounted() {
    const { spell } = this;
    if (spell) {
      this.id = spell.id;
      this.name = spell.name;
      this.level = spell.level;
      this.school = spell.school;
      this.range = spell.spell_range;
      this.castingTime = spell.casting_time;
      this.duration = spell.duration;
      this.ritual = spell.ritual;
      this.concentration = spell.concentration;
      this.componentV = spell.components.includes('V');
      this.componentS = spell.components.includes('S');
      this.componentM = spell.components.includes('M');
      this.material = spell.material;
      this.desc = spell.desc;
    }
  },
  data: () => ({
    dialog: false,
    iconColor: 'grey',
    spellLevels: [...Array(10).keys()],
    id: -1,
    name: '',
    level: 0,
    school: '',
    range: '',
    castingTime: '',
    duration: '',
    ritual: false,
    concentration: false,
    componentV: false,
    componentS: false,
    componentM: false,
    material: '',
    desc: '',
  }),
  methods: {
    save() {
      this.dialog = false;
      let components = '';
      if (this.componentV) { components += 'V'; }
      if (this.componentS) { components += 'S'; }
      if (this.componentM) { components += 'M'; }
      this.$emit('save', {
        id: this.id,
        name: this.name,
        level: this.level,
        ritual: this.ritual,
        concentration: this.concentration,
        school: this.school,
        casting_time: this.castingTime,
        components,
        spell_range: this.range,
        duration: this.duration,
        material: this.material,
        desc: this.desc,
      });
    },
  },
};
</script>
