# Simple TFS API wrapper
class TFS(object):
    def __init__(self, uri):
        uri = 'http://cyg249:8080/tfs/DefaultCollection/akshitaK'
        from System import Uri
        self.uri = Uri(uri)
        self._connected = False
 
    def connect(self):
        import clr
        clr.AddReferenceToFileAndPath(r"C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\IDE\ReferenceAssemblies\v2.0\Microsoft.TeamFoundation.dll")
        clr.AddReference("Microsoft.TeamFoundation.Client.dll")
        clr.AddReference("Microsoft.TeamFoundation.VersionControl.Client.dll")
        clr.AddReference("Microsoft.TeamFoundation.WorkItemTracking.Client.dll")
        from Microsoft.TeamFoundation.Client import WindowsCredential, TfsClientCredentials, TfsTeamProjectCollection
        tfsCreds = TfsClientCredentials(WindowsCredential(), True)
        self.server = TfsTeamProjectCollection(self.uri, tfsCreds)
        if self.server is None:
            raise InvalidOperationException("Could not get TFS server for " + self.uri + ".")
 
        self.server.EnsureAuthenticated();
 
        if not self.server.HasAuthenticated:
            raise InvalidOperationException("TFS could not authenticate.")
     
        self._connected = True
 
    def query_work_items(self, projectName, fromDate):
        from Microsoft.TeamFoundation.WorkItemTracking.Client import WorkItemStore
        from System.Collections.Generic import Dictionary
 
        if not self._connected:
            raise InvalidOperationException("TFS not connected.")
         
        workItemStore = self.server.GetService(clr.GetClrType(WorkItemStore))
 
        if workItemStore is None:
            raise InvalidOperationException("Could not get WorkItemStore.")
 
        parameters = Dictionary[String, String]()
        parameters.Add("Project", projectName)
        query = "Select [Id], [Title], [Changed Date] From WorkItems Where [System.TeamProject] = @Project"
        if fromDate is not None:
            query = query + " And [Changed Date] >= '" + fromDate.ToString("yyyy-MM-dd", CultureInfo.InvariantCulture) + "'"
 
        query = query + " Order By [Changed Date] Asc"
 
        return workItemStore.Query(query, parameters)