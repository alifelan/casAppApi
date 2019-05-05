from casApp.models import Date, Location, User, Casa, Event, Teacher, Class, Group
from datetime import datetime, timedelta
Location(name='Aulas 1', maps='https://www.google.com/maps/place/Aulas+1,+Av.+Del+Estado,+Tecnol%C3%B3gico,+Monterrey,+N.L./@25.6519307,-100.2923944,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bfb892a97d65:0x46930af15131d70f!8m2!3d25.6519259!4d-100.2902057',
         photo='https://geo3.ggpht.com/maps/photothumb/fd/v1?bpb=ChAKDnNlYXJjaC5UQUNUSUxFEkAKEgllfamSuL9ihhEP1zFR8QqTRhIKDccrSg8VRtE4xBoSCWcZqD64v2KGESaYbqfQg-ltKgoNWyxKDxXX7TjEGgYI8AEQmAM&gl=MX').save()
Location(name='Aulas 2', maps='https://www.google.com/maps/place/Aulas+2,+Av.+Eugenio+Garza+Sada+Sur,+Tecnol%C3%B3gico,+Monterrey,+N.L./@25.6509248,-100.2923944,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bfb8fb2bae25:0xc4ba7649ec7e4e97!8m2!3d25.65092!4d-100.2902057',
         photo='https://geo2.ggpht.com/maps/photothumb/fd/v1?bpb=ChAKDnNlYXJjaC5UQUNUSUxFEkAKEgklriv7uL9ihhGXTn7sSXa6xBIKDbkFSg8VDMM4xBoSCS0OaLvRv2KGEUF1kRJ7NxDhKgoNEAVKDxXX7TjEGgYI8AEQmAM&gl=MX').save()
Location(name='Aulas 3', maps='https://www.google.com/maps/place/Aulas+3,+Av.+Eugenio+Garza+Sada+Sur,+Tecnol%C3%B3gico,+Monterrey,+N.L./@25.649919,-100.2923944,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bfb91b312645:0x890ccb2496fd3db8!8m2!3d25.6499142!4d-100.2902057',
         photo='https://geo2.ggpht.com/maps/photothumb/fd/v1?bpb=ChAKDnNlYXJjaC5UQUNUSUxFEkAKEglFJjEbub9ihhG4Pf2WJMsMiRIKDUDUSQ8VffQ4xBoSCS0OaLvRv2KGEUF1kRJ7NxDhKgoNxt1JDxXX7TjEGgYI8AEQmAM&gl=MX').save()
Location(name='Aulas 4', maps='https://www.google.com/maps/place/Aulas+4/@25.6496521,-100.2911898,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bfb93b13d655:0x5d35a0db42588438!8m2!3d25.6496473!4d-100.2890011',
         photo='https://geo3.ggpht.com/maps/photothumb/fd/v1?bpb=ChAKDnNlYXJjaC5UQUNUSUxFEiwKEglV1hM7ub9ihhE4hFhC26A1XRIKDRPTSQ8VfwQ5xCoKDVnTSQ8V5Rw5xBoGCPABEJgD&gl=MX').save()
Location(name='Biotecnología', maps='https://www.google.com/maps/place/Centro+De+Biotecnolog%C3%ADa/@25.6522203,-100.2916037,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bfb8be17f3a7:0xaaebcedf4272c4f1!8m2!3d25.6522155!4d-100.289415',
         photo='https://lh5.googleusercontent.com/p/AF1QipPBBFa7OzaQJvqrk5AtgGyCMKGwN0N3mSf56DQN=w426-h240-k-no').save()
Location(name='Aulas 6', maps='https://www.google.com/maps/place/Aulas+6,+Av.+Junco+de+la+Vega,+Tecnol%C3%B3gico,+Monterrey,+Nuevo+Le%C3%B3n/@25.6516349,-100.2901154,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bfbf330ac0d1:0x43f392f4de634925!8m2!3d25.6516301!4d-100.2879267',
         photo='https://geo1.ggpht.com/cbk?panoid=82e4xBXN2LQo-6RGgfQISw&output=thumbnail&cb_client=search.TACTILE.gps&thumb=2&w=408&h=240&yaw=222.82613&pitch=0&thumbfov=100').save()
Location(name='Aulas 7', maps='https://www.google.com/maps/place/Aulas+7,+Tecnol%C3%B3gico,+Monterrey,+N.L./@25.6516349,-100.2901154,17z/data=!4m5!3m4!1s0x8662bfb932e0805f:0xaa205f89934b505a!8m2!3d25.6495448!4d-100.2883211',
         photo='https://geo3.ggpht.com/cbk?panoid=eHNCzMWNB4Pvx9qnzmRV9A&output=thumbnail&cb_client=search.TACTILE.gps&thumb=2&w=408&h=240&yaw=323.88614&pitch=0&thumbfov=100').save()
Location(name='Centro de Congresos', maps='https://www.google.com/maps/place/Grupo+Financiero+Banorte+Cajero/@25.6488789,-100.2899974,19.49z/data=!4m5!3m4!1s0x8662bfa1537ee279:0x1278d1c676d6e255!8m2!3d25.6489399!4d-100.2898999',
         photo='https://geo2.ggpht.com/maps/photothumb/fd/v1?bpb=ChAKDnNlYXJjaC5UQUNUSUxFEkAKEgl54n5Tob9ihhFV4tZ2xtF4EhIKDUTESQ8VMfk4xBoSCS0OaLvRv2KGEUF1kRJ7NxDhKgoNuLdJDxXI-TjEGgYI8AEQmAM&gl=MX').save()
Location(name='Biblioteca', maps='https://www.google.com/maps/place/Biblio+Tec/@25.6503998,-100.2919037,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bfb91e03da2d:0x23f512283b787392!8m2!3d25.650395!4d-100.289715',
         photo='https://lh5.googleusercontent.com/p/AF1QipOn0SVKiapFUaTzUYW3LBwUpMJ4T0QQH2A2dtfh=w408-h306-k-no').save()
Location(name='Gimnasio', maps='https://www.google.com/maps/place/Gym/@25.6486411,-100.2899804,19.53z/data=!4m5!3m4!1s0x8662bfb96c09f6e7:0x6ae71e689514d532!8m2!3d25.6487138!4d-100.2897236',
         photo='https://lh5.googleusercontent.com/p/AF1QipMx7zilyMXuj-I_Q7gZtKLOQM87vLn6ym3J7q54=w408-h544-k-no').save()
Location(name='Centrales', maps='https://www.google.com.mx/maps/place/Edificio+Centrales,+Tecnológico,+Monterrey,+N.L./@25.6515092,-100.2901194,18z/data=!3m1!4b1!4m5!3m4!1s0x8662bfb8c388c75d:0x35d6dd6c40d6849b!8m2!3d25.6515068!4d-100.2890224',
         photo='https://geo0.ggpht.com/maps/photothumb/fd/v1?bpb=ChAKDnNlYXJjaC5UQUNUSUxFEiAKEgldx4jDuL9ihhGbhNZAbN3WNSoKDfwbSg8VEBw5xBoGCPABEJgD&gl=MX').save()
Location(name='Learning Commons', maps='https://www.google.com.mx/maps/place/Enfermer%C3%ADa-+Centrales+2/@25.6512683,-100.2902266,18z/data=!3m1!4b1!4m5!3m4!1s0x8662bfb8c2b902e9:0x57ecb33f95da60ee!8m2!3d25.6512664!4d-100.2893844',
         photo='https://geo1.ggpht.com/maps/photothumb/fd/v1?bpb=ChAKDnNlYXJjaC5UQUNUSUxFEjQKEgnpArnCuL9ihhHuYNqVP7PsVxoSCW-4qz-iv2KGES1eLoZEK27rKgoNmBJKDxXsDTnEGgYI8AEQmAM&gl=MX').save()
Location(name='CETEC', maps='https://www.google.com.mx/maps/place/CETEC/@25.6503281,-100.293259,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bfb9ab2ede9d:0x2d625c445b0a7c8b!8m2!3d25.6503233!4d-100.291065',
         photo='https://lh5.googleusercontent.com/p/AF1QipNKQuSmIPKK2AAn6IOVapux3EY3N7s6E03--ljD=w408-h240-k-no-pi-10-ya161.99998-ro-0-fo100').save()
Location(name='CEDES', maps='https://www.google.com.mx/maps/place/Centro+de+Estudios+para+el+Desarrollo+Sostenible/@25.6536406,-100.2947227,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bfc7bc6b7dfb:0x37f2f7070d7122b9!8m2!3d25.6536358!4d-100.2925287',
         photo='https://lh5.googleusercontent.com/p/AF1QipNZE61wkvXkNOPTs4jAS0OCaeA3A0pjZJU_L5E=w408-h544-k-no').save()
Location(name='Rectoria', maps='https://www.google.com.mx/maps/place/Rector%C3%ADa+Tecnol%C3%B3gico+De+Monterrey/@25.6514666,-100.2931946,17z/data=!3m1!4b1!4m5!3m4!1s0x8662bfb85f2d38f1:0x1aa4a3c675016d3e!8m2!3d25.6514618!4d-100.2910006',
         photo='https://lh5.googleusercontent.com/p/AF1QipO6qVdbfPyv7Q5hea4MlCIwdW2w6EoKB1kF7RWb=w408-h306-k-no').save()

Date.objects.all().delete()
days = [0, 1, 2, 3, 4, 5]
x = datetime(1, 1, 1, 7)
for day in days:
    for i in range(8):
        time = (x + timedelta(hours=1, minutes=30) * i).time()
        Date(day=day, time=time).save()
    Date(day=day, time=datetime(1, 1, 1, 18).time()).save()
    Date(day=day, time=datetime(1, 1, 1, 19, 30).time()).save()

gallinas = Casa(name="Gallinas de Guinea")
gallinas.save()
Casa(name="Cuervos").save()
Casa(name="Venados").save()
Casa(name="Patos").save()
Casa(name="Pavo Reales").save()
ali = User(name="Ali", mat="A00821099", password="popopopo123", casa=gallinas)
ali.save()
User(name="admin", mat="admin", password="admin", casa=gallinas).save()
date = datetime.strptime('05/09/19 21:00', '%m/%d/%y %H:%M')
top = Event(name="Twenty One Pilots", description="Concierto de TOP",
            location="Arena Monterrey", date=date)
top.save()
date = datetime.strptime('06/20/19 14:00', '%m/%d/%y %H:%M')
machaca = Event(name="Machaca", description="Festival Machaca", location="Fundidora", date=date)
machaca.save()
ali.events.add(top)
ali.events.add(machaca)

mejorado = Teacher(teacher_name="Mejorado")
mejorado.save()
cl = Class(class_id="TC2024", class_name="AMSS")
cl.save()
gr = Group(class_id=cl, group_number=2, semester="EN19")
gr.save()
gr.teachers.add(mejorado)
gr.dates.add(Date.objects.all()[5])
ali.enrolled_in.add(gr)
