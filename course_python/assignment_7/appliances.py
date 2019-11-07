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
      Accepts: 'On', 'on', 'Off' or 'off'. Default is 'Off'.
    
    Outputs:
    --------
    None
    """    
    
    def __init__(self, name, status='Off'):

        Appliance_Item.status_summary[name] = status

        self._name = name
        self._status = status

    def change_status(self, make_change):
        if make_change.casefold() == 'yes':
            if self.status == 'On':
                self.status = 'Off'
            elif self.status.casefold() == 'off':
                self.status = 'On'        

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(name, str), 'Name is not a string. Try again.'
        self._name = value

    @property
    def status(self):
        return self._status
        
    @status.setter
    def status(self, value):
        assert isinstance(value, str), 'Status is not a string. Try again.'
        if value.casefold() == 'on':
            self._status = 'On'
        elif value.casefold() == 'off':
            self._status = 'Off'
        else:
            ValueError('Status must be "On" or "Off".')
        
