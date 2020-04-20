<template>
    <el-container class="home-container">
        <el-header>
            <div class="title">
                分割平台
            </div>
        </el-header>
        <el-container>
            <el-main>
                <div class="image">
                    <el-image class="image" :src="src" fit="scale-down"></el-image>
                </div>
                <hr style="color: gainsboro" />
                <upload class="upload"></upload>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
    import Upload from "../components/Upload";

    export default {
        name: "Home",
        components: {
            Upload,
        },
        data() {
            return {
                src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg'
            }
        }
    }
</script>

<style scoped>
    .home-container {
        height: 100%;
    }

    .title {
        height: 60px;
        line-height: 60px;
    }

    .image {
        width: 2048px;
        height: 1024px;
        margin: 0 auto;
    }

    .el-header, .el-footer {
        background-color: #B3C0D1;
        color: #333;
    }

    .el-aside {
        background-color: #D3DCE6;
        color: #333;
    }

    .el-main {
        background-color: #E9EEF3;
        color: #333;
    }

    .upload {
        width: 320px;
        margin: 0 auto;
    }

</style>