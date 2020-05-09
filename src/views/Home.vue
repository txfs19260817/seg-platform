<template>
    <el-container class="home-container">
        <el-header>
            <div class="title">
                分割平台
            </div>
        </el-header>
        <el-container>
            <el-aside width="200px">
                <h3>设置</h3>
                <h4>切换图像分割场景模式</h4>
                <el-tooltip content="图像分割场景模式" placement="top">
                    <el-switch
                            v-model="segType"
                            active-color="#13CE66"
                            inactive-color="#409EFF"
                            active-value="vista"
                            inactive-value="isaid"
                            active-text="街景分割"
                            inactive-text="遥感分割">
                    </el-switch>
                </el-tooltip>
                <h4>切换上传模式</h4>
                <el-tooltip content="上传模式" placement="top">
                    <el-switch
                            v-model="multiple"
                            active-color="#13CE66"
                            inactive-color="#409EFF"
                            active-text="批量上传"
                            inactive-text="单张上传">
                    </el-switch>
                </el-tooltip>
            </el-aside>
            <el-main>
                <div class="image">
                    <h1 v-if="segType === 'isaid'">当前图像分割场景模式：遥感分割</h1>
                    <h1 v-if="segType === 'vista'">当前图像分割场景模式：街景分割</h1>
                    <el-image class="image"
                              :src="'data:image/png;base64,'+src"
                              fit="scale-down"
                              :preview-src-list="srcList">
                        <div slot="error" class="el-image__error">
                            <i v-if="!multiple" class="el-icon-picture-outline"></i>
                            <span v-else>批量上传图像数据模式下，模型预测完毕后会自动开始下载处理后图像的压缩文件。</span>
                        </div>
                    </el-image>
                    <h3>上传图像数据</h3>
                    <h4 v-if="multiple">最大上传4张</h4>
                    <upload v-if="!multiple" class="upload" :img.sync="src" :seg-type.sync="segType"></upload>
                    <upload-multiple v-else class="upload" :img.sync="src" :seg-type.sync="segType"></upload-multiple>
                    <h3>类别与颜色对应关系表</h3>
                    <img v-if="segType === 'isaid'" class="colorbar" src="../../public/colorbar_isaid.png"
                         alt="colorbar"/>
                    <img v-if="segType === 'vista'" class="colorbar" src="../../public/colorbar_vistas.jpg"
                         alt="colorbar"/>
                </div>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
    import Upload from "../components/Upload";
    import UploadMultiple from "../components/UploadMultiple";

    export default {
        name: "Home",
        components: {
            Upload,
            UploadMultiple,
        },
        data() {
            return {
                // image src
                src: '',
                // seg task type
                segType: 'isaid',
                // multiple images upload
                multiple: false,
            }
        },
        methods: {},
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