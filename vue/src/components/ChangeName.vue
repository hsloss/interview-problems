<template>
    <input type="text"
            placeholder="new name"
            v-model="newName"
            v-if="isEdit"
            @keyup.enter="$emit('changeName')"
            @blur="clear">
</template>

import ChosenHeroes from "./components/ChosenHeroes.vue";

export default {
  components: {
    ChosenHeroes
  },
  data() {
    return {
      heroes: [
        { name: "Superman" },
        { name: "Batman" },
        { name: "Aquaman" },
        { name: "Wonder Woman" },
        { name: "Green Lantern" },
        { name: "Martian Manhunter" },
        { name: "Flash" }
      ],
      newName: "",
      isEdit: false,
      heroToModify: null,
    };
  },
  methods: {
    editHero(hero) {
      this.isEdit = true;
      this.newName = hero.name;
      this.heroToModify = hero;
    },

    changeName() {
      this.heroToModify.name = this.newName;
      this.isEdit = false;
      this.newName = this.hero.name
    },

    clear() {
      this.heroToModify = null;
      this.newName = "";
      this.isEdit = false;
    }
  }
};
</script>

<style scoped>
ul.roster {
  text-align: left;
}
.edit {
  color: blue;
  text-decoration: underline;
}
.edit:hover {
  cursor: pointer;
}
</style>