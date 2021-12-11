# -*- coding: utf-8 -*-


from ast import *


class Render:
    

    template_source='config/template.svg'
    
            
    def __init__(self,file_name):
        
        
        self.Object_dictionnary={'cluster':(50,100),'network':(50,400)}
        
        self.positionObjet={}
               
        self.file_name=file_name
        

    def generate_template(self,dest_name, buffer_size=1024*1024):
        
        """      
        Copy a file from source to dest. source and dest

        
    
        """
        source=open(self.template_source)
        
        dest=open(dest_name,'w')
        
        while True:
            copy_buffer = source.read(buffer_size)
            if not copy_buffer:
                break
            dest.write(copy_buffer)
            
        dest.close()  
        
    
    def init_render(self):
        
        
        """
        
         this function init the render processing 
         
        """
        
        
        self.generate_template(self.file_name)
            
        self.output=open(self.file_name,'a')
                

 
    def close_render(self):
        
        
        
        """
        
        this function close  the svg tag and the ouput file 
        
        
        """
                
        self.output.write("</svg>")
        
        self.output.close()
                

    def draw_cluster(self,name,nb_computers,processor):
        
        
        
        """
        
        this function draw a cluster of computers 
        
        """
             
        key='cluster'
        
        x=self.Object_dictionnary[key][0]
        
        y=self.Object_dictionnary[key][1]
               
        self.positionObjet[name]=(x+105,y)

        nb_computers=int(nb_computers)
                      
        self.output.write("'<rect x='{}' y='{}' width='120' height='{}' rx='5'  style=' fill:#26CD22;'  />'".format(x-10,y,45*(nb_computers+1)))
            
        self.output.write("<text x='{}' y='{}'  style='fill:black;font-size:20px;'>{}</text>".format(x,y+15,name))

        ycomputer=y  
        
        for  i in range(nb_computers):
            
            ycomputer+=45
            
            self.output.write("'<rect x='{}' y='{}' width='100' height='40' rx='5'  style=' fill:#41c1f4;'  />'".format(x,ycomputer))
                
            node_name=   "Node"+str(i+1) 
            
            self.output.write("<text x='{}' y='{}'  style='fill:black;font-size:20px;'>{}</text>".format(x+15,ycomputer+30,node_name))        
                               
        self.Object_dictionnary[key]=(x+150,y)
        
                

    def draw_network(self,name,debit):
        
        
        """
        
         this function draw a network
        """
             
        
        key='network'
        
        
        x=self.Object_dictionnary[key][0]
        
        y=self.Object_dictionnary[key][1]
               
        self.positionObjet[name]=(x+105,y)

        label_debit=debit+'Kbit/s'
                
        self.output.write("'<rect x='{}' y='{}' width='120' height='60' rx='1'  style=' fill:#26CD22;'  />'".format(x,y))
                        
        self.output.write("<text x='{}' y='{}'  style='fill:black;font-size:20px;'>{}</text>".format(x+15,y+20,name))
            
        self.output.write("<text x='{}' y='{}'  style='fill:black;font-size:15px;'>{}</text>".format(x+15,y+40,label_debit))
        
        self.Object_dictionnary[key]=(x+150,y)




        
    def draw_connection(self,item1,item2):
             
        """
        
        this function draw a connection link betwen two element which can be (network <-> network ) or ( network<->cluster)
        """

        
        x1,y1=self.positionObjet[item1]
        
        x2,y2=self.positionObjet[item2]
               
        self.output.write("<line x1='{}' y1='{}' x2='{}' y2='{}' stroke='black' style=' fill:#26CD22;' stroke-width='3' />".format(x1,y1,x2,y2))
            
        self.output.write("<circle cx='{}' cy='{}' r='{}'   style=' fill:#d80250;'/>".format(x1,y1,5))            
            
        self.output.write("<circle cx='{}' cy='{}' r='{}'   style=' fill:#d80250;'/>".format(x2,y2,5))                   
     

            
    def draw_item(self,item):
        """
        
        this function analyze the item and call the right function to draw the element 
        """

        if  'Declaration' in  str(type(item))  :
        
            if item.type_.name=='Cluster':
                
                
                self.draw_cluster(item.identifier.name,item.primaries[0].value,item.primaries[1].value)
            
            elif item.type_.name=='Network':
            
                
                self.draw_network(item.identifier.name,item.primaries[0].value)
            
        elif 'Statement' in  str(type(item)) :
                       
             cluster_name=item.selectedobject_call_method.split('.')[0]
             
             network_name=item.primaries[0].value
             
             self.draw_connection(cluster_name,network_name)
            

