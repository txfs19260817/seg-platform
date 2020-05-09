<template>
    <div>
        <div class="upload-list">
            <el-upload
                    :action="addr"
                    accept="image/jpeg,image/jpg,image/png"
                    :limit="limit"
                    :show-file-list="true"
                    :on-remove="removeFile"
                    :on-exceed="handleExceed"
                    :on-change="handleChange"
                    :multiple="true"
                    :file-list="fileList"
                    :auto-upload="false"
            >
                <el-button class="card-foot-btn" icon="upload2">选取文件</el-button>
            </el-upload>
        </div>
        <div slot="footer" class="dialog-footer text-center">
            <el-button @click="uploadFile" type="primary">上传</el-button>
            <el-button @click="emptyFilelist">清空</el-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "UploadMultiple",
        props: {
            segType: {
                type: String,
                default: 'isaid'
            }
        },
        data() {
            return {
                fileList: [],
                // the max number of files
                limit: 4,
                // loading
                load: null,
            }
        },
        methods: {
            // push file to file list when add a file
            handleChange(fileList) {
                this.fileList.push(fileList)
            },
            // remove a file from the file list
            removeFile(file) {
                // reassign the file name when remove a file
                let arr = [];
                for (let i = 0; i < this.fileList.length; i++) {
                    if (this.fileList[i].uid !== file.uid) {
                        arr.push(this.fileList[i])
                    }
                }
                this.fileList = arr
            },
            // upload file manually
            uploadFile() {
                if (this.fileList.length === 0) {
                    this.$message.warning('请选取文件');
                    return
                }
                // Loading
                this.load = this.$loading({
                    lock: true,
                    text: 'Loading... Please wait patiently. ',
                    spinner: 'el-icon-loading',
                    background: 'rgba(0, 0, 0, 0.5)'
                });
                const formData = new FormData();
                // append each uploaded images to formData structure
                this.fileList.forEach((file, i) => {
                    formData.append('file' + i, file.raw)
                });
                // post method
                let config = {
                    responseType: 'blob',
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                };
                this.$http.post(this.addr, formData, config).then(res => {
                    // download zip
                    const url = window.URL.createObjectURL(new Blob([res.data]));
                    const link = document.createElement('a');
                    link.href = url;
                    link.setAttribute('download', 'results.zip');
                    document.body.appendChild(link);
                    link.click();

                    // empty the file list
                    this.emptyFilelist();

                    // close loading modal and show success popup
                    this.load.close();
                    this.$message.info("success");
                }).catch(err => {
                    this.load.close();
                    this.$message.error('上传失败，请重新上传');
                    console.log('报错', err)
                })
            },
            handleExceed(files, fileList) {
                this.$message.error(`上传文件数量不能大于` + this.limit);
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

                return test && isLt3M
            },
            emptyFilelist() {
                this.fileList.splice(0, this.fileList.length);
            },
        },
        computed: {
            // url
            addr() {
                return "http://localhost:5000/predict?type=" + this.segType + "&multiple=1"
            }
        }
    }
</script>

<style scoped>
    .upload-list {
        height: 200px;
        overflow: auto;
    }
</style>