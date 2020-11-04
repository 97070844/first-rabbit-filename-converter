"""
Python code to get a filetype (file extension) from a given filepath

"""

FILE_TYPES = {'image':['.ico','.jpeg','.png','.ai','.gif','.jpg','.svg','.bmp'],
'video':['.avi','.mp4','.mov','.wmv','.flv','.mkv','.m4v','.vob'],
'programming':['.py','.java','.c','.cpp','.cs','.php','js','.pl','.h','.swift','.vb'],
'audio' : ['.mp3','.wpl','.wma','.wav','.ogg','.mpa'],
'word-related': ['.doc','.docx','.txt','.pdf','.odt','wpd','.rtf'],
'spreadsheet': ['.ods','..xls','.xlsm','.xlsx'],
'presentation': ['.pps','.ppt','.pptx','.odp','.key'],
'internet-related': ['.css','.html','.xtml','.json','.asp','.aspx','htm']
}


#return filetype
def get_filetype(path):
    format = get_fileformat(path)
    for name,ext in FILE_TYPES.items():
        if format in ext:
            output = name
            return output
    
    output = None      
    return output 

#return file extension
def get_fileformat(path):
    #use regular expression
    #to get (.extension) from a filepath
    import re
    format = re.search("\.\w+",path).group(0)
    
    return format



############### Example #############
if __name__ == '__main__':
    filepath = "E:\\user\Aj48\Desktop\folder\sample-(1).py"

    filetype = get_filetype(filepath)

    print(filetype)






