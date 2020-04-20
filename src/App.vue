<template>
    <div id="app">
        <Home></Home>
    </div>
</template>

<script>
    import Home from "./views/Home";

    export default {
        name: 'app',
        components: {
            Home
        }
    }
</script>

<style>
    html, body, #app {
        height: 100%;
        margin: 0;
        padding: 0;
    }
</style>
