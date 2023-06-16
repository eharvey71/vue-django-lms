<template>
  <div class="home">
    <div class="hero is-link is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to MicroMastery</h1>
        <h2 class="subtitle">Elevate Your Skills, Boost Your Career, and Stand Out with Verified Micro-Credentials!</h2>
      </div>
    </div>
    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-star"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Accelerate Your Success</h2>
              <p>Gain in-demand skills, advance your career! Our microcredentialing service offers a unique opportunity to propel your success by acquiring specialized skills that are in high demand</p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-compass"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Stay Ahead of the Curve</h2>
              <p>Microcredentials for continuous learning and professional growth. In a rapidly evolving world, maintaining relevance and staying ahead of the curve is paramount</p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="fas fa-bolt"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Empower Your Journey</h2>
              <p>Showcase new credentials to employers, clients, and peers. Gain a competitive advantage and build trust and credibility in your abilities</p>
            </div>
          </div>
          <div class="column is-12 has-text-centered">
            <a href="/sign-up" class="button is-link is-size-3 mt-6 mb-6">Click to get started</a>
          </div>
          <hr>
          <div 
              class="column is-3"
              v-for="course in courses"
              v-bind:key="course.id"
          >
              <CourseItem :course="course" />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

import CourseItem from '@/components/CourseItem.vue'

export default {
  name: 'Home',
  data() {
      return {
          courses: []
      }
  },
  components: {
      CourseItem
  },
  mounted() {
      console.log('mounted')

      document.title = 'Welcome | MicroMastery'

      axios
          .get('courses/get_frontpage_courses/')
          .then(response => {
              console.log(response.data)

              this.courses = response.data
          })
  }
}
</script>