<template>
<div class="card">
    <div class="card-image">
        <figure class="image is-4by3">
            <img :src="course.get_image" alt="Placeholder Image">
        </figure>
    </div>

    <div class="card-content">
        <div class="media">
            <div class="media-content">
                <p class="is-size-5">{{ course.title }}</p>
            </div>
        </div>

        <div class="content">
            <span v-html="course.short_description"></span>

            <router-link :to="{'name': 'Course', params: {slug: course.slug}}">
                <p><br /><button class="button is-primary">More</button></p>
            </router-link>
        </div>
    </div>
</div>
</template>

<script>
export default {
    props: ['course']
}
</script>