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
                    <h1 v-if="segTypeStr === 'isaid'">当前图像分割场景模式：遥感分割</h1>
                    <h1 v-if="segTypeStr === 'vista'">当前图像分割场景模式：街景分割</h1>
                    <el-image class="image"
                              :src="'data:image/png;base64,'+src"
                              fit="scale-down"
                              :preview-src-list="srcList">
                        <div slot="error" class="el-image__error">
                            <i class="el-icon-picture-outline"></i>
                        </div>
                    </el-image>
                    <img v-if="segTypeStr === 'isaid'" class="colorbar" src="../../public/colorbar.png" alt="colorbar"/>
                    <img v-if="segTypeStr === 'vista'" class="colorbar" src="../../public/colorbar_vistas.jpg" alt="colorbar"/>
                    <div>
                        <el-tooltip content="切换图像分割场景" placement="top">
                            <el-switch
                                    v-model="segTypeStr"
                                    active-color="#13CE66"
                                    inactive-color="#409EFF"
                                    active-value="vista"
                                    inactive-value="isaid"
                                    active-text="街景分割"
                                    inactive-text="遥感分割"
                                    @change="changeSegType">
                            </el-switch>
                        </el-tooltip>
                        <upload class="upload" :img.sync="src" :seg-type.sync="segType"></upload>
                    </div>
                </div>
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
                // image src
                src: '',
                // seg task type
                segTypeStr: 'isaid',
                segType: {type: 'isaid'},
            }
        },
        methods: {
            changeSegType(v) {
                this.segType.type = v
            },
        },
        computed: {
            srcList() {
                return ['data:image/png;base64,' + this.src]
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
        width: 1024px;
        height: 512px;
        margin: 0 auto;
    }

    .colorbar {
        width: 1024px;
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
        display: flex;
    }

    .upload {
        width: 320px;
        margin: 0 auto;
    }

</style>