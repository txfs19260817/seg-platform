<template>
    <div>
        <el-upload
                class="upload-demo"
                ref="upload"
                list-type="picture-card"
                accept="image/jpeg,image/jpg,image/png"
                :limit="1"
                action="http://localhost:5000/predict"
                :before-upload="handleBeforeUpload"
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :on-exceed="handleExceed"
                :on-success="handleSuccess"
                :file-list="fileList"
        >
            <i class="el-icon-plus"></i>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过2mb</div>
        </el-upload>
        <el-dialog :visible.sync="dialogVisible">
            <img width="100%" :src="dialogImageUrl" alt="Uploaded Image">
        </el-dialog>
    </div>
</template>

<script>
    export default {
        name: "Upload",
        data() {
            return {
                fileList: [],
                // Preview dialog
                dialogImageUrl: '',
                dialogVisible: false,
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
                this.dialogImageUrl = file.url;
                this.dialogVisible = true;
            },
            handleExceed(files, fileList) {
                this.$message.error(`请删除后重新添加图片`);
            },
            handleSuccess(response, file, fileList) {
                console.log(response);
                this.$emit('update:img', response)
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