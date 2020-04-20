<template>
    <el-upload
            class="upload-demo"
            ref="upload"
            accept="image/jpeg,image/jpg,image/png"
            :limit=1
            action="http://localhost:5000/predict"
            :before-upload="handleBeforeUpload"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :on-exceed="handleExceed"
            :on-success="handleSuccess"
            :file-list="fileList"
            :auto-upload="false">
            <el-button style="margin-right: 10px" slot="trigger" size="small" type="primary">选取一张图片</el-button>
            <el-button icon="el-icon-arrow-right" circle disabled type="warning"></el-button>
            <el-button style="margin-left: 10px" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
        <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过2mb</div>
    </el-upload>
</template>

<script>
    export default {
        name: "Upload",
        data() {
            return {
                fileList: []
            };
        },
        methods: {
            submitUpload() {
                this.$refs.upload.submit();
            },
            handleBeforeUpload(file) {
                let test = /^image\/(jpeg|png|jpg)$/.test(file.type);
                const isLt2M = file.size / 1024 / 1024 < 2;
                if (!test) {
                    this.$message.error('上传图片格式有误，支持格式：png, jpg, jpeg');
                    return false
                }
                if (!isLt2M) {
                    this.$message.error('上传图片大小不能超过 2MB');
                    return false
                }
                return test && isLt2M
            },
            handleRemove(file, fileList) {
                console.log(file, fileList);
            },
            handlePreview(file) {
                console.log(file);
            },
            handleExceed(files, fileList) {
                this.$message.error(`请删除后重新添加图片`);
            },
            handleSuccess(response, file, fileList) {
                console.log(response, file, fileList);
            },
        }
    }
</script>

<style scoped>
    .buttons {
        display: flex;
        justify-content: center;
    }

</style>