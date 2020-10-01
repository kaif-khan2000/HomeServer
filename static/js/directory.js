function addFolder(id) {
    //add code to add a folder
    name = '';
    name = prompt("Name of the folder");
    if (name != null) {
        $.ajax({
            type: 'GET',
            async: false,
            url: '/addFolder',
            data: {
                'parentId': id,
                'name': name,
            },
            success: function (response) {
                location.reload();
            }
        });
    }

}

//ajax code to rename a file
function renameFile(x, oldname) {
    var newName = prompt('Enter name for ' + oldname)
    if (newName != null) {
        $.ajax({
            type: "GET",
            async: false,
            url: "/renameFile",
            data: {
                'id': x,
                'name': newName,
            },
            success: function (response) {
                location.reload();
            }
        });
    }
}

function deleteFile(x){
    if(confirm("This file will be deleted permenently.")){
        $.ajax({
            type:"GET",
            url:"/deleteFile",
            async:false,
            data:{
                "id":x,
            },
            success:function (response){
              location.reload();  
            }
        });
    }
}

function deleteFolder(x){
    if(confirm("This folder and its contents will be deleted permenently!")){
        $.ajax({
            type:"GET",
            url:"/deleteFolder",
            async:false,
            data:{
                "id":x,
            },
            success:function (response){
              location.reload();  
            }
        });
    }
}

list = ['pdf','video','audio','image']
function openFile(file,type){
    flag = false;
    type = type.split('/')
    for( i in list){
        for(j in type){
            if(list[i] == type[j]) flag = true;
        }
    }

    if (flag) {
        location.href = "/"+file;
    }else{
        
       if(confirm("Unsupported Fi.To download press confirm.")){
          location.href = "/"+file;
       }
        
    }
}