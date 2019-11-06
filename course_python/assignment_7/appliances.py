class Appliance_Item(object):
    
    status_summary = {}
    
    """
    Description:
    ------------
    Stores relevant information of appliances.
    
    Attributes:
    -----------
    name : ~str
      name of the appliance.
    status : ~str
      Status of the appliance.
      Accepts: 'On' or 'Off'. Default is 'Off'.
    
    Outputs:
    --------
    None
    """    
    
    def __init__(self, name, status):

        Appliance_Item.status_summary[name] = status

        self.name = name
        self.status = status

    def change_status(self, make_change):
        if make_change == 'Yes':
            if self.status == 'On':
                self.status = 'Off'
            elif self.status == 'Off':
                self.status = 'On'        
