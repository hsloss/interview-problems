<template>
  <div>
    <!-- justice leage application begins here -->
    <h1 id="jl">Justice League Mission Planner</h1>
    <ChangeName v-bind:heroes="heroes" v-on:changeName="updateName($event)"></ChangeName>
    <ChosenHeroes v-bind:heroes="heroes"></ChosenHeroes>
  </div>
</template>


<script>
import ChosenHeroes from "./components/ChosenHeroes.vue";
import Hero from "./components/Hero.vue";
import ChangeName from "./components/ChangeName.vue"

export default {
  components: {
    ChosenHeroes,
    Hero,
    ChangeName
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
    },
    updateName: function(updatedName){
        this.name = updatedName;
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