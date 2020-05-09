<template>
    <div>
        <el-upload
                class="upload-demo"
                ref="upload"
                list-type="picture-card"
                accept="image/jpeg,image/jpg,image/png"
                :limit="1"
                :action="addr"
                :before-upload="handleBeforeUpload"
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :on-exceed="handleExceed"
                :on-success="handleSuccess"
                :file-list="fileList">
            <i class="el-icon-plus"></i>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过3mb</div>
        </el-upload>
<!--        image preview-->
        <el-dialog :visible.sync="dialogVisible">
            <img width="100%" :src="dialogImageUrl" alt="Uploaded Image">
        </el-dialog>
    </div>
</template>

<script>
    export default {
        name: "Upload",
        props: {
            segType: {
                type: String,
                default: 'isaid'
            }
        },
        data() {
            return {
                fileList: [],
                // Preview dialog
                dialogImageUrl: '',
                dialogVisible: false,
                // loading
                load: null,
            };
        },
        methods: {
            submitUpload() {
                this.$refs.upload.submit();
            },
            handleBeforeUpload(file) {
                let test = /^image\/(jpeg|png|jpg)$/.test(file.type);
                const isLt3M = file.size / 1024 / 1024 < 3;
                // check format
                if (!test) {
                    this.$message.error('上传图片格式有误，支持格式：png, jpg, jpeg');
                    return false
                }
                // check size
                if (!isLt3M) {
                    this.$message.error('上传图片大小不能超过 3MB');
                    return false
                }

                // Loading
                this.load = this.$loading({
                    lock: true,
                    text: 'Loading... Please wait patiently. ',
                    spinner: 'el-icon-loading',
                    background: 'rgba(0, 0, 0, 0.5)'
                });

                return test && isLt3M
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

                this.load.close();
                this.$emit('update:img', response)
            },
        },
        computed:{
            addr(){
                return "http://localhost:5000/predict?type="+this.segType+"&multiple=0"
            }
        }
    }
</script>

<style scoped>
    .buttons {
        display: flex;
        justify-content: center;
    }

</style>