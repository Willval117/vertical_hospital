# -*- coding: utf-8 -*-
{
    'name' : "Hospital vertical",
    'summary': "",
    'autor': "William Valencia",
    "version": "1.0.0",
    'sequence': 2,
    'depends':['base','base_setup'],
    'data':[
        'security/ir.model.access.csv',
        'data/sequence_patient.xml',
        'views/patient_view.xml',
        'views/treatment_view.xml',
    ],
    'qweb':[],
    'application':True,
    'installable':True,
    'auto_install':False,
}