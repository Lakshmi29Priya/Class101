import dropbox
class TransferData:
      def __init__(self,access_token):
          self.access_token=access_token

      def upload_file(self,file_from,file_to):
          dbx=dropbox.Dropbox(self.access_token)

          f=open(file_from,'rb')
          dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.AxbuNndcsBUJAbgdJC9S03mP3SKyNEZL5nFQyG5nuzfVfxlK_89eJNzd9lBxFPGZTyeTLlR5bVGYN5d4QETuauaxdaCnLQWt8ilxVgH2boQHzj8pjRJX6p0N8igFp7XmehJz7mY'
    transferData=TransferData(access_token)

    file_from='C:/Users/admin/Desktop/Class101/test.txt'
    file_to='/@project_101/test.txt'

    transferData.upload_file(file_from,file_to)
    print("the file has moved")

main()

     
