<template>
  <div>
    <ul class="roster">
      <h3>Roster:</h3>
      <li v-for="hero in heroes"
          :key="hero.name"
          :value="hero.name">
        <!-- to do: conditionally display this span -->
        <span v-if="hero.chosenHero">✔ &nbsp;</span>
        <span>{{ hero.name }}&nbsp;</span>
        <span class="edit"
              @click="editHero(hero)">edit</span>
      </li>
      <br>
          <input type="text"
             placeholder="new name"
             v-model="newName"
             v-if="isEdit"
             @keyup.enter="changeName"
             @blur="clear">
      <br>
      <span v-if="isEdit">enter to submit, click outside the box to cancel</span>
    </ul>
  </div>
</template>

<script>
import Hero from "./Hero";
import ChosenHeroes from "./ChosenHeroes"

export default {
  components: {
    Hero,
    ChosenHeroes
  },
  props: ["heroes"],
  data() {
    return {
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